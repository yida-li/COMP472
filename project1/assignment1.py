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
HORIZONLINE = pygame.image.load(r'perfectHorizoneLine.png')
VERTICALLINE = pygame.image.load(r'perfectVerticalLine.png')
INSTRUCTIONS = pygame.image.load(r'instructions.png')
# Not used colors
RED = (255, 0, 0)
# Q
GREEN = (0, 255, 0)
QUARANTINE = (0, 255, 0)

# V
ORANGE = (255, 165, 0)
VACCINE = (255, 255, 0)
OPTIMALPATH = (252, 3, 115)

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
    def __init__(self, row, col, width, length, total_rows, total_columns, type):

        self.row = row
        self.col = col
        self.y = row * width
        self.x = col * length
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
        self.alphabet = 'error'
        self.Price = 100000  # edge
        self.ultimatePriceFlag = True
        ##
        # Metamorphosis

        # types are edge,node,map
        self.typeofNode = type

    def changeRole(self, role):
        if(role == 'roleC'):
            self.status = 'roleC'
        if(role == 'roleV'):
            self.status = 'roleV'
        if(role == 'roleP'):
            self.status = 'roleP'

    def make_quarantine(self):
        if (self.typeofNode != 'edgeH' and self.typeofNode != 'edgeV' and self.typeofNode != 'node'):
            self.status = 'quarantine'

    def make_vaccine(self):
        if (self.typeofNode != 'edgeH' and self.typeofNode != 'edgeV' and self.typeofNode != 'node'):
            self.status = 'vaccine'

    def make_playground(self):
        if (self.typeofNode != 'edgeH' and self.typeofNode != 'edgeV' and self.typeofNode != 'node'):
            self.status = 'playground'

    def get_pos(self):
        return self.row, self.col

    def make_shortestpath(self):
        self.color = OPTIMALPATH

    def reset(self):
        self.color = WHITE
        self.status = 'vacant'

    def make_start(self):
        self.status = 'roleC'
        self.color = ORANGE

    def make_path(self):
        self.color = PURPLE

    def is_accessible(self):

        return self.access

    def is_quarantine(self):

        return self.status == 'quarantine'

    def is_playground(self):

        return self.status == 'playground'

    def is_Map(self):

        return self.typeofNode == 'map'

    def is_EdgeH(self):
        return self.typeofNode == 'edgeH'

    def is_EdgeV(self):
        return self.typeofNode == 'edgeV'

    def is_Alphabet(self):
        return self.typeofNode == 'node'

    def drawImage(self, win):

        if (self.status == 'playground'):
            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))
            win.blit(IMG, (self.col*100+25, self.row*50+12))

        elif (self.status == 'vaccine'):
            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))
            win.blit(IMG_VAC, (self.col*100+50, self.row*50+12))
        elif (self.status == 'quarantine'):
            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))
            win.blit(IMG_VIR, (self.col*100+25, self.row*50+12))

        elif(self.status == 'roleP'):
            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))
            win.blit(ROLEP, (self.x, self.y))
        elif(self.status == 'roleV'):
            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))
            win.blit(ROLEV, (self.x, self.y))
        elif(self.status == 'roleC'):
            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))
            win.blit(ROLEC, (self.x, self.y))

        elif (self.typeofNode == 'edgeH'):

            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))

            if(self.Price < 2500):

                font = pygame.font.Font('freesansbold.ttf', 20)
                Display = font.render(str(self.Price), 1, BLACK)
                textRect = Display.get_rect(
                    center=(self.col*100+50, self.row*50+25))
                win.blit(Display, textRect)
            else:
                win.blit(HORIZONLINE, (self.x, self.y+25))

        elif (self.typeofNode == 'edgeV'):

            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))
            if(self.Price < 2500):

                font = pygame.font.Font('freesansbold.ttf', 20)
                Display = font.render(str(self.Price), 1, BLACK)
                textRect = Display.get_rect(
                    center=(self.col*100+50, self.row*50+25))
                win.blit(Display, textRect)
            else:
                win.blit(VERTICALLINE, (self.x+25, self.y))

        elif (self.alphabet != 'error'):

            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render(
                self.alphabet, True, BLACK)
            textRect = text.get_rect(center=(self.col*100+50, self.row*50+25))

            win.blit(text, textRect)
        else:
            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.length, self.width))

    # under the scenario that i need to potentially use this which is coincedently implaussible
    def updateNeighborP(self, grid):

        self.neighbors = []

        # DOWN
        if self.row < self.total_rows - 1 and grid[self.row + 1][self.col].is_accessible() and not grid[self.row + 1][self.col].is_quarantine():
            self.neighbors.append(grid[self.row + 1][self.col])

        # UP
        if self.row > 0 and grid[self.row - 1][self.col].is_accessible() and not grid[self.row - 1][self.col].is_quarantine():
            self.neighbors.append(grid[self.row - 1][self.col])

        # RIGHT
        if self.col < self.total_columns - 1 and grid[self.row][self.col + 1].is_accessible() and not grid[self.row][self.col + 1].is_quarantine():
            self.neighbors.append(grid[self.row][self.col + 1])

        # LEFT
        if self.col > 0 and grid[self.row][self.col - 1].is_accessible() and not grid[self.row][self.col - 1].is_quarantine():
            self.neighbors.append(grid[self.row][self.col - 1])

    def update_neighborV(self, grid):
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

    def update_neighborC(self, grid):
        self.neighbors = []

        # DOWN
        if self.row < self.total_rows - 1 and self.is_accessible() and not grid[self.row + 1][self.col].is_playground():
            self.neighbors.append(grid[self.row + 1][self.col])

        # UP
        if self.row > 0 and self.is_accessible() and not grid[self.row - 1][self.col].is_playground():
            self.neighbors.append(grid[self.row - 1][self.col])

        # RIGHT
        if self.col < self.total_columns - 1 and self.is_accessible() and not grid[self.row][self.col + 1].is_playground():
            self.neighbors.append(grid[self.row][self.col + 1])

        # LEFT
        if self.col > 0 and self.is_accessible() and not grid[self.row][self.col - 1].is_playground():
            self.neighbors.append(grid[self.row][self.col - 1])

    def update_all_neighborEdges(self, grid):
        self.neighbors = []

        # DOWN
        if self.row < self.total_rows - 1 and self.is_accessible():
            if grid[self.row + 1][self.col].is_Map() == True:

                self.neighbors.append(grid[self.row + 1][self.col])

        # UP
        if self.row > 0 and self.is_accessible():
            if grid[self.row - 1][self.col].is_Map() == True:

                self.neighbors.append(grid[self.row - 1][self.col])

        # RIGHT
        if self.col < self.total_columns - 1 and self.is_accessible():
            if grid[self.row][self.col + 1].is_Map() == True:

                self.neighbors.append(grid[self.row][self.col + 1])

        # LEFT
        if self.col > 0 and self.is_accessible():
            if grid[self.row][self.col - 1].is_Map() == True:

                self.neighbors.append(grid[self.row][self.col - 1])


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def construct_Nodes(rows, columns, width, length):

    mySuperAlphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'aQ', 'bQ', 'cQ', 'dQ', 'eQ', 'fQ', 'gQ', 'hQ', 'iQ', 'jQ', 'kQ', 'lQ', 'mQ', 'nQ', 'oQ', 'pQ', 'qQ', 'rQ', 'sQ', 'tQ', 'uQ', 'vQ', 'wQ', 'xQ', 'yQ', 'a@Q', 'b@', 'c@', 'd@', 'e@', 'f@', 'g@', 'h@', 'i@', 'j@', 'k@', 'l@', 'm@', 'n@', 'o@', 'p@', 'q@', 'r@', 's@', 't@', 'u@', 'v@', 'w@', 'x@', 'y@', 'z@', 'AM', 'BM', 'CM', 'DM', 'EM', 'FM', 'GM', 'HM', 'IM', 'JM', 'KM', 'LM', 'MM', 'NM', 'OM', 'PM', 'QM', 'RM', 'SM', 'TM', 'UM', 'VM', 'WM', 'XM', 'YM', 'ZM', 'ZzM', 'Yy', 'Xx', 'Ww',
                        'Vv', 'Uu', 'Tt', 'Ss', 'Rr', 'Qq', 'Pp', 'Oo', 'Nn', 'Mm', 'Ll', 'Kk', 'Jj', 'Ii', 'Hh', 'Gg', 'Ff', 'Ee', 'Dd', 'Cc', 'Bb', 'Aa', 'aAa', 'bBb', 'cCc', 'dDd', 'v1x', 'v2x', 'v3x', 'v4x',
                        'v5x', 'v6x', 'v7x', 'v8x', 'v9x', '1v0x', '1v1x', '1v2x', '1v3x', '1v4x', '1v5x', '1v6x', '1v7x', '1v8x', '1v9x', '2v0x', '2v1x', '2v2x', '2v3x', '2v4x', '2v5x', '2v6x', '2v7x', '2v8x', '2v9x', '30']

    counter = 0
    R = 2*rows+1  # 5
    C = 2*columns+1  # 7
    gap = width // rows  # 50
    lgap = length//columns  # 100
    type = 'null'
    indexX = True      # declare x flag set to 1
    grid = []

    for i in range(R):
        grid.append([])
        indexY = True  # declare Y flag set to 1
        for j in range(C):

            if(indexX == 1):
                if(indexY == 1):
                    type = 'node'
                    spot = Spot(i, j, gap, lgap, R, C, type)

                    spot.alphabet = mySuperAlphabets[counter]
                    counter = counter+1

                else:
                    type = 'edgeH'
                    spot = Spot(i, j, gap, lgap, R, C, type)

            else:
                if(indexY == 1):
                    type = 'edgeV'
                    spot = Spot(i, j, gap, lgap, R, C, type)
                else:
                    type = 'map'

                    spot = Spot(i, j, gap, lgap, R, C, type)
            indexY = not indexY  # flip the  y flag

            grid[i].append(spot)

        indexX = not indexX  # flip the x flag

    return grid


