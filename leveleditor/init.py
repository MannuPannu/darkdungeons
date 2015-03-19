import pygame

#Inits the game
def init():
    pygame.init()

    screenSize = [640, 480]
    screen=pygame.display.set_mode(screenSize)

    pygame.display.set_caption("Level editor!")

    return screen
