from aoc_tools import Advent_Timer

def readfile(fname):
    with open(fname, 'r') as file:
        return int(file.read())

def manhat_dist(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

def is_wall(x, y, num):
    rval = x*x + 3*x + 2*x*y + y + y*y
    rval += num
    rval = bin(rval)[2:].count('1')
    return rval%2 != 0

def is_open(x, y, num):
    return not is_wall(x, y, num)

class astar_cell:
    def __init__(self, G, H, came_from):
        self.G = G
        self.H = H
        self.F = G + H
        self.came_from = came_from

def astar_step(open_paths, maze_state, pout, num, maxstep):
    open_paths = sorted(open_paths, key=lambda x: maze_state[x].F, reverse=True)
    p = open_paths.pop()

    steps = [[1,0], [-1,0], [0,1], [0,-1]]

    for s in steps:
        pnew = (p[0] + s[0], p[1] + s[1])
        if -1 in pnew:
            continue
        if is_wall(*pnew, num):
            continue
        if pnew in maze_state and maze_state[pnew].G <= maze_state[p].G+1:
            continue
        if maze_state[p].G+1 >= maxstep:
            continue
        maze_state[pnew] = astar_cell(maze_state[p].G+1, manhat_dist(*pnew, *pout), s)
        if (pnew == pout):
            maxstep = maze_state[p].G+1
        else:
            open_paths.append(pnew)



    return open_paths, maze_state, maxstep

def shortest_path_length(maze_state, pout):
    return len(shortest_path(maze_state, pout)) - 1

def shortest_path(maze_state, pout):
    path = [pout,]
    while cf := maze_state[pout].came_from:
        pout = (pout[0] - cf[0], pout[1] - cf[1])
        path.append(pout)
    return path[::-1]

def count_locs_within(maze_state, limit):
    return len([1 for c in maze_state if maze_state[c].G <= limit])

def show_maze(maze_state, pin, pout, num):
    cells = maze_state.keys()
    xmin = min([c[0] for c in cells]) - 1
    xmax = max([c[0] for c in cells]) + 2
    ymin = min([c[1] for c in cells]) - 1
    ymax = max([c[1] for c in cells]) + 2
    short_p = set(shortest_path(maze_state, pout))

    for y in range(ymax - ymin):
        tmp = ""
        for x in range(xmax - xmin):
            p = (xmin + x, ymin + y)
            if p == pin:
                tmp += "A"
            elif p == pout:
                tmp += "B"
            elif p in short_p:
                tmp += "O"
            elif p in maze_state:
                tmp += "."
            elif is_wall(*p, num):
                tmp += "#"
            else:
                tmp += " "
        print(tmp)


if __name__ == "__main__":
    timer = Advent_Timer()
    data = readfile("data/day_13.dat")
    pin  = (1,  1)
    pout = (31, 39)

    open_paths = [pin,]
    maze_state = dict()
    maze_state[open_paths[-1]] = astar_cell(0, manhat_dist(*pin, *pout), None)
    maxstep = float("inf")

    while len(open_paths) != 0:
        open_paths, maze_state, maxstep = astar_step(open_paths, maze_state, pout, data, maxstep)

    #show_maze(maze_state, pin, pout, data)

    print("Shortest path is {} long".format(shortest_path_length(maze_state, pout)))
    print("Can visit {} locations within 50 steps".format(count_locs_within(maze_state, 50)))
    timer.end_hit()
