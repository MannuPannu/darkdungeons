import pygame

from pygame import Rect

class Entity(object):
    
    moveX = 0
    moveY = 0

    movingLeft = True

    def __init__(self, image, size, level):
        self.image = image
        self.size = size
        self.level = level #The current level the entity is in 

    def draw(self, screen):
        #Draw correct tile of image

        #Entity moving right = draw right part of image
        if self.movingLeft != True:
            screen.blit(self.image, self.pos, (self.size, 0, self.size, self.size))
        else:
            screen.blit(self.image, self.pos, (0, 0, self.size, self.size))

    def moveUp(self):
        self.moveY -= self.acceleration
        
    def moveLeft(self):
        self.moveX -= self.acceleration

    def moveRight(self):
        self.moveX += self.acceleration

    def moveDown(self):
        self.moveY += self.acceleration

    def printPos(self):
        (x, y) = self.pos

    def breakMove(self, breakSpeed):
        if self.moveX > 0:
            self.moveX = self.moveX - breakSpeed
            if self.moveX < 0: 
                self.moveX = 0 
        elif self.moveX < 0:
            self.moveX = self.moveX + breakSpeed
            if self.moveX > 0:
                self.moveX = 0

        if self.moveY > 0:
            self.moveY = self.moveY - breakSpeed
            if self.moveY < 0:
                self.moveY = 0
        elif self.moveY < 0:
            self.moveY = self.moveY + breakSpeed
            if self.moveY > 0:
                self.moveY = 0

    def stopMove(self):
        self.moveY = 0
        self.moveX = 0


    #Moves the entity
    def move(self):
        x, y = self.pos

        #Cap speed if movement speed is above max
        if self.moveX > self.maxSpeed:
            self.moveX = self.maxSpeed
        if self.moveX < -self.maxSpeed:
            self.moveX = -self.maxSpeed
        if self.moveY > self.maxSpeed:
            self.moveY = self.maxSpeed
        if self.moveY < -self.maxSpeed:
            self.moveY = -self.maxSpeed

        #Check for collision 
        isCol = self.level.checkCol(Rect(x + self.moveX, y + self.moveY, self.size, self.size))
        if isCol == True: #Collision detected!
            #Try to get closer to the colliding object
            while self.level.checkCol(Rect(x + self.moveX, y + self.moveY, self.size, self.size)) == True and ((self.moveX != 0) or (self.moveY) != 0):
                self.breakMove(1) 

            self.pos = (x + self.moveX, y + self.moveY)

        else: #Just move!
            #self.pos = (x + self.moveX, y + self.moveY) #Move this to NPS entity!
            self.moveEntity()
            self.breakMove(self.breakSpeed)

            #Set if moving left for drawing sprite
            if self.moveX > 0:
                self.movingLeft = False
            elif self.moveX < 0:
                self.movingLeft = True



            
            

        


