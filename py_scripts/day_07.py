def readfile(fname):
    with open(fname, 'r') as file:
        return [ip_segment(line) for line in file]

def has_ABBA(line):
    return len([1 for i in range(len(line)-3)
                if line[i:i+4] == line[i:i+4][::-1] and line[i] != line[i+1]])

def get_ABA(line):
    return [line[i:i+3] for i in range(len(line)-2)
            if line[i] == line[i+2] and line[i] != line[i+1]]

def has_BAB(line1, line2):
    BABs = get_ABA(line1)
    ABAs = get_ABA(line2)
    for cand_a in ABAs:
        if cand_a[1] + cand_a[0] + cand_a[1] in BABs:
            return True
    return False

class ip_segment:
    def __init__(self, inline):
        self.hypernet_subsegs = []
        self.supernet_subsegs = []
        self.mode = 0

        line = ""
        for i, char in enumerate(inline):
            if char == '[':
                if len(line):
                    self.supernet_subsegs.append(line)
                    line = ""
                continue
            if char == ']':
                if len(line):
                    self.hypernet_subsegs.append(line)
                    line = ""
                continue
            line += char

        if len(line):
            self.supernet_subsegs.append(line)

    def is_TLS(self):
        for line in self.hypernet_subsegs:
            if has_ABBA(line):
                return False
        for line in self.supernet_subsegs:
            if has_ABBA(line):
                return True
        return False

    def is_SSL(self):
        return any([has_BAB(a,b) for a in self.supernet_subsegs for b in self.hypernet_subsegs])


if __name__ == "__main__":
    data = readfile("data/day_07.dat")
    print(len([1 for ip in data if ip.is_TLS()]))
    print(len([1 for ip in data if ip.is_SSL()]))
