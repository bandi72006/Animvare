#Bandar Al Aish

import pygame
import math

class Species:
    def __init__(self, x, y, target, colour):
        self.x = x
        self.y = y
        self.target = target
        self.colour = colour

    def move(self, leader):
        if leader.x != self.x:
            if leader.y != self.y:
                self.target = [leader.x, leader.y]

        self.rotation = 5*(math.degrees(math.atan((self.target[1]-self.y)/(self.target[0]-self.x))))
        changeInX = math.cos(math.radians(self.rotation)) 
        changeInY = math.sin(math.radians(self.rotation))

        self.x += changeInX*0.1
        self.y += changeInY*0.1
        if self.colour == (0,0,255):
            print(self.rotation)

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), 7)