def draw_grid(win, rows, width, columns, length):
    gap = width // rows
    # gap=100
    lgap = length // columns
    # lgap= 200

    pygame.draw.line(win, RED, (0, 0),
                     ((columns*2+1)*100, 0), 10)
    pygame.draw.line(win, RED, (0, (rows*2+1)*50),
                     ((columns*2+1)*100, (rows*2+1)*50), 10)

    pygame.draw.line(win, RED, (0, (rows*2+1)*50),
                     (0, 0), 10)
    pygame.draw.line(win, RED, ((columns*2+1)*100, (rows*2+1)*50),
                     ((columns*2+1)*100, 0), 10)


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


def reconstruct_path(came_from, destination):

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
            reconstruct_path(came_from, Destination)
            money = calculatePrice(came_from, Destination)
            currentNODE.color = PURPLE
            start.color = ORANGE

            return money

        for INDEXNEIGHBOR in currentNODE.neighbors:
            tempSCORETRACKER = g_scoreDictionary[currentNODE] + 1

            if tempSCORETRACKER < g_scoreDictionary[INDEXNEIGHBOR]:
                # came_from[i]= currentNode  wtv node we're on right now
                came_from[INDEXNEIGHBOR] = currentNODE
                # g_scoreD[i]=
                g_scoreDictionary[INDEXNEIGHBOR] = tempSCORETRACKER
                f_scoreDictionary[INDEXNEIGHBOR] = tempSCORETRACKER + \
                    h(INDEXNEIGHBOR.get_pos(), Destination.get_pos()) + \
                    INDEXNEIGHBOR.Price    # heuristic

                if INDEXNEIGHBOR not in open_set_hash:  # look inside queue and add a count
                    count += 1
                    open_set.put(
                        (f_scoreDictionary[INDEXNEIGHBOR], count, INDEXNEIGHBOR))  # put in f score, the incremented count , spot object
                    open_set_hash.add(INDEXNEIGHBOR)

    return 1000


