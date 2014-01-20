#!c:/Python27/python.exe

import pygame
import time

screen = pygame.display.set_mode((320, 200))
while 1:
    time.sleep(2)
    screen = pygame.display.set_mode((640, 480))
    time.sleep(2)
    screen = pygame.display.set_mode((320, 200))
    time.sleep(2)
