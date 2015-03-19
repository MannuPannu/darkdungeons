import pygame, Tile, random

from pygame import Rect

from Tile import Tile

#The walls should be put in lists to look for collision detection

class Room():
    """ A room in the dungeon """

    def createDoor(self):
        #Create an opening at a random pos but not in a corner
        randNr = random.randint(0, len(self.wallTiles) - 1)

        if randNr == 0: #Upper left corner
            randNr += 2 #Move right 
        elif randNr == self.width: #Upper right corner
            randNr += 2
        elif randNr == self.width + self.height: #Lower left corner
            randNr += 2
        elif randNr == self.width + self.height + self.height: #Lower right corner
            randNr += 2
            
        #Opening is 2 tiles wide
        firstTile = self.wallTiles[randNr]
        nextTile = self.wallTiles[randNr - 1]
        
        #Create a door!
        firstTile.isSolid = False 
        nextTile.isSolid = False
    
    def generateTiles(self):
        (x, y) = self.pos
        #Tiles for upper wall
        for i in range(0, self.width):
            tileRect = Rect(x + (i*self.tileSize), y , self.tileSize, self.tileSize)
            self.wallTiles.append(Tile(tileRect, True))

        #tiles for left wall
        for i in range(1, self.height):
            tileRect = Rect(x, y + (i * self.tileSize), self.tileSize, self.tileSize)
            self.wallTiles.append(Tile(tileRect, True))

        #tiles for right wall
        for i in range(1, self.height):
            tileRect = Rect(x + ((self.width -1) * self.tileSize), y + (i * self.tileSize), self.tileSize, self.tileSize)
            self.wallTiles.append(Tile(tileRect, True))

        #tiles for southern wall
        for i in range(1, self.width - 1):
            tileRect = Rect(x + (i * self.tileSize), y + ((self.height-1) * self.tileSize), self.tileSize, self.tileSize)
            self.wallTiles.append(Tile(tileRect, True))

    def __init__(self, posX, posY, height, width, wallImage):
        self.pos = (posX, posY)
        self.height = height
        self.width = width
        self.wallImage = wallImage
        self.tileSize = wallImage.get_width()

        self.wallTiles = []

        self.generateTiles()

        self.createDoor()

    def draw(self, screen):
        (x, y) = self.pos
        #Draw walls
        for tile in self.wallTiles:
            if tile.isSolid == True:
                rect = tile.rect
                screen.blit(self.wallImage, (rect.left, rect.top))

    def checkCol(self, entityRect):
        returnValue = False

        for tile in self.wallTiles:
            if tile.isSolid == True:
                rect = tile.rect
                if rect.colliderect(entityRect):
                    returnValue = True
                    break

        return returnValue
