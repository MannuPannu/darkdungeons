import pygame, Entity

from pygame import Rect


class Player(Entity.Entity):
    """ The player class """

    #Player speed
    maxSpeed = 5
    acceleration = 3
    breakSpeed = 2 #Could potentially be based on ground material (ice = slippery)

    #How far our hero can see in the fog
    sightDistance = 30

    def moveEntity(self):
        self.level.moveLevel(self.moveX, self.moveY)
        
        #Update fog of war (Could be changed to less updates)
        #Check when player has moved at least a tiles width for example
        (x, y) = self.pos
        size = self.size
        self.level.updateFog(Rect(x- self.sightDistance, y - self.sightDistance, size + self.sightDistance *2, size + self.sightDistance*2))

    def __init__(self, image, size, level, pos):
        self.pos = pos

        #Set level pos relative to players position
        level.setPosRelativeToPlayerPos(self.pos)

        super(Player, self).__init__(image, size, level)

        (x, y) = self.pos

        self.level.updateFog(Rect(x - self.sightDistance, y - self.sightDistance, size + self.sightDistance, size + self.sightDistance))

    def tick(self):
        self.move()


