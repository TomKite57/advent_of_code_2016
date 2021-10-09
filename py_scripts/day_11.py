from aoc_tools import Advent_Timer

#def readfile(fname):
#    with open(fname, 'r') as file:
#        return [line.strip() for line in file]

class maze_search:
	def __init__(self, initial_state):
		self.history = dict()
		self.open_paths = [state(),]
		self.open_paths[0].initial_state(initial_state)
		self.current_best = float("inf")

	def valid_state(self, p):
		if not p.valid():
			return False
		if p.G >= self.current_best:
			return False
		if self.history.get(p.get_hash(), float("inf")) <= p.G:
			return False
		return True

	def do_move(self, p, objs, s):
		new_p = state()
		new_p.copy_state(p)
		new_p.move(p.E, objs, s)
		if self.valid_state(new_p):
			self.smart_append(0, len(self.open_paths)-1, new_p)
			self.history[new_p.get_hash()] = new_p.G
			if new_p.goal():
				self.current_best = new_p.G

	def smart_append(self, i, j, p):
		if len(self.open_paths) == 0:
			self.open_paths.append(p)
			return
		if self.open_paths[i].G <= p.G:
			self.open_paths.insert(i, p)
			return
		if self.open_paths[j].G >= p.G:
			self.open_paths.insert(j+1, p)
			return
		if abs(i - j) <= 1:
			self.open_paths.insert(j, p)
			return
		midpoint = (i+j)//2
		if self.open_paths[midpoint].G == p.G:
			self.open_paths.insert(midpoint, p)
			return
		if self.open_paths[midpoint].G <= p.G:
			self.smart_append(i, midpoint, p)
			return
		if self.open_paths[midpoint].G > p.G:
			self.smart_append(midpoint, j, p)
			return

	def take_step(self):
		p = self.open_paths.pop()
		if p.G >= self.current_best:
			return
		floor = list(p.floors[p.E])

		if p.E == 0:
			steps = [+1,]
		elif p.E == 1:
			steps = [-1, +1]
		elif p.E == 2:
			steps = [-1, +1]
		elif p.E == 3:
			steps = [-1,]

		for i, obji in enumerate(floor):
			for s in steps:
				self.do_move(p, [obji], s)
			for j, objj in enumerate(floor[i+1:]):
				for s in steps:
					self.do_move(p, [obji, objj], s)

	def full_advance(self):
		while len(self.open_paths):
			self.take_step()

class state:
	def __init__(self):
		self.G = 0
		self.E = 0
		self.floors = [set(), set(), set(), set()]
		self.tot_num = 0

	def initial_state(self, floors):
		for i, f in enumerate(floors):
			self.floors[i] = f
		self.tot_num = sum([len(f) for f in self.floors])

	def goal(self):
		return len(self.floors[3]) == self.tot_num

	def copy_state(self, other):
		self.G = other.G
		self.E = other.E
		self.tot_num = other.tot_num
		self.floors = [set(f) for f in other.floors]


	def move(self, f_num, objs, direc):
		for obj in objs:
			self.floors[f_num].remove(obj)
			self.floors[f_num+direc].add(obj)
		self.E += direc
		self.G += 1

	def get_hash(self):
		hash = []
		for F in self.floors:
			contents = {'M': set(), 'G': set()}
			g_surplus = 0
			m_surplus = 0
			pairs = 0
			for f in F:
				contents[f[1]].add(f[0])
			for m in contents['M']:
				if m not in contents['G']:
					m_surplus += 1
				else:
					pairs += 1
			for g in contents['G']:
				if g not in contents['M']:
					g_surplus += 1
			hash.append([-1,]*g_surplus + [0,]*pairs + [1,]*m_surplus)
		return (self.E, *[tuple(x) for x in hash])


	def valid(self):
		for F in self.floors:
			if len(F) == 0:
				continue
			contents = {'M': set(), 'G': set()}
			for f in F:
				contents[f[1]].add(f[0])
			if len(contents['G']) == 0:
				continue
			for m in contents['M']:
				if m not in contents['G']:
					return False
		return True

	def show(self):
		all_things = []
		for F in self.floors:
			all_things += list(F)
		all_things = sorted(all_things)

		for i in range(len(self.floors)-1, -1, -1):
			tmp = "F" + str(i+1) + ": "
			if i == self.E:
				tmp += "E "
			else:
				tmp += "  "
			for thing in all_things:
				if thing in self.floors[i]:
					tmp += thing + " "
				else:
					tmp += ".  "
			if i==3:
				tmp += " G=" + str(self.G)
			print(tmp)
		print()


if __name__ == "__main__":
	timer = Advent_Timer()
	#data = readfile("data/day_11.dat")

	data = [set(['SG', 'SM', 'PG', 'PM']), set(['TG', 'RG', 'RM', 'CG', 'CM']), set(['TM']), set()]
	maze1 = maze_search(data)
	maze1.full_advance()
	print("Minimum steps: {}".format(maze1.current_best))

	data = [set(['SG', 'SM', 'PG', 'PM'] + ['EG', 'EM', 'DG', 'DM']), set(['TG', 'RG', 'RM', 'CG', 'CM']), set(['TM']), set()]
	maze2 = maze_search(data)
	maze2.full_advance()
	print("Minimum steps: {}".format(maze2.current_best))

	timer.end_hit()