def calculatePrice(came_from, destination):

    Price = 0.0

    while destination in came_from:

        destination = came_from[destination]
        destination.make_path()
        if (destination.Price < 6969):

            Price = destination.Price+Price

    return Price


def reconstruct_path1(came_from, destination):

    while destination in came_from:
        print(destination.x, destination.y)
        destination = came_from[destination]
        destination.make_path()


def algorithm1(grid, start, Destination):

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
            reconstruct_path(came_from, Destination)
            currentNODE.color = PURPLE
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
                    h(INDEXNEIGHBOR.get_pos(), Destination.get_pos()) + \
                    INDEXNEIGHBOR.Price    # heuristic

                if INDEXNEIGHBOR not in open_set_hash:  # look inside queue and add a count
                    count += 1
                    open_set.put(
                        (f_scoreDictionary[INDEXNEIGHBOR], count, INDEXNEIGHBOR))  # put in f score, the incremented count , spot object
                    open_set_hash.add(INDEXNEIGHBOR)

    return False


def reconstruct_path2(came_from, destination):

    while destination in came_from:
        print(destination.x, destination.y)
        destination = came_from[destination]
        destination.make_shortestpath()


def algorithm2(grid, start, Destination):

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
            reconstruct_path2(came_from, Destination)
            currentNODE.color = OPTIMALPATH
            start.color = OPTIMALPATH
            return True

        for INDEXNEIGHBOR in currentNODE.neighbors:
            tempSCORETRACKER = g_scoreDictionary[currentNODE] + 1

            if tempSCORETRACKER < g_scoreDictionary[INDEXNEIGHBOR]:
                # came_from[i]= currentNode  wtv node we're on right now
                came_from[INDEXNEIGHBOR] = currentNODE
                # g_scoreD[i]=
                g_scoreDictionary[INDEXNEIGHBOR] = tempSCORETRACKER
                f_scoreDictionary[INDEXNEIGHBOR] = tempSCORETRACKER + \
                    h(INDEXNEIGHBOR.get_pos(), Destination.get_pos()) + \
                    INDEXNEIGHBOR.Price    # heuristic

                if INDEXNEIGHBOR not in open_set_hash:  # look inside queue and add a count
                    count += 1
                    open_set.put(
                        (f_scoreDictionary[INDEXNEIGHBOR], count, INDEXNEIGHBOR))  # put in f score, the incremented count , spot object
                    open_set_hash.add(INDEXNEIGHBOR)

    return False


