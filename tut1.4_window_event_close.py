#!c:/Python27/python.exe

import pygame
import time

screen = pygame.display.set_mode((320, 200))
running = 1

#this  activates the window close X button
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0


