import pygame
from Blocks import Piece
from Blocks import Background
from Blocks import ImageBlock
from tkinter import *

"""
7 width
6 height
"""
RED = (255,0,0)
YELLOW = (200,200,0)
def turn():
    global board
    global pieces
    global screen
    global Turn
    turnDone = False
    selectedCol = int(pos[0]/cellSize)
    for i in range(0,6):
        if board[i][selectedCol] == 0:
            if Turn is False:
                pieces.append(ImageBlock("Art\\Cell-Blue.png", 128,128,[selectedCol*128, 640-i*128]))
                board[i][selectedCol] = 1
                turnDone = True
                break
            if Turn:
                pieces.append(ImageBlock("Art\\Cell-Green.png", 128,128,[selectedCol*128, 640-i*128]))
                board[i][selectedCol] = 2
                turnDone = True
                break
    if not turnDone:
        return
    for i in pieces:
        i.draw(screen)
    Turn = not Turn
    pygame.display.flip()
    checkWin()
def checkWin():
    global board
    pass
def restart():
    global board
    for i in range(0, 6):
        board.append([])
        for j in range(0, 7):
            board[i].append(0)
    background.draw(screen)
Turn = False
Running = True
previous = False
pygame.init()
screen = pygame.display.set_mode((896,768))
background = Background("Art\\Board.png")
background.draw(screen)
pygame.display.flip()
pygame.display.flip()
pieces = []
board = []
pos = []
cellSize = 128
for i in range(0,6):
    board.append([])
    for j in range(0,7):
        board[i].append(0)
Clock = pygame.time.Clock()
while Running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    if keys[pygame.K_ESCAPE]:
        Running = False
    if keys[pygame.K_SPACE]:
        restart()
    Clock.tick(60)
    pygame.event.get()
    if (pygame.mouse.get_pressed()[0]) and (previous is False):
        previous = True
    if (pygame.mouse.get_pressed()[0] == 0) and previous:
        previous = False
        pos = pygame.mouse.get_pos()
        turn()