def reconstruct_path3(came_from, destination):

    while destination in came_from:
        print(destination.x, destination.y)
        destination = came_from[destination]
        destination.make_path()


def algorithm3(grid, start, Destination):

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
            reconstruct_path(came_from, Destination)
            currentNODE.color = PURPLE
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
                    h(INDEXNEIGHBOR.get_pos(), Destination.get_pos()) + \
                    INDEXNEIGHBOR.Price    # heuristic

                if INDEXNEIGHBOR not in open_set_hash:  # look inside queue and add a count
                    count += 1
                    open_set.put(
                        (f_scoreDictionary[INDEXNEIGHBOR], count, INDEXNEIGHBOR))  # put in f score, the incremented count , spot object
                    open_set_hash.add(INDEXNEIGHBOR)

    return False


# a functionn inside a function this is real heuristic programming, python is so useful wow
def fetchRobotPlayground(grid):

    for row in grid:
        for spot in row:
            if spot.status == 'playground' and spot.ultimatePriceFlag == True:
                spot.ultimatePriceFlag = False
                return spot


def fetchRobotPlayground1(grid):

    for row in grid:
        for spot in row:
            if spot.status == 'playground' and spot.ultimatePriceFlag == False:
                spot.ultimatePriceFlag = True
                return spot


# this will def return 2 if there is 2 playground n if n playground 0 then 0 playerground
def fetchTheAmountOfRobotsPlayground(grid):
    counter = 0
    for row in grid:
        for spot in row:
            if spot.status == 'playground':
                counter = counter+1
    return counter


