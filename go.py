#!c:/Python27/python.exe

#3.7b - adding actual gridlines

import pygame
import math

running = 1
width = 400 
height = 400
bgcolor = 0, 150, 0
line_color = 0, 23, 200
gridline_color = 45, 45, 45

#I had to look this up. The individual spaces between grid lines are called modules
module_width = 20

#initializing these since we're doing the redraw before they coords exist the first time
x = 0
y = 0

screen = pygame.display.set_mode((width, height))

#screen.fill was overwriting our cross hair so we had to move it outside
screen.fill(bgcolor)

#draw the gridlines (does this need to be inside the while loop?
#or the crosshairs need to be inside the lines because destroying the
#crosshairs is overwriting the gridlines

#create the grid
#FIXME there's something off with the crosshairs vs the line
for i in xrange (1, width, module_width): 
    pygame.draw.line(screen, gridline_color, (i, 1), (i, height))
    pygame.draw.line(screen, gridline_color, (1, i), (width, i))


#pygame.draw.line(screen, gridline_color, (10, 1), (10, 400))
#pygame.draw.line(screen, gridline_color, (20, 1), (20, 400))

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
	
	#we're going to divide this into 20 px grid squares.
	#this should give us 40 wide and 40 down
	x, y = event.pos
	x = int(math.ceil(x / 20.0)) 
	y = int(math.ceil(y / 20.0))

	#just printing out the coords to the console
        print "mouse at (%d, %d)" % event.pos
	print "grid square: " + str(x) + " - " + str(y)

	#we're going to draw a crosshair just for the hell of it in the
	#grid where the cursor is
	#x and y are set to the top left of the grid square we want
	#I probably could have combined below with the above stuff, but
	#this allowed me to print everything to the console to see what 
	#I was doing better
	x = (x * module_width) - module_width
	y = (y * module_width) - module_width 

	#offset the cursor location to center the crosshair in the grid box
        pygame.draw.line(screen, line_color, ((x + (module_width / 2)), y), ((x + (module_width / 2)), (y + module_width)))
	pygame.draw.line(screen, line_color, (x, (y + (module_width / 2))), ((x + module_width), (y + (module_width / 2))))

    pygame.display.flip()
    #note that having back to back flips makes it flicker

