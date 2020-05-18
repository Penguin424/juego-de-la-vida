import pygame as pg
import numpy as np
import time
import sys

pg.init()

width, height = 1000, 1000

screen = pg.display.set_mode((height,width))

bg = 25, 25, 25

screen.fill(bg)

nxC, nyC = 50, 50

dimCW = width / nxC
dimCH = height / nyC

gameState = np.zeros((nxC,nyC))

pauseExect = False

while True:
    
    newGameState = np.copy(gameState)
    screen.fill(bg)
    time.sleep(0.2)

    for evt in pg.event.get():
        if evt.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif evt.type == pg.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pg.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pg.mouse.get_pos()

            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))

            newGameState[celX, celY] = not mouseClick[2]

    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:

                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                        gameState[(x)     % nxC, (y - 1) % nyC] + \
                        gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                        gameState[(x - 1) % nxC, (y)     % nyC] + \
                        gameState[(x + 1) % nxC, (y)     % nyC] + \
                        gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                        gameState[(x)     % nxC, (y + 1) % nyC] + \
                        gameState[(x + 1) % nxC, (y + 1) % nyC]

                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            poly = [((x) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    ((x) * dimCW, (y + 1) * dimCH)
            ]

            if newGameState[x, y] == 0:
                pg.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pg.draw.polygon(screen, (255, 255, 255), poly, 0)

    gameState = np.copy(newGameState)

    pg.display.flip()

