from random import randrange


def length(vec):
	return (vec[0]**2 + vec[1]**2) ** .5


def normalise(vec):
	l = length(vec)
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
	def __init__(self):
		self.genes = Gene()
		self.position = self.genes.get_movement()
		self.score = 0

	def evaluate(self, aim):
		if self.position == aim:
			return 10000
		distance = Individuum.distance(self.position, aim)
		self.score = float(10000) / distance

	def mate(self, other):
		child = Individuum()
		child.genes = self.genes + other.genes
		return child

	@staticmethod
	def distance(pos1, pos2):
		diff = (pos1[0] - pos2[0], pos1[1] - pos2[1])
		return length(diff)

	def __repr__(self):
		return "%i with Genes: %s" % (self.score, self.genes)


class Gene:
	def __init__(self):
		self.length = randrange(0, 200)
		self.direction = Gene.random_pos()

	def get_movement(self):
		return (self.direction[0]*self.length, self.direction[1]*self.length)

	def __add__(self, other):
		new_genes = Gene()
		new_genes.length = float(self.length + other.length) / 2
		new_genes.direction = Gene.combine(self.direction, other.direction)
		return new_genes

	@staticmethod
	def combine(dir1, dir2):
		x = float(dir1[0] + dir2[0]) / 2
		y = float(dir1[1] + dir2[1]) / 2
		return normalise((x, y))

	def __repr__(self):
		return "L:%f (%f|%f)" % (self.length, self.direction[0], self.direction[1])

	@staticmethod
	def random_pos():
		vec = (randrange(-5, 5), randrange(-5, 5))
		l = length(vec)
		while l == 0:
			vec = (randrange(-5, 5), randrange(-5, 5))
			l = length(vec)
		normalise(vec)
		return vec
