import pygame
from maze import *
from enum import Enum

RES = WIDTH, HEIGHT = 1202,902

WHITE = (255,255,255)
BLACK = (0,0,0)
DARKRED =(207, 0, 0)
class DIRECTION(Enum):
    North = 1
    South = 2
    Right = 3
    Left  =  4

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

gridCells = generateMaze()

class Player():
    def __init__(self,x:int,y:int) -> None:
        self.x = x
        self.y = y
        self.lastDirection = ""
        self.score = 0
        self.velocity = 5
        self.mazesCompleted = 0

        self.disabledDirection = {
            "UP" : False,
            "DOWN" : False,
            "RIGHT" : False,
            "LEFT" : False,
        }

    def draw(self) -> None:
        rect = pygame.draw.rect(screen,WHITE,(self.x,self.y,TILESIZE/2,TILESIZE/2))
        return rect

    def getRect(self) -> None:
        return pygame.Rect((self.x,self.y),(TILESIZE/2,TILESIZE/2))

    def getState(self) -> list:
        return [self.x,self.y,self.score,self.mazesCompleted]


    def movement(self,keysPressed) -> None:

        if keysPressed[pygame.K_UP] and not self.disabledDirection["UP"]:
            self.y -= self.velocity
            self.lastDirection = "UP"
        if keysPressed[pygame.K_DOWN] and not self.disabledDirection["DOWN"]:
            self.y += self.velocity
            self.lastDirection = "DOWN"
        if keysPressed[pygame.K_RIGHT] and not self.disabledDirection["RIGHT"]:
            self.x += self.velocity
            self.lastDirection = "RIGHT"
        if keysPressed[pygame.K_LEFT] and not self.disabledDirection["LEFT"]:
            self.x -= self.velocity
            self.lastDirection = "LEFT"

    def detectCollision(self,collisionRects) -> bool:
        for layer in collisionRects:
            for rect in layer:
                if playerRect.colliderect(rect):
                    
                    if self.lastDirection == "RIGHT":
                        self.x = rect.left - TILESIZE/2
                        self.disabledDirection["RIGHT"] = True

                    if self.lastDirection == "LEFT":
                        self.x = rect.right
                        self.disabledDirection["LEFT"] = True

                    if self.lastDirection == "DOWN":
                        self.y = rect.top - TILESIZE/2
                        self.disabledDirection["DOWN"] = True

                    if self.lastDirection == "UP":
                        self.y = rect.bottom
                        self.disabledDirection["UP"] = True
                        
    def resetDirections(self):
        self.disabledDirection["UP"] = False
        self.disabledDirection["DOWN"] = False
        self.disabledDirection["RIGHT"] = False
        self.disabledDirection["LEFT"] = False

player = Player(5,5)

cellRects = [cell.getRects() for layer in gridCells for cell in layer]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
    screen.fill("black")

    keysPressed = pygame.key.get_pressed()
    player.movement(keysPressed)

    [cell.draw(screen) for layer in gridCells for cell in layer]
    [player.draw()]

    playerRect = player.getRect()

    player.detectCollision(cellRects)



    pygame.display.flip()
    clock.tick(60)

pygame.quit()