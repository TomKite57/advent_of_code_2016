def read_file(filename):
    with open(filename, 'r') as file:
        return [process_line(line) for line in file]

def process_line(line):
    A = line[:3]
    B = line[5:8]
    C = line[10:]
    return [int(x) for x in [A,B,C]]

def valid_triangle(line):
    a, b, c = line
    return (a+b>c and a+c>b and b+c>a)

def rotate_list(data):
    rval = []
    for i in range(2, len(data), 3):
        for j in [0,1,2]:
            rval.append([data[i-x][j] for x in [2,1,0]])
    return rval

if __name__ == "__main__":
    data = read_file("data/day_03.dat")
    print(sum([valid_triangle(line) for line in data]))
    print(sum([valid_triangle(line) for line in rotate_list(data)]))
