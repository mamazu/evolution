from random import randrange

class Population:
	def __init__(self, size=100):
		self.generation = 0
		self.size = int(size)
		self.pop = [Individuum() for _ in range(self.size)]

	def evolve(self, aim):
		for indi in self.pop:
			indi.evaluate(aim)

	def get_avg_score(self):
		return sum([indi.score for indi in self.pop])//self.size

class Individuum:
	def __init__(self):
		self.genes = Gene()

class Gene:
	def __init__(self):
		self.length = randrange(0, 10)
		self.direction = Gene.random_pos()

	def get_movement(self):
		return (self.direction[0]*self.length,self.direction[1]*self.length)

	@staticmethod
	def random_pos():
		return (randrange(-5, 5), randrange(-5, 5))
