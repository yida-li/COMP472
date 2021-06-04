import time
import pygame
import random
import math
from queue import PriorityQueue
pygame.display.set_caption("A* Path Finding Algorithm")

# Images stolen from ZIXIQUIAN
IMG = pygame.image.load(r'perfectPlayerground.png')
IMG_VAC = pygame.image.load(r'perfectVaccine.png')
IMG_VIR = pygame.image.load(r'perfectVirus.png')
ROLEC = pygame.image.load(r'roleC.png')
ROLEV = pygame.image.load(r'roleV.png')
ROLEP = pygame.image.load(r'roleP.png')

# Not used colors
RED = (255, 0, 0)
# Q
GREEN = (0, 255, 0)
QUARANTINE = (0, 255, 0)

# V
ORANGE = (255, 165, 0)
VACCINE = (255, 255, 0)


# P
PURPLE = (128, 0, 128)

BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
PURPLE2 = PURPLE
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Spot:
    def __init__(self, row, col, width, length, total_rows, total_columns):
        self.row = row
        self.col = col
        self.y = row * width
        self.x = col * length
        # self.shape=self.register_shape('player.png')
        # default contructor sets color to white
        self.color = WHITE
        self.neighbors = []
        self.heuristic = 0
        self.width = width
        self.length = length
        self.total_rows = total_rows
        self.total_columns = total_columns
        self.status = 'vacant'
        self.access = True  # if spot can be traversed
        self.cost = 0
        self.role = 'noRole'

    def changeRole(self, role):
        if(role == 'roleC'):
            self.role = 'roleC'
        if(role == 'roleV'):
            self.role = 'roleV'
        if(role == 'roleP'):
            self.role = 'roleP'

    def make_quarantine(self):
        self.status = 'quarantine'
        self.color = GREEN

    def make_vaccine(self):
        self.status = 'vaccine'
        self.color = VACCINE

    def make_playground(self):
        self.status = 'playground'
        self.color = BLUE

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_contaminated(self):
        return self.color == GREEN

    def is_start(self):
        return self.color == ORANGE

    def is_accessible(self):

        return self.access

    def is_end(self):

        return self.color == TURQUOISE

    def is_vaccine(self):
        return self.color == VACCINE

    def is_vacant(self):
        return self.color == WHITE

    def reset(self):
        self.color = WHITE
        self.status = 'vacant'
        self.role = 'noRole'

    def make_start(self):
        self.status = 'starting Point'
        self.role = 'roleC'
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_end(self):
        self.status = 'turq'
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        if self.color == ORANGE:

            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))
        else:
            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))

    def drawImage(self, win):

        if (self.status == 'playground'):
            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))
            win.blit(IMG, (self.x, self.y))

        elif (self.status == 'vaccine'):
            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))
            win.blit(IMG_VAC, (self.x, self.y))
        elif (self.status == 'quarantine'):
            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))
            win.blit(IMG_VIR, (self.x, self.y))
        elif (self.color == ORANGE):
            if(self.role == 'roleP'):
                pygame.draw.rect(
                    win, self.color, (self.x, self.y, self.length, self.width))
                win.blit(ROLEP, (self.x+25, self.y+50))
            elif(self.role == 'roleV'):
                pygame.draw.rect(
                    win, self.color, (self.x, self.y, self.length, self.width))
                win.blit(ROLEV, (self.x+25, self.y+50))
            else:
                pygame.draw.rect(
                    win, self.color, (self.x, self.y, self.length, self.width))
                win.blit(ROLEC, (self.x+25, self.y+50))
        elif (self.color == RED):
            if(self.role == 'roleP'):
                pygame.draw.rect(
                    win, self.color, (self.x, self.y, self.length, self.width))
                win.blit(ROLEP, (self.x+25, self.y+50))
            elif(self.role == 'roleV'):
                pygame.draw.rect(
                    win, self.color, (self.x, self.y, self.length, self.width))
                win.blit(ROLEV, (self.x+25, self.y+50))
            else:
                pygame.draw.rect(
                    win, self.color, (self.x, self.y, self.length, self.width))
                win.blit(ROLEC, (self.x+25, self.y+50))
        else:
            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))

    # under the scenario that i need to potentially use this which is coincedently implaussible
    def update_neighbors_asGhostChild(self, grid):
        self.neighbors = []

        # DOWN
        if self.row < self.total_rows - 1 and self.is_accessible() and not grid[self.row + 1][self.col].is_contaminated():
            self.neighbors.append(grid[self.row + 1][self.col])

        # UP
        if self.row > 0 and self.is_accessible() and not grid[self.row - 1][self.col].is_contaminated():
            self.neighbors.append(grid[self.row - 1][self.col])

        # RIGHT
        if self.col < self.total_columns - 1 and self.is_accessible() and not grid[self.row][self.col+1].is_contaminated():
            self.neighbors.append(grid[self.row][self.col + 1])

        # LEFT
        if self.col > 0 and self.is_accessible() and not grid[self.row][self.col-1].is_contaminated():
            self.neighbors.append(grid[self.row][self.col - 1])

    def update_neighbors(self, grid):
        self.neighbors = []

        # DOWN
        if self.row < self.total_rows - 1 and self.is_accessible():
            self.neighbors.append(grid[self.row + 1][self.col])

        # UP
        if self.row > 0 and self.is_accessible():
            self.neighbors.append(grid[self.row - 1][self.col])

        # RIGHT
        if self.col < self.total_columns - 1 and self.is_accessible():
            self.neighbors.append(grid[self.row][self.col + 1])

        # LEFT
        if self.col > 0 and self.is_accessible():
            self.neighbors.append(grid[self.row][self.col - 1])


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def construct_Nodes(rows, columns, width, length):
    grid = []
    gap = width // rows
    lgap = length//columns
    for i in range(rows):
        grid.append([])
        for j in range(columns):

            spot = Spot(i, j, gap, lgap, rows, columns)
            # print(spot.col, spot.row,  gap, lgap, width, length)
            grid[i].append(spot)

    return grid


