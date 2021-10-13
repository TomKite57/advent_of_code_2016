from aoc_tools import Advent_Timer
from collections import deque

def remove_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)
    return d

class elf_game:
    def __init__(self, num):
        self.tot = num

    def full_advance_p1(self):
        remaining = deque([i+1 for i in range(self.tot)])
        for _ in range(len(remaining)-1):
            remaining = remove_nth(remaining, 1)
            remaining.rotate(-1)
        return remaining[0]

    def full_advance_p2(self):
        remaining = deque([i+1 for i in range(self.tot)])

        for _ in range(len(remaining)-1):
            remaining = remove_nth(remaining, len(remaining)//2)
            remaining.rotate(-1)
        return remaining[0]

    def show(self):
        tmp = ""
        for i in range(self.tot):
            if self.current == i:
                tmp += "(" + str(self.elves[i]) + ") "
            else:
                tmp += str(self.elves[i]) + " "
        print(tmp)

if __name__ == "__main__":
    timer = Advent_Timer()
    data = 3_005_290
    data = 5

    g = elf_game(data)
    print("Lucky elf: {}".format(g.full_advance_p1()))
    print("Lucky elf: {}".format(g.full_advance_p2()))

    timer.end_hit()
