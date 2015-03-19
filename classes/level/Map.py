import pygame, string

from TileArea import TileArea
from Tile import Tile

from pygame import Rect

#It takes a map file and creates tiles for a map

class Map(TileArea):
    """ A map level """

    #Default starting pos
    playerStartPos = (0,0)
   
    def initEmptyMap(self, sizeInTiles):
        self.initArea("0", sizeInTiles)
        return self
    
    #Parses the map file and create tiles and put them in a list
    def loadMapFile(self, mapFileName):

        try:
            f = open(mapFileName)
        except IOError as e:
            print 'Map file not found'
            return False

        line = f.readline() #Load player start pos
        tempList = line.strip().split(" ")
        self.playerStartPos = (int(tempList[0]), int(tempList[1]))

        line = f.readline() #Load map size
        self.sizeInTiles = int(line)

        for i, line in enumerate(f):
            #remove \n
            lineTiles = line.strip().split(" ")

            #Create tiles from the row
            for j, tileType in enumerate(lineTiles):
                self.areaTiles.append(self.createTile(tileType, (i, j)))

        return True
            
    #1 Loads tiles from a file
    def fromFile(self, mapFileName):
        if self.loadMapFile(mapFileName):
            return self
        else:
            return None # no map file was found, return none


    def checkCol(self, entityRect):
        returnValue = False

        (mapX, mapY) = self.pos

        #print "MapX: " + str(mapX) + "MapY: " + str(mapY)
        (x, y, w, h) = entityRect

        #Calc entity pos in relation to map pos
        entityPosX = x - mapX
        entityPosY = y - mapY
        
        #Get tiles the entity is over
        tilesInArea = self.getTileArea((entityPosX, entityPosY, w, h))

        #Check if entity collides with any of those tiles
        for i, tile in enumerate(tilesInArea):

            if tile.isSolid == True:
                #Calc boundaries of this tile
                (x, y) = tile.tilePos
                
                tileRect = Rect(x, y, self.tileSize, self.tileSize)

                 #Calc boundaries of entity
                entityRect = Rect(entityPosX, entityPosY, w, h)

                 #Check if they collide
                if tileRect.colliderect(entityRect):
                    returnValue = True
                    break

        return returnValue

    def saveMapToFile(self, fileName):

        filePath = "maps/" + fileName

        print filePath
        f = open(filePath, "w+")
        
        #Save player start pos
        (x, y) = self.playerStartPos
        f.write(str(x) + " " + str(y) + "\n")

        #Save map size
        f.write(str(self.sizeInTiles) + '\n')

        #Save tiles
        tileIndex = 0

        for i in range(self.sizeInTiles):
            #Create string to write to file
            s = ""
            for j in range(self.sizeInTiles):
                tile = self.areaTiles[tileIndex]
                s += str(tile.tileType) + ' '
                tileIndex += 1

            s = s[:-1] + '\n'

            f.write(s)





