import pygame, Map

#An extended map to be used in level editor
class DrawableMap (Map.Map):

    #move step
    moveStep = 1

    #Draw things specific for drawable Map
    def draw(self, screen):
        #Call super class draw
        super(DrawableMap, self).draw(screen)

        #Draw rest
        (mapPosX, mapPosY) = self.pos
        (x, y) = self.playerStartPos
        screen.blit(self.main.playerStartImage, (x + mapPosX,y + mapPosY))
   
    #Return tile index from the list
    #based on the pixel pos on the map
    def getIndexFromPos(self, mousePos):
        (mapPosX, mapPosY) = self.getRelativeMapPos(mousePos)

        #Get tile coordinates
        tileX = mapPosX / self.tileSize
        tileY = mapPosY / self.tileSize

        #Calc index in tile list
        index = (tileY * self.sizeInTiles) + tileX
        return index

    #Edits the tile on the given position
    def editTileOnClick(self, mousePos, tileType):
        
        index = self.getIndexFromPos(mousePos)
        
        tile = self.areaTiles[index]

        tile.tileType = tileType
        tile.updateTileData()

    #Add start pos
    def addStartPos(self, mousePos):
        self.playerStartPos = self.getRelativeMapPos(mousePos)

    #Move map
    def moveUp(self):
        (mapPosX, mapPosY) = self.pos
        self.pos = (mapPosX, mapPosY - self.moveStep)

    def moveLeft(self):
        (mapPosX, mapPosY) = self.pos
        self.pos = (mapPosX - self.moveStep, mapPosY)

    def moveRight(self):
        (mapPosX, mapPosY) = self.pos
        self.pos = (mapPosX + self.moveStep, mapPosY)

    def moveDown(self):
        (mapPosX, mapPosY) = self.pos
        self.pos = (mapPosX, mapPosY + self.moveStep)
        
    
