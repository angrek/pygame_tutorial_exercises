#!c:/Python27/python.exe

import pygame

#this exercise is to convert the nomal position to cartesian coords

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
    elif event.type == pygame.MOUSEMOTION:
	#I have no idea what I'm doing....
	#ok, I got it close within one number
	print "test"
        x, y = event.pos
        if x >= (width / 2):
	    x -= (width / 2)
	elif x == (width / 2):
	    x = 0
        else:
	    x = ((width / 2) - x)
	    x = -abs(x)
	if y >= (height / 2):
	    y -= (height / 2)
	    y = -abs(y)
	elif y == (height / 2):
            y = 0
        else:
	    y = ((height / 2) - y)

	    
        print "mouse at (%d, %d)" % event.pos
	print "cartesian -> " + str(x) + " - " + str(y)


    screen.fill(bgcolor)


    pygame.display.flip()

