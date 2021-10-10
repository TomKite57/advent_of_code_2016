from aoc_tools import Advent_Timer
import hashlib

OPEN_DOORS = set(['b', 'c', 'd', 'e', 'f'])
DPOS_DICT = {'U': [0, -1], 'D': [0, 1], 'L': [-1, 0], 'R': [1, 0]}

def hash(str_in):
    return hashlib.md5(str_in.encode('utf-8')).hexdigest()

class explorer:
    def __init__(self, password):
        self.password = password
        self.history = ""
        self.pos = [0, 0]

    def clone(self, new_direc=None):
        rval = explorer(self.password)
        rval.pos = [p for p in self.pos]
        for c in self.history:
            rval.history += c
        if new_direc is not None:
            rval.history += new_direc
            rval.pos = [p + dp for p, dp in zip(rval.pos, DPOS_DICT[new_direc])]
        return rval

    def move(self):
        if self.at_goal():
            return []
        u, d, l, r = hash(self.password + self.history)[:4]
        new_explorers = []

        if u in OPEN_DOORS and self.pos[1] != 0:
            new_explorers.append(self.clone('U'))
        if d in OPEN_DOORS and self.pos[1] != 3:
            new_explorers.append(self.clone('D'))
        if l in OPEN_DOORS and self.pos[0] != 0:
            new_explorers.append(self.clone('L'))
        if r in OPEN_DOORS and self.pos[0] != 3:
            new_explorers.append(self.clone('R'))

        return new_explorers

    def at_goal(self):
        if self.pos == [3, 3]:
            return True

def shortest_path(pword):
    paths = [explorer(pword),]
    while len(paths) != 0:
        new_paths = []
        for p in paths:
            new_paths += p.move()
        for p in new_paths:
            if p.at_goal():
                return p.history
        paths = new_paths
    return ""

def longest_path(pword):
    rval = -1
    paths = [explorer(pword),]
    while len(paths) != 0:
        new_paths = []
        for p in paths:
            new_paths += p.move()
        for p in new_paths:
            if p.at_goal():
                rval = len(p.history)
        paths = new_paths
    return rval


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Shortest path is\n{}".format(shortest_path("njfxhljp")))
    print("Longest path is\n{}".format(longest_path("njfxhljp")))

    timer.end_hit()
