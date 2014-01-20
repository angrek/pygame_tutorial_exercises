#!c:/Python27/python.exe

import pygame
import time

screen = pygame.display.set_mode((320, 200))
running = 1

blue = 0, 0, 255
point1 = 0, 0
point2 = 200, 100


#this  activates the window close X button
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill((0, 150, 0))
    pygame.display.flip()
    pygame.draw.line(screen, blue, point1, point2)
    #just leaving this here for reference as to how it usually looks
    #pygame.draw.line(screen, (0, 0, 255), (0, 0), (200, 100))
    pygame.display.flip()


