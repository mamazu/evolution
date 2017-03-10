from random import randrange

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

	def repopulate(self):
		from random import choice
		to_get = self.size - len(self.pop)
		for _ in range(to_get):
			m1 = choice(self.pop)
			m2 = choice(self.pop)
			child = m1.mate(m2)
			self.pop.append(child)

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
		self.score = 10000 / distance

	def mate(self, other):
		child = Individuum()
		child.genes = self.genes + other.genes
		return child

	@staticmethod
	def distance(pos1, pos2):
		xdif = pos1[0]-pos2[0]
		ydif = pos1[1]-pos2[1]
		return (xdif **2 + ydif**2)**(.5)

	def __repr__(self):
		return str(self.score)

class Gene:
	def __init__(self):
		self.length = randrange(0, 200)
		self.direction = Gene.random_pos()

	def get_movement(self):
		return (self.direction[0]*self.length,self.direction[1]*self.length)

	def __add__(self, other):
		new_genes = Gene()
		new_genes.length = (self.length + other.length) / 2
		new_genes.direction = Gene.combine(self.direction, other.direction)
		return new_genes

	@staticmethod
	def combine(dir1, dir2):
		x = (dir1[0] + dir2[0]) / 2
		y = (dir1[1] + dir2[1]) / 2
		return (x, y)

	@staticmethod
	def random_pos():
		return (randrange(-5, 5), randrange(-5, 5))
