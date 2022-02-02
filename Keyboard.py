#Externe Module
import pygame


class Keyboard:

    def isPressed(entity, event):
        

        button = pygame.key.get_pressed()

        if button[pygame.K_w]: entity.updatePos(0,-5)
        if button[pygame.K_a]: entity.updatePos(-5,0)
        if button[pygame.K_s]: entity.updatePos(0,5)
        if button[pygame.K_d]: entity.updatePos(5,0)

