def read_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip('\n').split(', ')

class lil_guy:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direc = 0
        self.positions = [(self.x, self.y), ]

    def rotate(self, char_in):
        if char_in == 'R':
            self.direc = (self.direc + 1)%4
        else:
            self.direc = (self.direc - 1)%4
        if self.direc < 0:
            self.direc += 4

    def move(self, steps=1):
        if (self.direc == 0):
            self.y += steps
        elif (self.direc == 1):
            self.x += steps
        elif (self.direc == 2):
            self.y -= steps
        elif (self.direc == 3):
            self.x -= steps

        self.positions.append( (self.x, self.y) )

    def distance(self):
        return abs(self.x) + abs(self.y)

    def find_intersection(self):
        for i in range(1, len(self.positions)):
            for j in range(1, i-1):
                hit, fx, fy = intersect(self.positions[i-1], self.positions[i],
                                        self.positions[j-1], self.positions[j])
                if hit:
                    return abs(fx) + abs(fy)
        return -1


def is_vert(p1, p2):
    if p1[0] == p2[0]:
        return True
    return False

def is_hori(p1, p2):
    if p1[1] == p2[1]:
        return True
    return False

def intersect(p1, p2, q1, q2):
    if is_vert(p1, p2) and is_vert(q1, q2):
        return False, -1, -1
    if is_hori(p1, p2) and is_hori(q1, q2):
        return False, -1, -1

    if not is_vert(p1, p2):
        p1, p2, q1, q2 = q1, q2, p1, p2

    x_val = p1[0]
    y_val = q1[1]

    if not (q1[0] <= x_val <= q2[0] or q2[0] <= x_val <= q1[0]):
        return False, -1, -1
    if not (p1[1] <= y_val <= p2[1] or p2[1] <= y_val <= p1[1]):
        return False, -1, -1
    return True, x_val, y_val


if __name__ == "__main__":
    instruc = read_file("data/day_01.dat")
    guy = lil_guy()

    for path in instruc:
        rot, step = path[0], int(path[1:])
        guy.rotate(rot)
        guy.move(step)

    print(guy.distance())
    print(guy.find_intersection())