# a complex matrix of sophistcated calcuations and will return a nice path with everything calculated
def SuperUltimateMachineLearning(grid, start):

    threshold = 10000
    hint = 10000
    number = fetchTheAmountOfRobotsPlayground(grid)

    gundam = {}
    for i in range(number):
        gundam[i] = algorithm(grid, start, fetchRobotPlayground(grid))
        if gundam[i] < threshold:
            threshold = gundam[i]
            hint = i

    for j in range(number):
        if j == hint:
            gundam[j] = algorithm2(grid, start, fetchRobotPlayground1(grid))
            return threshold
        else:
            gundam[j] = algorithm(grid, start, fetchRobotPlayground1(grid))

    return threshold


def SuperUltimateMachineLearning1(grid, start):

    threshold = 10000
    hint = 10000
    number = fetchTheAmountOfRobotsQuarantine(grid)

    gundam = {}
    for i in range(number):

        gundam[i] = algorithm(grid, start, fetchRobotQuarantine(grid))
        if gundam[i] < threshold:
            threshold = gundam[i]
            hint = i

    for j in range(number):
        if j == hint:
            gundam[j] = algorithm2(grid, start, fetchRobotQuarantine1(grid))
            return threshold
        else:
            gundam[j] = algorithm(grid, start, fetchRobotQuarantine1(grid))

    return threshold


def checkRobotPlayground(grid):
    flag = False
    for row in grid:
        for spot in row:
            if spot.status == 'playground':
                flag = True
    return flag


def fetchRobotQuarantine(grid):
    for row in grid:
        for spot in row:
            if spot.status == 'quarantine' and spot.ultimatePriceFlag == True:
                spot.ultimatePriceFlag = False
                return spot


def fetchRobotQuarantine1(grid):
    for row in grid:
        for spot in row:
            if spot.status == 'quarantine' and spot.ultimatePriceFlag == False:
                spot.ultimatePriceFlag = True
                return spot


# this will def return 2 if there is 2 playground n if n playground 0 then 0 playerground
def fetchTheAmountOfRobotsQuarantine(grid):
    counter = 0
    for row in grid:
        for spot in row:
            if spot.status == 'quarantine':
                counter = counter+1
    return counter


def checkRobotQuarantine(grid):
    flag = False
    for row in grid:
        for spot in row:
            if spot.status == 'quarantine':
                flag = True
    return flag


def fetchRobotVaccine(grid):
    for row in grid:
        for spot in row:
            if spot.status == 'vaccine':
                return spot


def checkRobotVaccine(grid):
    flag = False
    for row in grid:
        for spot in row:
            if spot.status == 'vaccine':
                flag = True
    return flag


def identify(start):
    print(start.Price)
    # for INDEXNEIGHBOR in start.neighbors:

    #  print(start.Price)


def addTravellingCostChildren(node):  # node with child

    temp = 0.0
    count = 0  # number of neighbor
    for INDEXNEIGHBOR in node.neighbors:

        if INDEXNEIGHBOR.status == 'vacant':
            temp = temp+1.0
        if INDEXNEIGHBOR.status == 'vaccine':
            temp = temp+2.0
        if INDEXNEIGHBOR.status == 'quarantine':
            temp = 100000
            node.access = False
       # if INDEXNEIGHBOR.status == 'playground':
          #  temp = temp+0
        count = count+1
    if (count == 2):
        node.Price = temp/2
    if (count == 1):
        node.Price = temp


def addTravellingCostPatient(node):  # node with patient

    temp = 0.0
    count = 0  # number of neighbor
    # if playground checker gets triggered twice then the edge is will be blocked for whatever reasons
    playgroundChecker = 0
    for INDEXNEIGHBOR in node.neighbors:

        if INDEXNEIGHBOR.status == 'vacant':
            temp = temp+1.0
        if INDEXNEIGHBOR.status == 'vaccine':
            temp = temp+2.0
        if INDEXNEIGHBOR.status == 'playground':
            temp = temp+3.0
            playgroundChecker = playgroundChecker+1
        count = count+1

    if (count == 2):
        node.Price = temp/2
    if (count == 1):
        node.Price = temp
    if (playgroundChecker == 2):
        node.access = False
        node.Price = 100000


