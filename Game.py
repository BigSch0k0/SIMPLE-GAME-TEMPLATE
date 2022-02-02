#Externe Module
import pygame
import sys

#Interne Dateien
from Display import Display
from Renderer import Render
from Scene import Scene
from Keyboard import Keyboard


class Game:

    def __init__(self):

        #Attribute       
        self.display = None
        
        self.run = True
        #Methodenaufrufe
        self.__init()
        

    def gameLoop(self):


        #-----Beispiel Szene------    
        scene = Scene()
        scene.sceneCreate_RANDOM()

        scene.sceneLoad("INGAME::001::001")
        #-------------------------

        while self.run:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.display.displayRun()


            #------------Entry Point----------------


            self.__graphicsEvents(scene)
            self.__keyboardEvents(scene, event)


            #---------------------------------------

            self.display.displayUpdate()

    
    def __init(self):

        self.display = Display()

    def __graphicsEvents(self, scene):
        
        Render.renderScene(self.display, scene.contentEntities_OBJECT)

    def __keyboardEvents(self, scene, event):
        
        Keyboard.isPressed(scene.contentEntities_OBJECT[0], event)
            