#!c:/Python27/python.exe

#Move a single pixel around the screen without crashing against the borders
#5.7 we left a trail like an etch a sketch
#5.8 we're going to make it a worm and only keep a set number of the pixels
#6.1 We're going to set it so the worm can't run into itself

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

flag = 0

class MovingPixel:
    """ A moving pixel class. """

    def __init__(self, x, y):
        """ Creates a moving pixel. """
        self.x = x
        self.y = y
        self.hdir = 0
        self.vdir = -1
	#we're going to make the worm length here. This will write
	#the number of worm pixels at the starting pixel and it will
	#be populated and popped out as new pixel moves go on
	self.worm_length = 25
	self.temp_list = [width/2, height/2]
	self.matrix = []
	for nums in range(self.worm_length):
	    self.matrix.append(self.temp_list)

    def direction(self, dir):
        """ Chances the pixels direction. """
        self.hdir, self.vdir = dir

    def move(self):
        """ Moves the pixel. """
        self.x += self.hdir
        self.y += self.vdir

    def draw(self, surface):
	self.my_list = [self.x, self.y]
	#we're leaving a trail here so we're making a list of coords
	self.matrix.append(self.my_list)
	#to make the worm we'll remove one from the beginning
	self.matrix.remove(self.matrix[0])
	for coords in self.matrix:
	    surface.set_at((coords[0], coords[1]), (255, 255, 255))
	self.matrix2 = self.matrix
	#self.matrix2.remove(self.matrix[self.worm_length-2])
	#if self.matrix[int(self.worm_length-1)] in self.matrix2:
	#   flag = 1

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
            elif event.key == pygame.K_q:
                pix.direction(UP_LEFT)
            elif event.key == pygame.K_e:
                pix.direction(UP_RIGHT)
            elif event.key == pygame.K_z:
                pix.direction(DOWN_LEFT)
            elif event.key == pygame.K_c:
                pix.direction(DOWN_RIGHT)
    
    pygame.display.flip()
    clock.tick(18)





















