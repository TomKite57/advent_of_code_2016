def read_file(filename):
    with open(filename, 'r') as file:
        return [room_code(line) for line in file]

def make_string(letter_list):
    rval = ""
    for l in letter_list:
        rval += l
    return rval

def letter_cycle(letter, iterations):
    if letter == ' ':
        return letter
    x = ord(letter) - ord('a')
    x += iterations
    x %= (ord('z') - ord('a') + 1)
    return chr(x + ord('a'))


class room_code:
    def __init__(self, line):
        code, checksum = line.strip().split('[')
        id = code.split('-')[-1]
        self.code = code[:-len(id)-1]
        self.id = int(id)
        self.checksum = checksum[:-1]

    def calc_checksum(self):
        letters = set([l for l in self.code if l!='-'])
        sort_func = lambda l: ord('z')*self.code.count(l) - ord(l)
        letters = sorted(letters, key=sort_func, reverse=True)
        return make_string(letters[:5])

    def real_room(self):
        return self.calc_checksum() == self.checksum

    def decrypt(self):
        line = self.code.replace('-', ' ')
        return make_string([letter_cycle(l, self.id) for l in line])



if __name__ == "__main__":
    data = read_file("data/day_04.dat")

    print(sum([x.id for x in data if x.real_room()]))
    print(*[x.id for x in data if "north pole objects" in x.decrypt()])
