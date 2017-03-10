from classes import *

aim = (20, 300)
start = (250, 250)

population = Population(1000)
population.evolve(aim)

print(population.get_avg_score())



# Drawing the population
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
frame_count = 0
while frame_count < 5000:
	screen.fill((255,255,255))
	for indi in population.pop:
		genes = indi.genes
		position = genes.get_movement()
		rel = (start[0]+position[0], start[1]+position[1])
		pygame.draw.circle(screen, (255,0,0), rel, 2)
	pygame.draw.circle(screen, (0,0,255), start , 3)
	pygame.draw.circle(screen, (0,255,0), aim , 3)
	pygame.display.update()
	frame_count += 1