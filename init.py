from classes import *

aim = (20, 40)
start = (250, 250)

population = Population(1000)
while population.generation < 10:
	population.evaluate(aim)
	population.kill(.2)
	# population.prints()
	population.repopulate()
print(population.get_avg_score())


# Drawing the population
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			key = event.key
			if key == pygame.K_ESCAPE:
				running = False

	screen.fill((255, 255, 255))
	for indi in population.pop:
		genes = indi.genes
		position = genes.get_movement()
		rel = (int(start[0]+position[0]), int(start[1]+position[1]))
		pygame.draw.circle(screen, (255, 0, 0), rel, 2)
	# Drawing start and end
	pygame.draw.circle(screen, (0, 0, 255), start, 3)
	rel_aim = (int(start[0]+aim[0]), int(start[1]+aim[1]))
	pygame.draw.circle(screen, (0, 255, 0), rel_aim, 3)
	pygame.display.update()
