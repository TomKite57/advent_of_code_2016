from aoc_tools import Advent_Timer

def parse_line(line):
    if line[0] != '/':
        return
    line = line[len("/dev/grid/node-"):]
    line = line.strip().split()
    x, y = [int(z[1]) for z in line[0].split('-')]
    size, used, avail, perc = [int(x[:-1]) for x in line[1:]]
    return [x, y, used, avail]
    #return [x, y, size, used, avail, perc]

def read_file(fname):
    with open(fname, 'r') as file:
        return [parse_line(line) for line in file][2:]

def count_valid_pairs(nodes):
    return len([1 for n1 in nodes for n2 in nodes if (n1 != n2 and n1[2] != 0 and n1[2] < n2[3])])

if __name__ == "__main__":
    timer = Advent_Timer()
    data = read_file("data/day_22.dat")

    print("Valid pairs: {}".format(count_valid_pairs(data)))

    timer.end_hit()
