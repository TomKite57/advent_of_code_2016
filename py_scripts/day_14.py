from aoc_tools import Advent_Timer
import hashlib

def hash(str_in):
    return hashlib.md5(str_in.encode('utf-8')).hexdigest()

def memoize(function):
  memo = {}
  def wrapper(*args):
    if args in memo:
      return memo[args]
    else:
      rv = function(*args)
      memo[args] = rv
      return rv
  return wrapper

@memoize
def trip_quint(string_in, advanced):
    string = hash(string_in)
    if advanced:
        for _ in range(2016):
            string = hash(string)
    trips = []
    quints = []
    trip_cands = set()
    quint_cands = set()
    for c in set(string):
        count = string.count(c)
        if count >= 3:
            trip_cands.add(c)
            if count >= 5:
                quint_cands.add(c)

    if trip_cands:
        for i, c in enumerate(string[:-2]):
            if c not in trip_cands:
                continue
            if c == string[i+1] == string[i+2]:
                trips.append(c)
    else:
        return trips, quints

    if quint_cands:
        for i, c in enumerate(string[:-4]):
            if c not in quint_cands:
                continue
            if c == string[i+1] == string[i+2] == string[i+3] == string[i+4]:
                quints.append(c)
    return trips, quints


class generator:
    def __init__(self, salt, advanced):
        self.salt = salt
        self.counter = -1
        self.passwords_found = 0
        self.advanced = advanced

    def advenced_hash(self):
        string = self.salt + str(self.counter)
        for _ in range(2017):
            string = hash(string)
        return string

    def advance(self):
        self.counter += 1
        char1, _ = trip_quint(self.salt + str(self.counter), self.advanced)
        if not char1:
            return
        for i in range(1, 1001):
            _, char2 = trip_quint(self.salt + str(self.counter + i), self.advanced)
            if char2 and char1[0] in char2:
                self.passwords_found += 1
                break


if __name__ == "__main__":
    timer = Advent_Timer()

    salt = 'abc'
    salt = 'jlmsuwbz'

    my_gen1 = generator(salt, False)
    while my_gen1.passwords_found != 64:
        my_gen1.advance()
    print("64th password is {}.".format(my_gen1.counter))

    my_gen2 = generator(salt, True)
    while my_gen2.passwords_found != 64:
        my_gen2.advance()
    print("64th password is {}.".format(my_gen2.counter))
    timer.end_hit()
