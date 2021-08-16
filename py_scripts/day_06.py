def make_string(letter_list):
    rval = ""
    for l in letter_list:
        rval += l
    return rval

def readfile(fname):
    with open(fname, 'r') as file:
        return [line.strip() for line in file]

def get_common_char(data, row, reverse):
    chars = [line[row] for line in data]
    return sorted([x for x in set(chars)], reverse=reverse, key=lambda x:chars.count(x))[0]

def get_message(data, reverse):
    return make_string([get_common_char(data, i, reverse) for i in range(len(data[0]))])

if __name__ == "__main__":
    data = readfile("data/day_06.dat")
    print(get_message(data, True))
    print(get_message(data, False))