def addTravellingCostHealth(start):  # start with child

    temp = 0.0
    count = 0  # number of neighbor
    for INDEXNEIGHBOR in start.neighbors:

        if INDEXNEIGHBOR.status == 'playground':
            temp = temp+1.0
        if INDEXNEIGHBOR.status == 'vacant':
            temp = temp+2.0
        if INDEXNEIGHBOR.status == 'quarantine':
            temp = temp+3.0
        count = count+1
    if (count == 2):
        start.Price = temp/2
    if (count == 1):
        start.Price = temp


def main():

    playerType = 'roleC'
    pygame.init()
    print("PLEASE SET UP THE MAP PERIMETER")
    print("recommended size : 10 rows, 5 columns")
    ROWS = int(input("Enter the total rows you would like "))
    COLUMNS = int(input("Enter the total columns you would like "))

    width = ROWS*50
    length = COLUMNS*100

    x = (COLUMNS*2+1)*100
    y = (ROWS*2+1)*50
    win = pygame.display.set_mode((x+10, y+250))
    win.fill(WHITE)
    grid = construct_Nodes(ROWS, COLUMNS, width, length)

    win.blit(INSTRUCTIONS, (20, y+20))
    start = None

    run = True
    print("\n\nPLEASE FOLLOW THE INSTRUCTIONS\n")
    print("-right click the grid to establish starting point")
    print("-hover the mouse to the grid and enter v for vaccine")
    print("-hover the mouse to the grid and enter q for quarantine")
    print("-hover the mouse to the grid and enter p for playground")
    print("-left click the grid to erase")
    print("-enter r to erase whole grid")
    print("-type 1 to change role C<default>\n-type 2 to change role V\n-type 3 to change role P")
    print("-enter m to start the A* search ")
    print("-enter s to randomize the map at your convenience")
    print("Stay put, entering the A* Path Finding Algorithm Game \n")
    for row in grid:
        for spot in row:
            temp = random.randint(0, 10)
            if (temp == 0 and spot.typeofNode != 'edgeH' and spot.typeofNode != 'edgeV' and spot.typeofNode != 'node'):
                spot.make_quarantine()
            if (temp == 1 and spot.typeofNode != 'edgeH' and spot.typeofNode != 'edgeV' and spot.typeofNode != 'node'):
                spot.make_vaccine()
            if (temp == 2 and spot.typeofNode != 'edgeH' and spot.typeofNode != 'edgeV' and spot.typeofNode != 'node'):
                spot.make_playground()
            if (temp == 3 and spot.typeofNode != 'edgeH' and spot.typeofNode != 'edgeV' and spot.typeofNode != 'node'):
                spot.reset()
    while run:
        draw(win, grid, ROWS, width, COLUMNS, length)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width, COLUMNS, length)
                limitX, limitY = pos
                if (limitX < x and limitY < y):
                    spot = grid[row][col]

                    if not start:
                        start = spot
                        start.make_start()
            if pygame.mouse.get_pressed()[1]:  # Middle
                pos = pygame.mouse.get_pos()
                limitX, limitY = pos
                if (limitX < x and limitY < y):
                    row, col = get_clicked_pos(
                        pos, ROWS, width, COLUMNS, length)
                    spot = grid[row][col]
                    identify(spot)

            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                limitX, limitY = pos
                if (limitX < x and limitY < y):
                    row, col = get_clicked_pos(
                        pos, ROWS, width, COLUMNS, length)
                    spot = grid[row][col]
                    spot.reset()
                    if spot == start:
                        start = None

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE and start:

                    if (playerType == 'roleC'):

                        if(checkRobotQuarantine(grid) == True):

                            for row in grid:
                                for spot in row:
                                    spot.update_all_neighborEdges(grid)
                                    addTravellingCostPatient(spot)
                            for row in grid:
                                for spot in row:
                                    spot.update_neighborC(grid)

                            number = SuperUltimateMachineLearning1(grid, start)
                            font = pygame.font.Font('freesansbold.ttf', 29)

                            Display = font.render(
                                'Shortest Path Cost:'+str(number), 1, OPTIMALPATH)
                            textRect = Display.get_rect(
                                topleft=(400, y+60))
                            win.blit(Display, textRect)

                    if (playerType == 'roleP'):

                        if(checkRobotPlayground(grid) == True):

                            for row in grid:
                                for spot in row:
                                    spot.update_all_neighborEdges(grid)
                                    addTravellingCostChildren(spot)
                            for row in grid:
                                for spot in row:
                                    spot.updateNeighborP(grid)

                            number = SuperUltimateMachineLearning(grid, start)
                            font = pygame.font.Font('freesansbold.ttf', 29)

                            Display = font.render(
                                'Shortest Path Cost:'+str(number), 1, OPTIMALPATH)
                            textRect = Display.get_rect(
                                topleft=(400, y+60))
                            win.blit(Display, textRect)

                    if (playerType == 'roleV'):
                        if(checkRobotVaccine(grid) == True):

                            for row in grid:
                                for spot in row:
                                    spot.update_all_neighborEdges(grid)
                                    addTravellingCostHealth(spot)
                            for row in grid:
                                for spot in row:
                                    spot.update_neighborC(grid)
                            algorithm1(
                                grid, start, fetchRobotVaccine(grid))   # destination here

                if event.key == pygame.K_s:
                    start = None
                    grid = construct_Nodes(ROWS, COLUMNS, width, length)
                    for row in grid:
                        for spot in row:
                            temp = random.randint(0, 10)
                            if (temp == 0 and spot.typeofNode != 'edgeH' and spot.typeofNode != 'edgeV' and spot.typeofNode != 'node'):
                                spot.make_quarantine()
                            if (temp == 1 and spot.typeofNode != 'edgeH' and spot.typeofNode != 'edgeV' and spot.typeofNode != 'node'):
                                spot.make_vaccine()
                            if (temp == 2 and spot.typeofNode != 'edgeH' and spot.typeofNode != 'edgeV' and spot.typeofNode != 'node'):
                                spot.make_playground()
                            if (temp == 3 and spot.typeofNode != 'edgeH' and spot.typeofNode != 'edgeV' and spot.typeofNode != 'node'):
                                spot.reset()

                if event.key == pygame.K_r:
                    start = None
                    win.fill(WHITE)

                    win.blit(INSTRUCTIONS, (20, y+20))
                    grid = construct_Nodes(ROWS, COLUMNS, width, length)
                    playerType = 'roleC'

                if event.key == pygame.K_x:
                    import sys
                    sys.exit("BYE")

                if event.key == pygame.K_p:

                    pos = pygame.mouse.get_pos()
                    limitX, limitY = pos
                    if (limitX < x and limitY < y):
                        row, col = get_clicked_pos(
                            pos, ROWS, width, COLUMNS, length)
                        spot = grid[row][col]
                        spot.make_playground()

                if event.key == pygame.K_v:

                    pos = pygame.mouse.get_pos()
                    limitX, limitY = pos
                    if (limitX < x and limitY < y):
                        row, col = get_clicked_pos(
                            pos, ROWS, width, COLUMNS, length)
                        spot = grid[row][col]
                        spot.make_vaccine()
                if event.key == pygame.K_q:

                    pos = pygame.mouse.get_pos()
                    limitX, limitY = pos
                    if (limitX < x and limitY < y):
                        row, col = get_clicked_pos(
                            pos, ROWS, width, COLUMNS, length)
                        spot = grid[row][col]
                        spot.make_quarantine()
                if event.key == pygame.K_1 and start:

                    role = 'roleC'
                    spot.changeRole(role)
                    playerType = 'roleC'
                    print('you have chosen to be role C')
                    heuristicUpdate(grid, playerType, start)
                if event.key == pygame.K_2 and start:

                    role = 'roleV'
                    playerType = 'roleV'
                    spot.changeRole(role)
                    print('you have chosen to be role V')
                    heuristicUpdate(grid, playerType, start)

                if event.key == pygame.K_3 and start:

                    role = 'roleP'
                    playerType = 'roleP'
                    spot.changeRole(role)
                    print('you have chosen to be role P')
                    heuristicUpdate(grid, playerType, start)

    pygame.quit()


def mainMain():
    while True:
        main()


mainMain()
