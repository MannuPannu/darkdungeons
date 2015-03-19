import pygame, init, event, render, update

import gui.inputbox

from classes.entities.Player import Player
from classes.level.Level import Level

class Main():

    wallImage = pygame.image.load("img/walledit.png")
    groundImage = pygame.image.load("img/ground.png")
    noneImage = pygame.image.load("img/none.png")
    playerStartImage = pygame.image.load("img/playerstart.png")
    playerImage = pygame.image.load("img/hero.png")
    clearFogImage = pygame.image.load("img/transparent.png")

    def __init__(self):

        self.gameOver = False

        self.screen = init.init()

        levelName = gui.inputbox.ask(self.screen, "Input level to load")

        self.level = Level("maps/" + levelName, self, (0,0))

        while self.level.mapFileLoaded == True:
            self.screen.fill((0,0,0))
            levelName = gui.inputbox.ask(self.screen, "Input map to load")
            self.level = Level("maps/" + levelName, self, (0,0))

        #Create main player in that room
        self.player = Player(self.playerImage, 15, self.level, (300, 200))

        self.startGameLoop()

    def startGameLoop(self):
    #Main game loop
        while True:
            event.doEvent(self)

            if self.gameOver == True:
                break

            update.doUpdate(self) 
    
            render.doRender(self)

            pygame.time.delay(75)

    pygame.quit()

    def getTileImages(self):
        return (self.wallImage, self.groundImage, self.noneImage, self.clearFogImage)

game = Main()



