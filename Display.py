#Externe Module
import pygame

#Intern files
from Settings import Settings

class Display:

    def __init__(self):

        self.screen = self.__setDisplay()
        self.clock = pygame.time.Clock()


    def displayRun(self):

        self.screen.fill((0, 0, 0))

    
    def displayUpdate(self):

        pygame.display.update()

        self.clock.tick(Settings.fps)


    def __setDisplay(self):

        display = pygame.display.set_mode([Settings.width, Settings.height])
        return display