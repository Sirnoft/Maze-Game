import pygame
from random import choice

RES = WIDTH, HEIGHT = 1202,902
TILESIZE = 100

columns, rows = int(WIDTH/TILESIZE),int(HEIGHT/TILESIZE)

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()


class Cell():
    def __init__(self,X,Y) -> None:
        self.x = X
        self.y = Y
        self.walls = {
            "TOP" : True,
            "BOTTOM" : True,
            "RIGHT" : True,
            "LEFT" : True}
        
        self.visited = False

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

    def check_cell(self,x,y):
        find_index = lambda x,y: x+(y*columns)

        if x < 0 or x > columns - 1 or y < 0 or y > rows - 1:
            return False
        return gridCells[find_index(x,y)]
    
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

gridCells = [Cell(col,row) for col in range(columns) for row in range(rows)]
currentCell = gridCells[0]
stack = []



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill("black")

    [cell.draw() for cell in gridCells]
    currentCell.visited = True
    currentCell.draw_current()

    next_cell = currentCell.check_neighbours()

    if next_cell:
        next_cell.visited = True
        stack.append(currentCell)
        removeWalls(currentCell,next_cell)
        currentCell = next_cell
    elif stack:
        currentCell = stack.pop()

  
    pygame.display.flip()
    clock.tick(60)

pygame.quit()