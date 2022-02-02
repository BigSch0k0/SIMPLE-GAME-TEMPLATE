#interne Dateien
from Texture import *


class Entity:

    def __init__(self, x = 150, y = 150, w = 50, h = 50, color = Color.red):

        #Positionsattribute
        self.posX = x
        self.posY = y
        self.width = w
        self.height = h

        self.posData = [self.posX, self.posY, self.width, self.height]

        #Render relevante Attribute
        self.texture = color
        self.color = color

    def updatePos(self, x=0, y=0):
        
        self.posX += x
        self.posY += y
        self.posData = [self.posX, self.posY, self.width, self.height]
