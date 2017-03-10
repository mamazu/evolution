from random import randrange

class Population:
	def __init__(self, size=100):
		self.pop = [Individuum() for _ in range(size)]

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
