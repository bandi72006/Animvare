#Bandar Al Aish

import pygame
import math
import random

class Biologist:
    def __init__(self, x, y, target, colour):
        self.x = x
        self.y = y
        self.target = target
        self.colour = colour
        self.hunted = False

    def move(self, xTar, yTar):

        self.target = [xTar, yTar]
        try:
            self.rotation = random.randint(-10,10)+20*(math.degrees(math.atan((self.target[1]-self.y)/(self.target[0]-self.x))))
        except:
            pass

        changeInX = math.cos(math.radians(self.rotation)) 
        changeInY = math.sin(math.radians(self.rotation))

        self.x += changeInX*random.random()
        self.y += changeInY*random.random()

        if self.x > 1280:
            self.x = 1280
        if self.x < 0:
            self.x = 0

        if self.y > 720:
            self.y = 720
        if self.y < 0:
            self.y = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), 7)