def draw_map(win, rows, width, columns, length):

    gap = width // rows
    lgap = length // columns
    for i in range(rows + 1):
        pygame.draw.line(win, GREY, (0, i * gap), (length, i * gap), 4)
        for j in range(columns + 1):
            pygame.draw.line(win, GREY, (j * lgap, 0), (j * lgap, width), 4)


def draw_grid(win, rows, width, columns, length):
    gap = width // rows
    lgap = length // columns
    for i in range(rows + 1):
        pygame.draw.line(win, PURPLE, (0, i * gap), (length, i * gap), 4)
        for j in range(columns + 1):
            pygame.draw.line(win, YELLOW, (j * lgap, 0), (j * lgap, width), 4)
            if i != rows and j != columns:
                pygame.draw.rect(win, GREY, [j * lgap, i * gap, 10, 10])
            elif i == rows:
                pygame.draw.rect(win, GREY, [j * lgap, i * gap - 10, 10, 10])
            elif j == columns:
                pygame.draw.rect(win, GREY, [j * lgap - 10, i * gap, 10, 10])

    pygame.draw.rect(win, GREY, [length - 10, width - 10, 10, 10])


def draw(win, grid, rows, width, columns, length):

    for row in grid:
        for spot in row:
            spot.drawImage(win)                       # draws their own color

    draw_grid(win, rows, width, columns, length)  # darws the lines
    pygame.display.update()


def heuristicUpdate(grid, playerType, startPoint):
    if playerType == 'roleP':
        for row in grid:

            for spot in row:

                if spot.status == 'playground':
                    spot.heuristic = h(startPoint.get_pos(), spot.get_pos())
                    spot.cost = 0
                if spot.status == 'vacant':
                    spot.cost = 1
                if spot.status == 'quarantine':
                    spot.cost = 1000
                if spot.status == 'vaccine':
                    spot.cost = 2

    if playerType == 'roleV':
        for row in grid:

            for spot in row:
                if spot.status == 'vaccine':
                    spot.heuristic = h(startPoint.get_pos(), spot.get_pos())
                    spot.cost = 0
                if spot.status == 'playground':
                    spot.cost = 1
                if spot.status == 'vacant':
                    spot.cost = 2
                if spot.status == 'quarantine':
                    spot.cost = 3
    if playerType == 'roleC':
        for row in grid:

            for spot in row:

                if spot.status == 'vaccine':
                    spot.cost = 2
                if spot.status == 'playground':
                    spot.cost = 3
                if spot.status == 'vacant':
                    spot.cost = 1
                if spot.status == 'quarantine':
                    spot.heuristic = h(startPoint.get_pos(), spot.get_pos())
                    spot.cost = 0


