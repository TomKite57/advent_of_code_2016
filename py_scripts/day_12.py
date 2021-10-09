from aoc_tools import Advent_Timer

def readfile(fname):
    with open(fname, 'r') as file:
        return [line.strip() for line in file]

class game:
    def __init__(self, rules):
        self.rules = rules
        self.registers = {'a': 0,
                          'b': 0,
                          'c': 0,
                          'd': 0}
        self.pos = 0

    def get(self, reg):
        if reg in self.registers:
            return self.registers[reg]
        return int(reg)

    def take_step(self):
        r = self.rules[self.pos].split(' ')
        if r[0] == 'cpy':
            self.registers[r[2]] = self.get(r[1])
            self.pos += 1
            return
        elif r[0] == 'inc':
            self.registers[r[1]] += 1
            self.pos += 1
            return
        elif r[0] == 'dec':
            self.registers[r[1]] -= 1
            self.pos += 1
            return
        elif r[0] == 'jnz':
            if self.get(r[1]) != 0:
                self.pos += self.get(r[2])
            else:
                self.pos += 1
            return

    def full_advance(self):
        while self.pos < len(self.rules):
            self.take_step()

if __name__ == "__main__":
    timer = Advent_Timer()
    data = readfile("data/day_12.dat")

    g = game(data)
    g.full_advance()
    print("Part 1 checksum: {}".format(g.registers['a']))

    g = game(data)
    g.registers['c'] = 1
    g.full_advance()
    print("Part 2 checksum: {}".format(g.registers['a']))

    timer.end_hit()
