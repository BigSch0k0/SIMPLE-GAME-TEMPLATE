#Externe Module
import pygame

#Interne Dateien
from Texture import *

class Render:

    def renderScene(display, sceneElements):

        for element in sceneElements:
        
            pygame.draw.rect(display.screen,element.color,tuple(element.posData))