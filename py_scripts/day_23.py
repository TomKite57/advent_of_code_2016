from aoc_tools import Advent_Timer

TGL_MAP = {'inc': 'dec', 'dec': 'inc', 'tgl' : 'inc', 'jnz': 'cpy', 'cpy': 'jnz'}

def isnum(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def readfile(fname):
    with open(fname, 'r') as file:
        return [line.strip() for line in file]

class game:
    def __init__(self, rules):
        self.rules = rules
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        self.pos = 0
        self.toggled = dict()
        for i in range(len(self.rules)):
            self.toggled[i] = False

    def get(self, reg):
        if reg in self.registers:
            return self.registers[reg]
        return int(reg)

    def take_step(self):
        r = self.rules[self.pos].split(' ')

        if self.toggled[self.pos]:
            r[0] = TGL_MAP[r[0]]

        if r[0] == 'cpy':
            if not isnum(r[2]):
                self.registers[r[2]] = self.get(r[1])
            self.pos += 1
            return
        if r[0] == 'inc':
            if not isnum(r[1]):
                self.registers[r[1]] += 1
            self.pos += 1
            return
        if r[0] == 'tgl':
            tgt = self.pos + self.get(r[1])
            if tgt in self.toggled:
                self.toggled[tgt] = not self.toggled[tgt]
            self.pos += 1
            return
        if r[0] == 'dec':
            if not isnum(r[1]):
                self.registers[r[1]] -= 1
            self.pos += 1
            return
        if r[0] == 'jnz':
            if self.get(r[1]) != 0:
                self.pos += self.get(r[2])
            else:
                self.pos += 1
            return

    def full_advance(self):
        while self.pos < len(self.rules):
            print(self.pos, self.registers)
            self.take_step()

if __name__ == "__main__":
    timer = Advent_Timer()
    data = readfile("data/day_23.dat")

    g = game(data)
    g.registers['a'] = 7
    g.full_advance()
    print("Part 1 checksum: {}".format(g.registers['a']))

    #g = game(data)
    #g.registers['a'] = 12
    #g.full_advance()
    #print("Part 2 checksum: {}".format(g.registers['a']))

    timer.end_hit()





"""
0   cpy a b             7 7 0 0
1   dec b               7 6 0 0
2   cpy a d             7 6 0 7
3   cpy 0 a             0 6 7 7
4   cpy b c             0 6 6 7
#=============#
5   inc a               (1) 6  6  7 // (2) 6  6  7 //...//                      |
6   dec c                1  6 (5) 7 //  2  6 (5) 7 //...// (6) 6 (0) 7          | a += b
7   jnz c -2
#=============#
8   dec d               6 6 0 (6) --------------------------------------------->|
9   jnz d -5                                                                    | a += b*d
#=============#
10  dec b               64 (5) 0  0
11  cpy b c             64  5  5  0
12  cpy c d             64  5  5  5
#=============#
13  dec d               64  5  5 (4) // 64  5  6 (3) //...//                    |
14  inc c               64  5 (6) 4  // 64  5 (7) 3  //...// 64  5 (10) (0) --->| c = 2*b
15  jnz d -2
#=============#
16  tgl c               64 5 10 0 [HOW DOES THIS CHANGE FOR 12] b=a-2, c=2a-4    [10 for a=7, 20 for a=12]
17  cpy -16 c           Back to beggining but with 10 toggled... (b=a) OR Back to beggining but with 20 toggled...
18  jnz 1 c
19  cpy 97 c
20  jnz 79 d
#=============#
21  inc a
22  inc d
23  jnz d -2
#=============#
24  inc c
25  jnz c -5
"""





"""
5 {'a': 5034, 'b': 2, 'c': 2, 'd': 3}
6 {'a': 5035, 'b': 2, 'c': 2, 'd': 3}
7 {'a': 5035, 'b': 2, 'c': 1, 'd': 3}
5 {'a': 5035, 'b': 2, 'c': 1, 'd': 3}
6 {'a': 5036, 'b': 2, 'c': 1, 'd': 3}
7 {'a': 5036, 'b': 2, 'c': 0, 'd': 3}
8 {'a': 5036, 'b': 2, 'c': 0, 'd': 3}
9 {'a': 5036, 'b': 2, 'c': 0, 'd': 2}
4 {'a': 5036, 'b': 2, 'c': 0, 'd': 2}
5 {'a': 5036, 'b': 2, 'c': 2, 'd': 2}
6 {'a': 5037, 'b': 2, 'c': 2, 'd': 2}
7 {'a': 5037, 'b': 2, 'c': 1, 'd': 2}
5 {'a': 5037, 'b': 2, 'c': 1, 'd': 2}
6 {'a': 5038, 'b': 2, 'c': 1, 'd': 2}
7 {'a': 5038, 'b': 2, 'c': 0, 'd': 2}
8 {'a': 5038, 'b': 2, 'c': 0, 'd': 2}
9 {'a': 5038, 'b': 2, 'c': 0, 'd': 1}
4 {'a': 5038, 'b': 2, 'c': 0, 'd': 1}
5 {'a': 5038, 'b': 2, 'c': 2, 'd': 1}
6 {'a': 5039, 'b': 2, 'c': 2, 'd': 1}
7 {'a': 5039, 'b': 2, 'c': 1, 'd': 1}
5 {'a': 5039, 'b': 2, 'c': 1, 'd': 1}
6 {'a': 5040, 'b': 2, 'c': 1, 'd': 1}
7 {'a': 5040, 'b': 2, 'c': 0, 'd': 1}
8 {'a': 5040, 'b': 2, 'c': 0, 'd': 1}
9 {'a': 5040, 'b': 2, 'c': 0, 'd': 0}
10 {'a': 5040, 'b': 2, 'c': 0, 'd': 0}
11 {'a': 5040, 'b': 1, 'c': 0, 'd': 0}
12 {'a': 5040, 'b': 1, 'c': 1, 'd': 0}
13 {'a': 5040, 'b': 1, 'c': 1, 'd': 1}
14 {'a': 5040, 'b': 1, 'c': 1, 'd': 0}
15 {'a': 5040, 'b': 1, 'c': 2, 'd': 0}
16 {'a': 5040, 'b': 1, 'c': 2, 'd': 0}
17 {'a': 5040, 'b': 1, 'c': 2, 'd': 0}
18 {'a': 5040, 'b': 1, 'c': -16, 'd': 0}
19 {'a': 5040, 'b': 1, 'c': 1, 'd': 0}
20 {'a': 5040, 'b': 1, 'c': 97, 'd': 0}
21 {'a': 5040, 'b': 1, 'c': 97, 'd': 79}
22 {'a': 5041, 'b': 1, 'c': 97, 'd': 79}
23 {'a': 5041, 'b': 1, 'c': 97, 'd': 78}
21 {'a': 5041, 'b': 1, 'c': 97, 'd': 78}
22 {'a': 5042, 'b': 1, 'c': 97, 'd': 78}
23 {'a': 5042, 'b': 1, 'c': 97, 'd': 77}
21 {'a': 5042, 'b': 1, 'c': 97, 'd': 77}
22 {'a': 5043, 'b': 1, 'c': 97, 'd': 77}
23 {'a': 5043, 'b': 1, 'c': 97, 'd': 76}
21 {'a': 5043, 'b': 1, 'c': 97, 'd': 76}
22 {'a': 5044, 'b': 1, 'c': 97, 'd': 76}
23 {'a': 5044, 'b': 1, 'c': 97, 'd': 75}
21 {'a': 5044, 'b': 1, 'c': 97, 'd': 75}
22 {'a': 5045, 'b': 1, 'c': 97, 'd': 75}
"""
