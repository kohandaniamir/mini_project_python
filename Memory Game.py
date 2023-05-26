import random
import sys
import pygame
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED =8
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10
BOARDHEIGHT = 7
# ==================================
GRAY=(100,100,100)
NAVYBLUE = (60,60,100)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,128,0)
PURPLE = (255,0,255)
CYAN = (0,255,255)
# ===================================
BG = NAVYBLUE
LIGHBGCOLOR=GRAY
BOXCOLOR=WHITE
HIGHLIGHTCOLOR=BLUE
# ====================================
DONUT="donut"
SQUARE ="square"
DIAMOND ="daiamond"
LINES = 'lines'
OVAL = "oval"
# ====================================


ALLCOLORS =(RED,GREEN,BLUE,YELLOW,ORANGE,PURPLE,CYAN)
ALLSHAPS = (DONUT,SQUARE,DIAMOND,LINES,OVAL)



XMARGIN = int((WINDOWWIDTH-(BOARDWIDTH*(BOXSIZE+GAPSIZE)))/2)
YMARGIN = int((WINDOWHEIGHT-(BOARDHEIGHT*(BOXSIZE+GAPSIZE)))/2)


assert (BOARDWIDTH*BOARDHEIGHT)%2==0,"board needs to have an even number of boxes for pairs of matches"
assert len(ALLCOLORS)*len(ALLSHAPS) *2>=BOARDWIDTH*BOARDHEIGHT,"Board is too small for the number of shapes/colors defined."


def getRandomizedBoard():
    icons = []
    for color in ALLCOLORS:
        for shaps in ALLSHAPS:
            icons.append((shaps,color))
    random.shuffle(icons)

    numIconsUsed= int(BOARDWIDTH*BOARDHEIGHT/2)
    icons = icons[:numIconsUsed]*2
    random.shuffle(icons)

    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board


def main():
    global DISPLAYSURF,FPSCLOCK
    pygame.init()
    FPSCLOCK =  pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption("Memory Game")
    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)


    while True:
        DISPLAYSURF.fill(BG)
        drawBoard(mainBoard,revealedBoxes)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)






def generateRevealedBoxesData(val):
    revealedBoxes=[]
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val]*BOARDHEIGHT)
    return revealedBoxes


def drawBoard(board,revealed):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top = leftTopCoordsOfbox(boxx,boxy)
            if not revealed[boxx][boxy]:
                pygame.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,BOXSIZE,BOXSIZE))
        # else:
        #     shape,color=getShapeAndColor(board,boxx,boxy)
        #     drawIcon(shape,color,boxx,boxy)

def leftTopCoordsOfbox(boxx,boxy):
    left =boxx*(BOXSIZE+GAPSIZE)+XMARGIN
    top =boxy*(BOXSIZE+GAPSIZE)+YMARGIN
    return (left,top)


main()
