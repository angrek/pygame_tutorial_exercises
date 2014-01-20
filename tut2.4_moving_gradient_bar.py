#!c:/Python27/python.exe

import pygame

y = 0
dir = 1
running = 1
width = 800 
height = 600
bgcolor = 0, 0, 0
barheight = 124

screen = pygame.display.set_mode((width, height))

barcolor = []
for i in range(1, 63):
    barcolor.append((0, 0, i*4))
for i in range(1, 63):
    barcolor.append((0, 0, 255 - i * 4))

while running:
    #this  activates the window close X button
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    screen.fill(bgcolor)

    for i in range(0, barheight):
	#Ok, so this isn't really a bar, it's more of a pie shape from one point
	#on the left and drawing to the points in the range of i
	#slightly misleading, but that's what the tutorial called it so...
        pygame.draw.line(screen, barcolor[i], (0, y+1), (799, y+i))

    #this makes the whole thing go up and down

    y += dir
    if y + barheight > 599 or y < 0:
        dir *= -1


    pygame.display.flip()
    #note that having back to back flips makes it flicker

