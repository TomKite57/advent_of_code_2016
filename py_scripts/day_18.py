from aoc_tools import Advent_Timer

tile_map = \
{
    "^^.": "^",
    ".^^": "^",
    "^..": "^",
    "..^": "^",
}

def gen_row(row):
    row = "." + row + "."
    rval = ""
    for i in range(1, len(row)-1):
        rval += tile_map.get(row[i-1:i+2], ".")
    return rval

def count_safe(row, length):
    rval = row.count('.')
    for _ in range(length-1):
        row = gen_row(row)
        rval += row.count('.')
    return rval

if __name__ == "__main__":
    timer = Advent_Timer()
    data = "^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^......."

    print("Number of safe tiles: {}".format(count_safe(data, 40)))
    print("Number of safe tiles: {}".format(count_safe(data, 400000)))

    timer.end_hit()
