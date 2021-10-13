from aoc_tools import Advent_Timer
from itertools import permutations as perm

def read_file(fname):
    with open(fname, 'r') as file:
        return [line.strip() for line in file]

def parse_rule(pword, rule):
    rule = rule.split(' ')

    if rule[0] == "swap":
        if rule[1] == "position":
            pword = ind_swap(pword, int(rule[2]), int(rule[5]))
        elif rule[1] == "letter":
            pword = let_swap(pword, rule[2], rule[5])

    elif rule[0] == "reverse":
        pword = reverse(pword, int(rule[2]), int(rule[4]))

    elif rule[0] == "rotate":
        if rule[1] == "left":
            pword = rotate_l(pword, int(rule[2]))
        elif rule[1] == "right":
            pword = rotate_r(pword, int(rule[2]))
        elif rule[1] == "based":
            pword = rotate_x(pword, rule[6])

    elif rule[0] == "move":
        pword = move(pword, int(rule[2]), int(rule[5]))

    return pword

def ind_swap(pword, i, j):
    if i > j:
        return ind_swap(pword, j, i)
    c = pword.pop(i)
    pword.insert(j-1, c)
    c = pword.pop(j)
    pword.insert(i, c)
    return pword

def let_swap(pword, x, y):
    for i, c in enumerate(pword):
        if c == x:
            pword[i] = y
        elif c == y:
            pword[i] = x
    return pword

def rotate_l(pword, num):
    rval = [None for x in pword]
    for i in range(len(pword)):
        rval[i] = pword[(i+num)%len(pword)]
    return rval

def rotate_r(pword, num):
    rval = [None for x in pword]
    for i in range(len(pword)):
        rval[i] = pword[(i-num)%len(pword)]
    return rval

def rotate_x(pword, x):
    i = pword.index(x)
    if i < 4:
        return rotate_r(pword, 1+i)
    else:
        return rotate_r(pword, 2+i)

def reverse(pword, i, j):
    return pword[:i] + pword[i:j+1][::-1] + pword[j+1:]

def move(pword, i, j):
    c = pword.pop(i)
    pword.insert(j, c)
    return pword

def list_to_string(arr):
    tmp = ""
    for x in arr:
        tmp += str(x)
    return tmp

def scramble_search(rules, string):
    goal = [c for c in string]
    base = [chr(ord('a') + i) for i in range(len(string))]
    for op in perm(base, len(base)):
        tmp = [x for x in op]
        for rule in rules:
            tmp = parse_rule(tmp, rule)
        if tmp == goal:
            return list(op)


if __name__ == "__main__":
    timer = Advent_Timer()
    data = read_file("data/day_21.dat")

    pword = [c for c in "abcdefgh"]
    for rule in data:
        pword = parse_rule(pword, rule)
    print("Scrambled password: {}".format(list_to_string(pword)))
    print("Matching password: {}".format(list_to_string(scramble_search(data, "fbgdceah"))))

    timer.end_hit()
