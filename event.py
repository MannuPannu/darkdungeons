import pygame, sys

from pygame.locals import *

def doEvent(main):

    player = main.player
    gameOver = main.gameOver

    keystate = pygame.key.get_pressed()

    ctrl_held = keystate[pygame.K_LCTRL] or keystate[pygame.K_RCTRL]

    if keystate[K_UP]:
        player.moveUp()
    if keystate[K_DOWN]:
        player.moveDown()
    if keystate[K_LEFT]:
        player.moveLeft()
    if keystate[K_RIGHT]:
        player.moveRight()


    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == 27:  #If player press ESC
                gameOver = True
            if event.key == pygame.K_q and ctrl_held:
                gameOver = True

    main.gameOver = gameOver
