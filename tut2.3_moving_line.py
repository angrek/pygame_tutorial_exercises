#!c:/Python27/python.exe

import pygame

y = 0
dir = 1
running = 1
width = 320
height = 200
bgcolor = 0, 150, 0
linecolor = 0, 0, 255
point1 = 0, 0
point2 = 150, 100
point3 = 320, 0

screen = pygame.display.set_mode((width, height))

while running:
    #this  activates the window close X button
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    screen.fill(bgcolor)
    #just leaving this here for reference as to how it usually looks
    #pygame.draw.line(screen, (0, 0, 255), (0, 0), (200, 100))
    pygame.draw.line(screen, linecolor, (0, y), (width-1, 7))

    y += dir
    if y == 0 or y == height-1: dir *= -1

    pygame.display.flip()
    #note that having back to back flips makes it flicker

