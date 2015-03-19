import pygame, sys

import gui.inputbox

from pygame.locals import *
from classes.level.DrawableMap import DrawableMap

#Events for leveleditor

def doEvent(main):

    gameOver = False

    pressed = pygame.key.get_pressed()

    (button1, button2, button3) = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()

    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == 27:  #If player press ESC
                main.gameOver = True
            if event.key == pygame.K_q and ctrl_held:
                main.gameOver = True
            if event.key == pygame.K_n and ctrl_held: #New map
                mapSizeString = gui.inputbox.ask(main.screen, "Input map size")
                mapSize = int(mapSizeString)

                while mapSize < 0 or mapSize > 100:
                    mapSizeString = gui.inputbox.ask(main.screen, "Wrong values: Input map size again")
                    mapSize = int(mapSizeString)


                mapInit = DrawableMap((25, 25), main)
                main.level = mapInit.initEmptyMap(int(mapSizeString))
                
                print mapSizeString
            if event.key == pygame.K_s and ctrl_held: #Save map
                fileName = gui.inputbox.ask(main.screen, "Save file to")

                main.level.saveMapToFile(fileName)

            if event.key == pygame.K_l and ctrl_held: #Load map
                 mapName = gui.inputbox.ask(main.screen, "Enter map to load")
                 mapInit = DrawableMap((100, 50), main)
                 tempLevel = mapInit.fromFile("maps/" + mapName)
                 
                 if tempLevel == None:
                     print "No map found"
                 else:
                     main.level = tempLevel

            if event.key == pygame.K_1:
                main.tileSelected = 0
            elif event.key == pygame.K_2:
                main.tileSelected = 1

            elif event.key == pygame.K_3:
                main.tileSelected = 2
            elif event.key == pygame.K_9:
                main.tileSelected = 9

    if button1:
        #Find out if it is clicking on the level
        (mapX, mapY) = main.level.pos
        levelRect = Rect(mapX, mapY, main.level.getSizeInPixels(), main.level.getSizeInPixels())
        if levelRect.collidepoint(mousePos):
            if main.tileSelected != 9:
                main.level.editTileOnClick(mousePos, main.tileSelected)
            elif main.tileSelected == 9:
                main.level.addStartPos(mousePos)

        (palX, palY) = main.palette.pos
        paletteRect = Rect(palX, palY, main.palette.getWidthInPixels(), main.palette.getHeightInPixels())

        #If clicked on palette
        if paletteRect.collidepoint(mousePos):
            main.tileSelected = main.palette.getTileTypeOnClick(mousePos)
            
    #Move map with keys
    if pressed[K_UP]:
        main.level.moveUp()
    if pressed[K_DOWN]:
        main.level.moveDown()
    if pressed[K_LEFT]:
        main.level.moveLeft()
    if pressed[K_RIGHT]:
        main.level.moveRight()

