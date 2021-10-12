#Bandar Al Aish

import pygame
import random
from species import * 
from predator import *

pygame.init()  
screen = pygame.display.set_mode((1280,720))  
run = True

target = [random.randint(0,1280), random.randint(0,720)]

leader = Species(random.randint(0,1280), random.randint(0,720), target, (0,0,255))
species = [Species(random.randint(0,1280), random.randint(0,720), [leader.x, leader.y], (255,0,0)) for i in range(20)]
hunters = [Predator(random.randint(0,1280), random.randint(0,720), [leader.x, leader.y], (0,0,0)) for i in range(5)]

frames = 0
tUpdate = random.randint(100,1000)

while True:  
    screen.fill((0,120,0))
    
    frames += 1
    pygame.draw.circle(screen, (255,255,0), (target[0], target[1]), 7)

    #Moves species' target randomly so they dynamically move
    if frames > tUpdate:
        target = [random.randint(0,1280), random.randint(0,720)]
        frames = 0
        tUpdate = random.randint(100,1000)

    #Moves and draws species
    for i in species:
        if i.hunted == False:
            i.move(leader.x, leader.y)
            i.isHunted(hunters)
        i.draw(screen)

    #Moves and draws hunters/predators
    for i in hunters:
        i.move(leader.x, leader.y)
        i.draw(screen)
    
    #Draws species' leader
    if leader.hunted == False:
        leader.move(target[0], target[1])
        leader.isHunted(hunters)
        leader.draw(screen)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    pygame.display.flip()  