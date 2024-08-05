import pygame
from random import randint
from maze import *
from player import *


RES = WIDTH, HEIGHT = 1202,902

WHITE = (255,255,255)
BLACK = (0,0,0)
DARKRED =(207, 0, 0)


pygame.init()
screen = pygame.display.set_mode(RES)
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

gridCells = generateMaze()

class Reward():
    def __init__(self,x:int,y:int) -> None:
        self.x = x
        self.y = y
        self.worth = 1
        self.distanceFromEnd = None

    def draw(self) -> None:
        pygame.draw.rect(screen,DARKRED,(self.x,self.y,TILESIZE/3,TILESIZE/3))
    
    def getRect(self) -> pygame.Rect:
        return pygame.Rect((self.x,self.y),(TILESIZE/3,TILESIZE/3))

    def placeOnMap(self) -> None:
        for x in columns:
            for y in rows:
                if not self.detectCollision():
                    #do placing
                    pass

    def detectCollision() -> None:
        pass

    def calculateValue(self) -> None:
        pass

singleMovement = True
player = Player(5,5)
playerRect = player.getRect()

cellRects = [cell.getRects() for layer in gridCells for cell in layer]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if singleMovement and event.type == pygame.KEYDOWN:
            player.singleMovement(event.key)

    screen.fill("black")
    [cell.draw(screen) for layer in gridCells for cell in layer]
    [player.draw(screen)]


    if not singleMovement:
        keysPressed = pygame.key.get_pressed()
        player.multiMovement(keysPressed)
    player.detectCollision(cellRects)




    pygame.display.flip()
    clock.tick(60)

pygame.quit()