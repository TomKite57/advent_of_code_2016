from aoc_tools import Advent_Timer

class game:
    def __init__(self, disks):
        self.disks = disks

    def state_at_time(self, t):
        return [d[1]+t%d[0] for d in self.disks]

    def ball_states(self, t):
        return [(d[1]+t+i+1)%d[0] for i, d in enumerate(self.disks)]

    def find_first_pass_trivial(self):
        t=0
        while True:
            if self.ball_states(t) == [0,]*len(self.disks):
                return t
            t += 1

    def find_first_pass_smort(self):
        t=0
        mult = 1
        for i in range(len(self.disks)):
            while True:
                if self.ball_states(t)[i] == 0:
                    mult *= self.disks[i][0]
                    break
                t += mult
        return t

if __name__ == "__main__":
    timer = Advent_Timer()

    #disks = [[5, 4], [2, 1]]
    disks = [[17, 1], [7, 0], [19, 2], [5, 0], [3, 0], [13, 5]]
    g = game(disks)
    print("First pass: {}.".format(g.find_first_pass_smort()))

    disks = [[17, 1], [7, 0], [19, 2], [5, 0], [3, 0], [13, 5], [11, 0]]
    g = game(disks)
    print("First pass: {}.".format(g.find_first_pass_smort()))

    timer.end_hit()
