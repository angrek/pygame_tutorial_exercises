#!c:/Python27/python.exe

#note, this prints out the grid stuff on the console. You won't
# see anything in the window that's created.

import pygame
import math

running = 1
width = 400 
height = 400
bgcolor = 0, 0, 0

screen = pygame.display.set_mode((width, height))


while running:
    #this  activates the window close X button
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEBUTTONDOWN:
	#we're going to divide this into 10 px grid squares.
	#this should give us 40 wide and 40 down
	x, y = event.pos
	x = int(math.ceil(x / 10.0)) 
	y = int(math.ceil(y / 10.0))
        

        print "mouse at (%d, %d)" % event.pos
	print "grid square: " + str(x) + " - " + str(y)

    screen.fill(bgcolor)


    pygame.display.flip()
    #note that having back to back flips makes it flicker

