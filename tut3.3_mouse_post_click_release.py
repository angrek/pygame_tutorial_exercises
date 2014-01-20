#!c:/Python27/python.exe

import pygame

running = 1
width = 640 
height = 400
bgcolor = 0, 0, 0

screen = pygame.display.set_mode((width, height))


while running:
    #this  activates the window close X button
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEBUTTONUP:
        print "mouse at (%d, %d)" % event.pos


    screen.fill(bgcolor)


    pygame.display.flip()
    #note that having back to back flips makes it flicker

