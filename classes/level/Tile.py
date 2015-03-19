class Tile:
    """ A tile in the level """

    def __init__(self, tileType, main, tilePos):

        self.tileType = tileType
        self.tilePos = tilePos #Pos of tile
        self.main = main

        self.updateTileData()

    def updateTileData(self):
        (wallImage, groundImage, noneImage, transparentImage) = self.main.getTileImages()

        if self.tileType == 0:
            self.tileImage = noneImage
            self.isSolid = True
        elif self.tileType == 1:
            self.tileImage = groundImage
            self.isSolid = False
        elif self.tileType == 2:
            self.tileImage = wallImage
            self.isSolid = True
        elif self.tileType == 3:
            self.tileImage = transparentImage
            self.isSolid = False

