from aoc_tools import Advent_Timer

def dragon_step(a):
    b = ""
    for c in a[::-1]:
        b += str(int(bool(not int(c))))
    return a + '0' + b

def checksum(a):
    if len(a)%2 != 0:
        return a

    rval = ""
    for i in range(0, len(a), 2):
        if a[i] == a[i+1]:
            rval += "1"
        else:
            rval += "0"
    return checksum(rval)

def solve(a, length):
    while len(a) < length:
        a = dragon_step(a)
    return checksum(a[:length])

if __name__ == "__main__":
    timer = Advent_Timer()

    print("Checksum is {}.".format(solve('10011111011011001', 272)))
    print("Checksum is {}.".format(solve('10011111011011001', 35651584)))

    timer.end_hit()
