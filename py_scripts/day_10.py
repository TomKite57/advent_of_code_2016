def minmax(a, b):
    return min(a, b), max(a, b)

def readfile(fname):
    with open(fname, 'r') as file:
        return [parse_input(line.strip()) for line in file]


def parse_input(line):
    if (discriminator := line[:3]) == 'bot':
        _, num, _, _, _, l_recip, l_num, _, _, _, h_recip, h_num = line.split(' ')
        return ['bot', int(num), l_recip, int(l_num), h_recip, int(h_num)]
    elif discriminator == 'val':
        _, num_a, _, _, recip, num_b = line.split(' ')
        return ['value', int(num_a), recip, int(num_b)]
    else:
        raise Exception("Did not recognise rule starting with \"{}\"".format(discriminator))


class game:
    def __init__(self, rules):
        self.bot_dict = dict()
        self.bin_dict = dict()
        self.bot_rule_dict = dict()

        # Gather all bots and output bins
        for line in rules:
            for i in range(0, len(line), 2):
                if line[i] == 'bot':
                    self.bot_dict[line[i+1]] = []
                elif line[i] == 'output':
                    self.bin_dict[line[i+1]] = []

        # Set rules
        for line in rules:
            if line[0] == 'bot':
                self.bot_rule_dict[line[1]] = line[2:]

        # Set initial state
        for line in rules:
            if line[0] == 'value':
                self.bot_dict[line[3]].append(line[1])


    def send_val(self, val, what, who):
        if what == 'bot':
            self.bot_dict[who].append(val)
        else:
            self.bin_dict[who].append(val)

    def advance(self):
        bots_to_advance = [bot for bot in self.bot_dict if len(self.bot_dict[bot])>=2]

        if len(bots_to_advance) == 0:
            return False

        for bot in bots_to_advance:
            rule = self.bot_rule_dict[bot]
            a, b = minmax(self.bot_dict[bot].pop(0), self.bot_dict[bot].pop(0))
            self.send_val(a, rule[0], rule[1])
            self.send_val(b, rule[2], rule[3])

        return True

    def full_advance(self):
        while (self.advance()):
            for bot in self.bot_dict:
                if (61 in self.bot_dict[bot]) and (17 in self.bot_dict[bot]):
                    print("Bot {} is sorting the 61 and 17 chips".format(bot))
            pass
        return

    def checksum(self):
        return self.bin_dict[0][0]*self.bin_dict[1][0]*self.bin_dict[2][0]


if __name__ == "__main__":
    data = readfile("data/day_10.dat")

    my_game = game(data)
    my_game.full_advance()
    print("Checksum is {}".format(my_game.checksum()))
