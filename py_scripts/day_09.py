from copy import deepcopy

def readfile(fname):
    with open(fname, 'r') as file:
        return file.read().strip()


def get_marker(line, ind1):
    if line[ind1] != '(':
        return
    ind2 = deepcopy(ind1)
    while line[ind2] != ')':
        ind2 += 1

    a, b = [int(x) for x in line[ind1+1:ind2].split('x')]
    return ind1, ind2, a, b


def decompress(line):
    ind = 0
    while ind < len(line):
        if line[ind] == '(':
            _, ind2, a, b = get_marker(line, ind)
            line = line[:ind] + line[ind2+1:ind2+1+a]*(b-1) + line[ind2+1:]
            ind = ind + a*b
            continue
        ind+=1
    return line


def full_decompress(line):
    ind = 0
    while ind < len(line):
        if line[ind] == '(':
            _, ind2, a, b = get_marker(line, ind)
            line = line[:ind] + line[ind2+1:ind2+1+a]*(b-1) + line[ind2+1:]
            continue
        ind+=1
    return line


def get_mult_fac(mult_facs):
    total = 1
    for i in range(len(mult_facs)):
        total *= mult_facs[i][0]
    return total


def mult_fac_decrease(mult_facs, delta):
    for i in range(len(mult_facs)):
        mult_facs[i][1] += delta
    return [p for p in mult_facs if p[1] > 0]


def quick_p2(line):
    ind = 0
    total = 0
    mult_facs = []
    while ind < len(line):
        if line[ind] == '(':
            ind1, ind2, a, b = get_marker(line, ind)
            ind = ind2 + 1
            mult_facs = mult_fac_decrease(mult_facs, ind1-ind2-1)
            mult_facs.append( [b,a] )
            continue
        total += get_mult_fac(mult_facs)
        mult_facs = mult_fac_decrease(mult_facs, -1)
        ind+=1
    return total


if __name__ == "__main__":
    data = readfile("data/day_09.dat")
    print(len(decompress(data)))
    print(quick_p2(data))