def get_clicked_pos(pos, rows, width, columns, length):
    gap = width // rows
    lgap = length // columns

    x, y = pos
    # print("X position is : ", x, " Y position is :", y)
    row = y // gap
    col = x // lgap

    # print("ROW is : ", row, " Column is :", col)
    return row, col


def reconstruct_path(came_from, destination, start):

    while destination in came_from:
        destination = came_from[destination]
        destination.make_path()


def algorithm(grid, start, Destination):

    priority_list = {}

    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_scoreDictionary = {spot: float("inf") for row in grid for spot in row}
    g_scoreDictionary[start] = 0
    f_scoreDictionary = {spot: float("inf") for row in grid for spot in row}
    f_scoreDictionary[start] = h(
        start.get_pos(), Destination.get_pos())
    open_set_hash = {start}
    while not open_set.empty():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # fetching just the node , so at first the currentNode is the starting point
        currentNODE = open_set.get()[2]
        open_set_hash.remove(currentNODE)

        if currentNODE == Destination:
            reconstruct_path(came_from, Destination, start)
            start.color = ORANGE
            return True

        for INDEXNEIGHBOR in currentNODE.neighbors:
            tempSCORETRACKER = g_scoreDictionary[currentNODE] + 1

            if tempSCORETRACKER < g_scoreDictionary[INDEXNEIGHBOR]:
                # came_from[i]= currentNode  wtv node we're on right now
                came_from[INDEXNEIGHBOR] = currentNODE
                # g_scoreD[i]=
                g_scoreDictionary[INDEXNEIGHBOR] = tempSCORETRACKER
                f_scoreDictionary[INDEXNEIGHBOR] = tempSCORETRACKER + \
                    h(INDEXNEIGHBOR.get_pos(), Destination.get_pos())     # heuristic

                if INDEXNEIGHBOR not in open_set_hash:  # look inside queue and add a count
                    count += 1
                    open_set.put(
                        (f_scoreDictionary[INDEXNEIGHBOR], count, INDEXNEIGHBOR))  # put in f score, the incremented count , spot object
                    open_set_hash.add(INDEXNEIGHBOR)

    return False


def fetchRobotPlayground(grid):
    for row in grid:
        for spot in row:
            if spot.status == 'playground':
                return spot


def fetchRobotQuarantine(grid):
    for row in grid:
        for spot in row:
            if spot.status == 'quarantine':
                return spot


