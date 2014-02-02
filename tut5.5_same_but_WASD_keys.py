#!c:/Python27/python.exe

#Move a single pixel around the screen without crashing against the borders

import pygame

#these are used for directions
UP = (0, -1)
UP_LEFT = (-1, -1)
UP_RIGHT = (1, -1)
DOWN = (0, 1)
DOWN_LEFT = (-1, 1)
DOWN_RIGHT = (1, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class MovingPixel:
    """ A moving pixel class. """

    def __init__(self, x, y):
        """ Creates a moving pixel. """
        self.x = x
        self.y = y
        self.hdir = 0
        self.vdir = -1

    def direction(self, dir):
        """ Chances the pixels direction. """
        self.hdir, self.vdir = dir

    def move(self):
        """ Moves the pixel. """
        self.x += self.hdir
        self.y += self.vdir

    def draw(self, surface):
        surface.set_at((self.x, self.y), (255, 255, 255))

#window dimentions
width = 640
height = 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

#create a moving pixel

pix = MovingPixel(width/2, height/2)

while running:
    pix.move()

    if pix.x <= 0 or pix.x >= width or pix.y <= 0 or pix.y >= height:
        print "CRASH"
        running = False

    screen.fill((0, 0, 0))
    pix.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pix.direction(UP)
            elif event.key == pygame.K_s:
                pix.direction(DOWN)
            elif event.key == pygame.K_a:
                pix.direction(LEFT)
            elif event.key == pygame.K_d:
                pix.direction(RIGHT)
    
    pygame.display.flip()
    clock.tick(120)





















