import pygame
from maze import *
from player import *
from time import sleep


RES = WIDTH, HEIGHT = 1202,902

WHITE = (255,255,255)
BLACK = (0,0,0)
DARKRED =(207, 0, 0)


pygame.init()
screen = pygame.display.set_mode(RES)
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

singleMovement = False
player = Player(5,5)

gridCells = generateMaze()
cellRects = [cell.getRects() for layer in gridCells for cell in layer]
finishRect = pygame.Rect((gridCells[-1][-1].x*TILESIZE,gridCells[-1][-1].y*TILESIZE),(TILESIZE,TILESIZE))
initialPostion = pygame.Vector2(5,5)


def distanceToEnd(playerRect:pygame.Rect,finishRect:pygame.Rect,lastPostion:pygame.Vector2) -> list[bool,pygame.Vector2]:
    newDistanceX = finishRect.x - playerRect.x
    newDistanceY = finishRect.y - playerRect.y
    newDistance = pygame.Vector2(abs(newDistanceX),abs(newDistanceY))

    if newDistance.x > lastPostion.x or newDistance.y > lastPostion.y:
        return [True,newDistance]
    else:
        return [False,newDistance]

def handleScore(player:Player,result:bool) -> None:
    if result:
            player.score +=0.02
            player.score = round(player.score,2)

def endCurrent(player:Player,finishRect:pygame.Rect) -> None: # Works
    if player.getRect().colliderect(finishRect):
        player.score += 10.0

def refreshMaze() -> None:
    pass
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if singleMovement and event.type == pygame.KEYDOWN:
            player.singleMovement(event.key)

    [cell.draw(screen) for layer in gridCells for cell in layer]
    [player.draw(screen)]

    if not singleMovement:
        keysPressed = pygame.key.get_pressed()
        player.multiMovement(keysPressed)
    player.detectCollision(cellRects)

    result = distanceToEnd(player.getRect(),finishRect,initialPostion)
    initialPostion = result[1]
    handleScore(player,result[0])
    endCurrent(player,finishRect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()