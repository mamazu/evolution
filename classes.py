from random import randrange


def dist(vec):
	return (vec[0]**2 + vec[1]**2) ** .5

def pretty(vec):
	return "(%.3f|%.3f)" % (vec[0], vec[1])

def normalise(vec):
	l = dist(vec)
	if l == 0:
		return vec
	vec = float(vec[0]) / l, float(vec[1]) / l
	return vec


class Population:
	def __init__(self, size=100):
		self.generation = 0
		self.size = int(size)
		self.pop = [Individuum() for _ in range(self.size)]

	def evaluate(self, aim):
		from operator import attrgetter
		for indi in self.pop:
			indi.evaluate(aim)
		self.pop.sort(key=attrgetter('score'))

	def kill(self, rate=.3):
		if rate < 0:
			return
		killer = int(self.size * rate)
		self.pop = self.pop[killer:]

	def prints(self):
		for i in range(4):
			print(self.pop[-(i+1)])

	def select(self):
		l = (len(self.pop)**2+len(self.pop))/2
		winner = randrange(l) + 1

		for i, indi in enumerate(self.pop):
			balls = self.size - i
			if winner <= balls:
				return self.pop[-(i+1)]
			winner -= balls

	def repopulate(self):
		from random import choice
		to_get = self.size - len(self.pop)
		for _ in range(to_get):
			m1 = self.select()
			m2 = self.select()
			# m1 = choice(self.pop)
			# m2 = choice(self.pop)
			child = m1.mate(m2)
			self.pop.append(child)
		self.generation += 1

	def get_avg_score(self):
		return sum([indi.score for indi in self.pop]) / self.size


class Individuum:
	ID = 0

	def __init__(self):
		self.id = str(Individuum.ID).zfill(6)
		Individuum.ID += 1
		self.genes = Gene()
		self.position = self.genes.get_movement()
		self.score = 0

	def evaluate(self, aim):
		# if self.genes.get_movement() != self.position:
		# 	self.position = self.genes.get_movement()
		diff = (self.position[0]-aim[0], self.position[1]-aim[1])
		l = dist(diff)
		if l == 0:
			self.score = 10000
			return
		self.score = float(10000) / l

	def mate(self, other):
		child = Individuum()
		child.genes = self.genes + other.genes
		return child

	def __repr__(self):
		return "Id: %s, Score: %.3f, Genes: [%s], Position: %s" % (self.id, self.score, self.genes, pretty(self.position))


class Gene:
	def __init__(self, length=None, direction=None):
		if length is None and direction is None:
			self.length = randrange(0, 200)
			self.direction = normalise(Gene.random_pos())
		else:
			self.length = length
			self.direction = normalise(direction)

	def get_movement(self):
		return (self.direction[0]*self.length, self.direction[1]*self.length)

	def __add__(self, other):
		length = float(self.length + other.length) / 2
		direction = Gene.combine(self.direction, other.direction)
		return Gene(length, direction)

	@staticmethod
	def combine(dir1, dir2):
		x = float(dir1[0] + dir2[0]) / 2
		y = float(dir1[1] + dir2[1]) / 2
		return (x, y)

	def __repr__(self):
		return "Length: %.3f Direction: %s" % (self.length, pretty(self.direction))

	@staticmethod
	def random_pos():
		vec = (randrange(-5, 5), randrange(-5, 5))
		l = dist(vec)
		while l == 0:
			vec = (randrange(-5, 5), randrange(-5, 5))
			l = dist(vec)
		return vec
