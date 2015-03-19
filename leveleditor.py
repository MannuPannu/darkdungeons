import pygame,sys

from leveleditor import init, event, render

#from classes.level.Map import Map
from classes.level.DrawableMap import DrawableMap
from leveleditor.Palette import Palette

class Main:

    wallImage = pygame.image.load("img/walledit.png")
    groundImage = pygame.image.load("img/groundedit.png")
    noneImage = pygame.image.load("img/noneedit.png")
    playerStartImage = pygame.image.load("img/playerstart.png")
    clearFogImage = pygame.image.load("img/transparent.png")

    #Inits the game
    def init(self):
        pygame.init()

        screenSize = [640, 480]
        self.screen = pygame.display.set_mode(screenSize)

        pygame.display.set_caption("Level editor!")

        #Load font texts
        helpTextFont = pygame.font.Font('FOO.ttf', 20)
        self.newMapText = helpTextFont.render("Ctrl-N : New map", True, (255, 255, 255))
        self.saveMapText = helpTextFont.render("Ctrl-S : Save map", True, (255, 255, 255))
        self.loadMapText = helpTextFont.render("Ctrl-L : Load map", True, (255, 255, 255))

        self.palette = Palette((450, 50), self)

    def __init__(self):
    #Create a empty map
        self.mapInit = DrawableMap((25, 25), self)
        self.level = self.mapInit.initEmptyMap(15)

        self.quitProgram = False
        self.init() #Init game

        self.tileSelected = 0

        self.startGameLoop()

    def startGameLoop(self):
    #Main game loop
        while True:

            event.doEvent(self)

            if self.quitProgram == True:
                break

            render.doRender(self)

        pygame.quit()

    def getTileImages(self):
        return (self.wallImage, self.groundImage, self.noneImage, self.clearFogImage)


#Start main class here
levelEditor = Main()

