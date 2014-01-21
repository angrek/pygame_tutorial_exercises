#!c:/Python27/python.exe

import pygame
import math

running = 1
width = 400 
height = 400
bgcolor = 0, 150, 0
line_color = 0, 23, 200
gridline_color = 45, 45, 45

#initializing these since we're doing the redraw before they coords exist the first time
x = 0
y = 0

screen = pygame.display.set_mode((width, height))

#screen.fill was overwriting our cross hair so we had to move it outside
screen.fill(bgcolor)

#draw the gridlines (does this need to be inside the while loop?
#or the crosshairs need to be inside the lines because destroying the
#crosshairs is overwriting the gridlines

pygame.draw.line(screen, gridline_color, (10, 1), (10, 400))
pygame.draw.line(screen, gridline_color, (20, 1), (20, 400))

while running:
    #this  activates the window close X button
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEBUTTONDOWN:

	#ok, we're just copying the previous line draw and changing the color
	#to the background color to destroy the previous crosshairs 
        pygame.draw.line(screen, bgcolor, ((x + 5), y), ((x + 5), (y + 10)))
	pygame.draw.line(screen, bgcolor, (x, (y + 5)), ((x + 10), (y + 5)))
	
	#we're going to divide this into 10 px grid squares.
	#this should give us 40 wide and 40 down
	x, y = event.pos
	x = int(math.ceil(x / 10.0)) 
	y = int(math.ceil(y / 10.0))

	#just printing out the coords to the console
        print "mouse at (%d, %d)" % event.pos
	print "grid square: " + str(x) + " - " + str(y)

	#we're going to draw a crosshair just for the hell of it in the
	#grid where the cursor is
	#x and y are set to the top left of the grid square we want
	#I probably could have combined below with the above stuff, but
	#this allowed me to print everything to the console to see what 
	#I was doing better
	x = (x * 10) - 10
	y = (y * 10) - 10

	#offset the cursor location to center the crosshair in the grid box
        pygame.draw.line(screen, line_color, ((x + 5), y), ((x + 5), (y + 10)))
	pygame.draw.line(screen, line_color, (x, (y + 5)), ((x + 10), (y + 5)))

    pygame.display.flip()
    #note that having back to back flips makes it flicker

