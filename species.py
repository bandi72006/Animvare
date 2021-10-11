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

        self.rotation = 10*(math.degrees(math.atan((self.target[1]-self.y)/(self.target[0]-self.x))))
        changeInX = math.cos(math.radians(self.rotation)) 
        changeInY = math.sin(math.radians(self.rotation))

        self.x += changeInX*0.05
        self.y += changeInY*0.05
        if self.colour == (0,0,255):
            print(self.rotation)

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