import random
import sys
import pygame
from pygame.locals import *
# ==================================================
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

# ==================================================

XMARGIN = int((WINDOWWIDTH-(BOARDWIDTH*(BOXSIZE+GAPSIZE)))/2)
YMARGIN = int((WINDOWHEIGHT-(BOARDHEIGHT*(BOXSIZE+GAPSIZE)))/2)

# ==================================================

assert (BOARDWIDTH*BOARDHEIGHT)%2==0,"board needs to have an even number of boxes for pairs of matches"
assert len(ALLCOLORS)*len(ALLSHAPS) *2>=BOARDWIDTH*BOARDHEIGHT,"Board is too small for the number of shapes/colors defined."

# ==================================================

def getBoxAtPixel(x,y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top=leftTopCoordsOfbox(boxx,boxy)
            boxRect=pygame.Rect(left,top,BOXSIZE,BOXSIZE)
            if boxRect.collidepoint(x,y):
                return (boxx,boxy)
    return (None,None)

# ==================================================

def drawHighlightBox(boxx,boxy):
    left,top=leftTopCoordsOfbox(boxx,boxy)
    pygame.draw.rect(DISPLAYSURF,HIGHLIGHTCOLOR,(left-5,top-5,BOXSIZE+10,BOXSIZE+10),4)

# ==================================================

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

# ==================================================


def main():
    global DISPLAYSURF,FPSCLOCK
    pygame.init()
    FPSCLOCK =  pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption("Memory Game")
    mousex =0
    mousey=0
    firstSelection=None


    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    DISPLAYSURF.fill(BG)
    startGameAnimation(mainBoard)


    while True:
        mouseClicked=False
        DISPLAYSURF.fill(BG)
        drawBoard(mainBoard,revealedBoxes)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEMOTION:
                mousex,mousey=event.pos
            elif event.type==MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked=True
        boxx,boxy=getBoxAtPixel(mousex,mousey)
        if boxx!= None and boxy!=None:
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx,boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revelboxesanimation(mainBoard,[(boxx,boxy)])
                revealedBoxes[boxx][boxy]=True
                if firstSelection==None:
                    firstSelection=(boxx,boxy)
                else:
                    icon1shape,icon1color=getShapeAndColor(mainBoard,firstSelection[0],firstSelection[1])
                    icon2shape,icon2color=getShapeAndColor(mainBoard,boxx,boxy)
                    if icon1shape != icon2shape or icon1color!=icon2color:
                        pygame.time.wait(1000)
                        coveredBoxesanimation(mainBoard,[(firstSelection[0],firstSelection[1]),(boxx,boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]]=False
                        revealedBoxes[boxx][boxy]=False
                    elif hasWon(revealedBoxes):
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)
                        mainBoard=getRandomizedBoard()
                        revealedBoxes=generateRevealedBoxesData(False)
                        drawBoard(mainBoard,revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        startGameAnimation(mainBoard)
                    firstSelection=None
        pygame.display.update()
        FPSCLOCK.tick(FPS)

# ==================================================

def hasWon(revealedBoxes):
    for i in revealedBoxes:
        if False in i:
            return False
    return True

# ==================================================

def gameWonAnimation(board):
     coveredboxes=generateRevealedBoxesData(True)
     color_1=LIGHBGCOLOR
     color_2=BG
     color_1,color_2=color_2,color_1
     DISPLAYSURF.fill(color_1)
     drawBoard(board,coveredboxes)
     pygame.display.update()
     pygame.time.wait(300)

# ==================================================

def generateRevealedBoxesData(val):
    revealedBoxes=[]
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val]*BOARDHEIGHT)
    return revealedBoxes

# ==================================================

def drawBoard(board,revealed):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top = leftTopCoordsOfbox(boxx,boxy)
            if not revealed[boxx][boxy]:
                pygame.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,BOXSIZE,BOXSIZE))
            else:
                shape,color=getShapeAndColor(board,boxx,boxy)
                drawIcon(shape,color,boxx,boxy)

# ==================================================


def leftTopCoordsOfbox(boxx,boxy):
    left =boxx*(BOXSIZE+GAPSIZE)+XMARGIN
    top =boxy*(BOXSIZE+GAPSIZE)+YMARGIN
    return (left,top)

# ==================================================

def getShapeAndColor(board,boxx,boxy):
    return board[boxx][boxy][0],board[boxx][boxy][1]

# ==================================================

def drawIcon(shape,color,boxx,boxy):
    quarter = int(BOXSIZE*0.25)
    half = int(BOXSIZE*0.5)
    left,top = leftTopCoordsOfbox(boxx,boxy)
    if shape==DONUT:
        pygame.draw.circle(DISPLAYSURF,color,(left+half,top+half),half-5)
        pygame.draw.circle(DISPLAYSURF,BG,(half+half,top+half),quarter-5)
    elif shape==SQUARE:
        pygame.draw.rect(DISPLAYSURF,color,(left+quarter,top+quarter,BOXSIZE-half,BOXSIZE-half))
    elif shape==DIAMOND:
        pygame.draw.polygon(DISPLAYSURF,color,((left+half,top),(left+BOXSIZE-1,top+half),(left+half,top+BOXSIZE-1),(left,top+half)))
    elif shape==LINES:
        for i in range(0,BOXSIZE,4):
            pygame.draw.line(DISPLAYSURF,color,(left,top+i),(left+i,top))
            pygame.draw.line(DISPLAYSURF,color,(left+i,top+BOXSIZE-1),(left+BOXSIZE-1,top+i))
    elif shape==OVAL:
        pygame.draw.ellipse(DISPLAYSURF,color,(left,top+quarter,BOXSIZE,half))

# ==================================================



def startGameAnimation(board):
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range (BOARDHEIGHT):
            boxes.append((x,y))
    random.shuffle(boxes)
    boxGroups=splitIntoGroupsOf(8,boxes)
    coveredBoxes =generateRevealedBoxesData(False)
    drawBoard(board,coveredBoxes)

    for boxGroup in boxGroups:
        revelboxesanimation(board,boxGroup)
        coveredBoxesanimation(board,boxGroup)

# ==================================================


def splitIntoGroupsOf(groupSize,thelist):
    result = []
    for i in range(0,len(thelist),groupSize):
        result.append(thelist[i:i+groupSize])
    return result


# ==================================================


def revelboxesanimation(board,boxesToReveal):
    for coverage in range (BOXSIZE,(-REVEALSPEED)-1,-REVEALSPEED):
        drawBoxCovers(board,boxesToReveal,coverage)

# ==================================================

def coveredBoxesanimation(board,boxesToCover):
    for coverage in range(0,BOXSIZE+REVEALSPEED,REVEALSPEED):
        drawBoxCovers(board,boxesToCover,coverage)

# ==================================================

def drawBoxCovers(board,boxes,coverage):
    for box in boxes:
        left,top=leftTopCoordsOfbox(box[0],box[1])
        pygame.draw.rect(DISPLAYSURF,BG,(left,top,BOXSIZE,BOXSIZE))
        shape,color=getShapeAndColor(board,box[0],box[1])
        drawIcon(shape,color,box[0],box[1])
        if coverage>0:
            pygame.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,coverage,BOXSIZE))
    pygame.display.update()
    FPSCLOCK.tick(FPS)


main()
