#!c:/Python27/python.exe

#plot random pixels on the screen

import pygame
import random

# Window dimensions
width = 640
height = 400
bgcolor = 0, 150, 0

#position
x = width / 2
y = height / 2

#direction
dir_x = 0
dir_y = -1

screen = pygame.display.set_mode((width, height))
screen.fill(bgcolor)
clock = pygame.time.Clock()
running = True

while running:
    x += dir_x
    y += dir_y

    if x <= 0 or x >=width or y <= 0 or y >=height:
	print "CRASH!"
	running = False
    screen.fill((0, 0, 0))
    screen.set_at((x, y), (255, 255, 255))


    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    running = False
	elif event.type == pygame.KEYDOWN:
	    if event.key == pygame.K_UP:
		dir_x = 0
		dir_y = -1
	    elif event.key == pygame.K_DOWN:
		dir_x = 0
		dir_y = 1
	    elif event.key == pygame.K_LEFT:
		dir_x = -1
		dir_y = 0
	    elif event.key == pygame.K_RIGHT:
		dir_x = 1
		dir_y = 0


    pygame.display.flip()
    clock.tick(240)



