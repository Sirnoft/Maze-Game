from typing import Any
import pygame
from random import choice


RES = WIDTH, HEIGHT = 1202,902
TILESIZE = 100

WHITE = (255,255,255)
BLACK = (0,0,0)
DARKRED =(207, 0, 0)

columns, rows = int(WIDTH/TILESIZE),int(HEIGHT/TILESIZE)

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

class Cell():
    def __init__(self,x:int,y:int) -> None:
        self.x = x
        self.y = y

        self.walls = {
            "TOP" : True,
            "BOTTOM" : True,
            "RIGHT" : True,
            "LEFT" : True
        }
        self.visited = False
        

    def draw(self) -> None:
        x,y = self.x * TILESIZE, self.y * TILESIZE
        if self.visited:
            pygame.draw.rect(screen,DARKRED,(x,y,TILESIZE,TILESIZE))

        if self.walls["TOP"]:
            pygame.draw.line(screen,WHITE,(x,y),(x+TILESIZE,y),2)
        if self.walls["BOTTOM"]:
            pygame.draw.line(screen,WHITE,(x+TILESIZE,y+TILESIZE),(x+TILESIZE,y+TILESIZE),2)
        if self.walls["RIGHT"]:
            pygame.draw.line(screen,WHITE,(x+TILESIZE,y),(x+TILESIZE,y+TILESIZE),2)
        if self.walls["LEFT"]:
            pygame.draw.line(screen,WHITE,(x,y+TILESIZE),(x,y),2)

    def checkCell(self,direction:str) -> bool:
        x, y = self.x, self.y
        direction = direction.upper()

        position = gridCells[x][y]

        try:
            if direction == "TOP" and y - 1 != -1:
                return gridCells[x][y-1]
            if direction == "BOTTOM":
                return gridCells[x][y+1]
            if direction == "RIGHT" and x - 1 > -1:
                return gridCells[x-1][y]
            if direction == "LEFT":
                return gridCells[x+1][y]
        except:
            return False
        return False
    
    def checkNeighbours(self) -> list:
        neighbours = []

        top = self.checkCell("TOP")
        bottom = self.checkCell("BOTTOM")
        right = self.checkCell("RIGHT")
        left = self.checkCell("LEFT")

        if top != False and not top.visited:
            neighbours.append(top)
        if bottom != False and not bottom.visited:
            neighbours.append(bottom)
        if right != False and not right.visited:
            neighbours.append(right)
        if left != False and not left.visited:
            neighbours.append(left)

        return neighbours

"""class Cell():
    def draw_current(self):
        x,y = self.x * TILESIZE, self.y * TILESIZE
        pygame.draw.rect(screen,pygame.Color('white'),(x+2,y+2,TILESIZE,TILESIZE))

    def draw(self) -> None:
        x,y = self.x * TILESIZE, self.y * TILESIZE
        if self.visited == True:
            pygame.draw.rect(screen,pygame.Color('black'),(x,y,TILESIZE,TILESIZE))

        if self.walls["TOP"]:
            pygame.draw.line(screen,pygame.Color('red'),(x,y),(x+TILESIZE,y),2)
        if self.walls["BOTTOM"]:
            pygame.draw.line(screen,pygame.Color('red'),(x + TILESIZE,y+TILESIZE),(x+TILESIZE,y+TILESIZE),2)
        if self.walls["RIGHT"]:
            pygame.draw.line(screen,pygame.Color('red'),(x + TILESIZE,y),(x+TILESIZE,y+TILESIZE),2)
        if self.walls["LEFT"]:
            pygame.draw.line(screen,pygame.Color('red'),(x,y+TILESIZE),(x,y),2)

    def check_neighbours(self):
        neighbours = []
        top = self.check_cell(self.x,self.y-1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x,self.y+1)
        left = self.check_cell(self.x -1,self.y)

        if top and not top.visited:
            neighbours.append(top)
        if right and not right.visited:
            neighbours.append(right)
        if bottom and not bottom.visited:
            neighbours.append(bottom)
        if left and not left.visited:
            neighbours.append(left)

        return choice(neighbours) if neighbours else False

def removeWalls(current,next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['LEFT'] = False
        next.walls['RIGHT'] = False
    elif dx == -1:
        current.walls['RIGHT'] = False
        next.walls['LEFT'] = False

    dy = current.y - next.y
    if dy == 1:
            current.walls['TOP'] = False
            next.walls['BOTTOM'] = False
    elif dy == -1:
        current.walls['BOTTOM'] = False
        next.walls['TOP'] = False
"""
gridCells = []
temp = []
for col in range(columns):
    for row in range(rows):
        temp.append(Cell(col,row))
    gridCells.append(temp)
    temp = []

stack = [choice(choice(gridCells))]

currentCell = stack[0]
neighbours = currentCell.checkNeighbours()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill("black")

    [cell.draw() for layer in gridCells for cell in layer]
    currentCell.visited = True

    for cell in neighbours:
        cell.visited = True

    pygame.display.flip()
    clock.tick(200)

pygame.quit()