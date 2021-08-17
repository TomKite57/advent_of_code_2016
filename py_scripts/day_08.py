def make_string(letter_list):
    rval = ""
    for l in letter_list:
        if l == 0:
            rval += '.'
        elif l == 1:
            rval += '#'
    return rval

def readfile(fname):
    with open(fname, 'r') as file:
        return [line.strip() for line in file]

def parse_rule(line):
    if line[:5] == "rect ":
        a, b = line[5:].split('x')
        return 'rec', int(a), int(b)

    if line[:13] == "rotate row y=":
        line, b = line.split(' by ')
        _, a = line.split('y=')
        return 'row', int(a), int(b)

    if line[:16] == "rotate column x=":
        line, b = line.split(' by ')
        _, a = line.split('x=')
        return 'col', int(a), int(b)

class screen:
    def __init__(self):
        self.grid = [[0 for _ in range(50)] for _ in range(6)]

    def swap(self, x, y):
        self.grid[y][x] = int(not self.grid[y][x])

    def advance(self, rule):
        rule, a, b = parse_rule(rule)
        if rule == 'rec':
            self.rect(a, b)
        elif rule == 'row':
            self.row(a, b)
        elif rule == 'col':
            self.col(a, b)

    def rect(self, a, b):
        [self.swap(x, y) for x in range(a) for y in range(b)]

    def row(self, a, b):
        old_row = [self.grid[a][i] for i in range(len(self.grid[a]))]
        for x in range(len(self.grid[a])):
            self.grid[a][x] = old_row[(x-b)%len(self.grid[a])]

    def col(self, a, b):
        old_col = [self.grid[i][a] for i in range(len(self.grid))]
        for y in range(len(self.grid)):
            self.grid[y][a] = old_col[(y-b)%len(self.grid)]

    def show(self):
        for row in self.grid:
            print(make_string(row))

    def pixel_count(self):
        return sum(sum(row) for row in self.grid)

    def print_word(self):
        for counter in range(0, len(self.grid[0]), 5):
            for row in self.grid:
                print(make_string(row[counter:counter+5]))
            print()


if __name__ == "__main__":
    data = readfile("data/day_08.dat")
    my_screen = screen()

    for rule in data:
        my_screen.advance(rule)

    print(my_screen.pixel_count(), '\n')
    my_screen.print_word()
