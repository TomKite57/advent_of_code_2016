from aoc_tools import Advent_Timer

def read_file(fname):
    with open(fname, 'r') as file:
        return [[int(x) for x in line.strip().split('-')] for line in file]

def lowest_ip(rules, ip=0):
    for r in rules:
        if r[0] <= ip <= r[1]:
            return lowest_ip(rules, r[1]+1)
    return ip

def all_ips(rules, max_val=4294967295):
    count = 1
    prev_ip = lowest_ip(rules)
    while True:
        prev_ip = lowest_ip(rules, prev_ip+1)
        if prev_ip > max_val:
            return count
        count += 1

if __name__ == "__main__":
    timer = Advent_Timer()
    data = read_file("data/day_20.dat")

    print("Lowest valid ip: {}".format(lowest_ip(data)))
    print("Total valid ips: {}".format(all_ips(data)))

    timer.end_hit()