def main():
    playerType = 'roleC'
    pygame.init()
    print("PLEASE SET UP THE MAP PERIMETER")
    print("recommended size : 10 rows, 5 columns")
    ROWS = int(input("Enter the total rows you would like "))
    COLUMNS = int(input("Enter the total columns you would like "))

    width = ROWS*100
    length = COLUMNS*200

    win = pygame.display.set_mode((length, width+width))

    win.fill(WHITE)

    grid = construct_Nodes(ROWS, COLUMNS, width, length)
    font = pygame.font.Font('freesansbold.ttf', 16)
    TITLE = pygame.font.Font('freesansbold.ttf', 16)
    text = TITLE.render(
        "----------INSTRUCTIONs-------------", True, (245, 66, 191))
    text1 = font.render(
        "-right click the grid to establish starting point", True, (245, 66, 191))
    text2 = font.render(
        "-hover the mouse to the grid and enter v for vaccine", True, (245, 66, 191))
    text3 = font.render(
        "-hover the mouse to the grid and enter q for quarantine", True, (245, 66, 191))
    text4 = font.render(
        "-hover the mouse to the grid and enter p for playground", True, (245, 66, 191))
    text5 = font.render(
        "-left click the grid to erase", True, (245, 66, 191))
    text6 = font.render(
        "-enter r to erase whole grid", True, (245, 66, 191))
    text7 = font.render(
        "-enter k to start the A* search for playground", True, (245, 66, 191))
    text8 = font.render(
        "-enter l to start the A* search for quarantine", True, (245, 66, 191))
    text9 = font.render(
        "-click starting point and type 1 to change role C<default>", True, (245, 66, 191))
    text10 = font.render(
        "-click starting point and type 2 to change role V ", True, (245, 66, 191))
    text11 = font.render(
        "-click starting point and type 3 to change role P", True, (245, 66, 191))
    text12 = font.render(
        "-close program to change the grid and no matter what dont press m", True, (245, 66, 191))
    textRect = text.get_rect(topleft=(0, width))
    textRect1 = text1.get_rect(topleft=(0, width+20))
    textRect2 = text2.get_rect(topleft=(0, width+20*2))
    textRect3 = text3.get_rect(topleft=(0, width+20*3))
    textRect4 = text4.get_rect(topleft=(0, width+20*4))
    textRect5 = text5.get_rect(topleft=(0, width+20*5))
    textRect6 = text6.get_rect(topleft=(0, width+20*6))
    textRect7 = text7.get_rect(topleft=(0, width+20*7))
    textRect8 = text8.get_rect(topleft=(0, width+20*8))
    textRect9 = text9.get_rect(topleft=(0, width+20*9))
    textRect10 = text10.get_rect(topleft=(0, width+20*10))
    textRect11 = text11.get_rect(topleft=(0, width+20*11))
    textRect12 = text12.get_rect(topleft=(0, width+20*12))
    win.blit(text, textRect)
    win.blit(text1, textRect1)
    win.blit(text2, textRect2)
    win.blit(text3, textRect3)
    win.blit(text4, textRect4)
    win.blit(text5, textRect5)
    win.blit(text6, textRect6)
    win.blit(text7, textRect7)
    win.blit(text8, textRect8)
    win.blit(text9, textRect9)
    win.blit(text10, textRect10)
    win.blit(text11, textRect11)
    win.blit(text12, textRect12)
    start = None

    run = True
    print("\n\nPLEASE FOLLOW THE INSTRUCTIONS\n")
    print("-right click the grid to establish starting point")
    print("-hover the mouse to the grid and enter v for vaccine")
    print("-hover the mouse to the grid and enter q for quarantine")
    print("-hover the mouse to the grid and enter p for playground")
    print("-left click the grid to erase")
    print("-enter r to erase whole grid")
    print("-enter shift change the size of the grid(unfinished)")
    print("-type 1 to change role C<default>\n-type 2 to change role V\n-type 3 to change role P")
    print("-enter space to start the A* search")
    print("-enter m to randomize the map at your convenience")

    print("Stay put, entering the A* Path Finding Algorithm Game \n")

    while run:
        draw(win, grid, ROWS, width, COLUMNS, length)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width, COLUMNS, length)

                spot = grid[row][col]
                if not start:
                    start = spot
                    start.make_start()

            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width, COLUMNS, length)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k and start:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors_asGhostChild(grid)
                    algorithm(
                        grid, start, fetchRobotPlayground(grid))   # destination here
                if event.key == pygame.K_l and start:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    algorithm(
                        grid, start, fetchRobotQuarantine(grid))   # destination here
                if event.key == pygame.K_m:
                    start = None
                    grid = construct_Nodes(ROWS, COLUMNS, width, length)
                    for row in grid:
                        for spot in row:
                            temp = random.randint(0, 5)
                            if (temp == 0):
                                spot.make_quarantine()
                            if (temp == 1):
                                spot.make_vaccine()
                            if (temp == 2):
                                spot.make_playground()
                            if (temp == 3):
                                spot.reset()

                if event.key == pygame.K_r:
                    start = None
                    grid = construct_Nodes(ROWS, COLUMNS, width, length)

                if event.key == pygame.K_p:

                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(
                        pos, ROWS, width, COLUMNS, length)
                    spot = grid[row][col]
                    spot.make_playground()
                if event.key == pygame.K_v:

                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(
                        pos, ROWS, width, COLUMNS, length)
                    spot = grid[row][col]
                    spot.make_vaccine()
                if event.key == pygame.K_q:

                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(
                        pos, ROWS, width, COLUMNS, length)
                    spot = grid[row][col]
                    spot.make_quarantine()
                if event.key == pygame.K_1 and start:

                    role = 'roleC'
                    spot.changeRole(role)
                    print('you have chosen to be role C')
                    heuristicUpdate(grid, playerType, start)
                if event.key == pygame.K_2 and start:
                    role = 'roleV'
                    spot.changeRole(role)
                    print('you have chosen to be role V')
                    heuristicUpdate(grid, playerType, start)

                if event.key == pygame.K_3 and start:
                    role = 'roleP'
                    spot.changeRole(role)
                    print('you have chosen to be role P')
                    heuristicUpdate(grid, playerType, start)

    pygame.quit()

# for snarks who wants to change the grid a million times


def mainMain():
    while True:
        main()


mainMain()
