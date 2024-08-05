import pygame
from maze import WHITE,TILESIZE

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

    def draw(self,screen) -> None:
        rect = pygame.draw.rect(screen,WHITE,(self.x,self.y,TILESIZE/2,TILESIZE/2))
        return rect

    def getRect(self) -> None:
        return pygame.Rect((self.x,self.y),(TILESIZE/2,TILESIZE/2))

    def getState(self) -> list:
        return [self.x,self.y,self.score,self.mazesCompleted]

    def multiMovement(self,keysPressed) -> None:

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

    def singleMovement(self,keyPressed) -> None:
        self.velocity = 15
        if keyPressed == pygame.K_UP and not self.disabledDirection["UP"]:
            self.y -= self.velocity
            self.lastDirection = "UP"
        if keyPressed == pygame.K_DOWN and not self.disabledDirection["DOWN"]:
            self.y += self.velocity
            self.lastDirection = "DOWN"
        if keyPressed == pygame.K_RIGHT and not self.disabledDirection["RIGHT"]:
            self.x += self.velocity
            self.lastDirection = "RIGHT"
        if keyPressed == pygame.K_LEFT and not self.disabledDirection["LEFT"]:
            self.x -= self.velocity
            self.lastDirection = "LEFT"

    def detectCollision(self,collisionRects) -> None:
        for layer in collisionRects:
            for rect in layer:
                if self.getRect().colliderect(rect):
                    
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
                    else:
                        self.resetDirections()                
    def resetDirections(self):
        self.disabledDirection["UP"] = False
        self.disabledDirection["DOWN"] = False
        self.disabledDirection["RIGHT"] = False
        self.disabledDirection["LEFT"] = False