#!c:/Python27/python.exe

import pygame
import time

screen = pygame.display.set_mode((320, 200))
running = 1

linecolor = 0, 0, 255
point1 = 0, 0
point2 = 150, 100
point3 = 320, 0

#this  activates the window close X button
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill((0, 150, 0))
    #just leaving this here for reference as to how it usually looks
    #pygame.draw.line(screen, (0, 0, 255), (0, 0), (200, 100))
    pygame.draw.line(screen, linecolor, point1, point2)
    pygame.draw.line(screen, linecolor, point3, point2)
    pygame.draw.line(screen, linecolor, point1, point3)
    pygame.display.flip()
    #note that having back to back flips makes it flicker

