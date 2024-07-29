import pygame
from maze import *

RES = WIDTH, HEIGHT = 1202,902

WHITE = (255,255,255)
BLACK = (0,0,0)
DARKRED =(207, 0, 0)

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

gridCells = generateMaze()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill("black")

    [cell.draw(screen) for layer in gridCells for cell in layer]


    pygame.display.flip()
    clock.tick(60)

pygame.quit()