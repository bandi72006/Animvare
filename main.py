#Bandar Al Aish

import pygame
import random
from species import * 
from predator import *
from biologist import *

pygame.init()  
screen = pygame.display.set_mode((1280,720))  
run = True

font = pygame.font.Font("freesansbold.ttf", 32)
sanctuaryText = font.render("Sanctuary", True, (0,0,0))

target = [random.randint(0,1280), random.randint(0,720)]

leader = Species(random.randint(50,200), random.randint(550,700), target, (0,0,255))
species = [Species(random.randint(50,200), random.randint(550,700), [leader.x, leader.y], (255,0,0)) for i in range(20)]
hunters = [Predator(random.randint(1000,1200), random.randint(10,150), [leader.x, leader.y], (0,0,0)) for i in range(5)]
biologists = []

frames = 0
bGo = False
tUpdate = random.randint(100,1000)

while True:  
    screen.fill((0,120,0))
    
    frames += 1
    pygame.draw.circle(screen, (255,255,255), (target[0], target[1]), 7)

    #creates biologists after 1000 frames
    if bGo:
        if biologists == []:
            biologists = [Biologist(random.randint(50,200), random.randint(550,700), [leader.x, leader.y], (255,255,0)) for i in range(5)]

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
        else:
            bGo = True

        i.draw(screen)
    
    #Draws species' leader
    if leader.hunted == False:
        leader.move(target[0], target[1])
        leader.isHunted(hunters)
        leader.draw(screen)

    #Moves and draws hunters/predators
    for i in hunters:
        i.move(leader.x, leader.y, bGo)
        i.draw(screen)

    #Moves and draws biologists
    if bGo:
        for i in biologists:
            i.move(leader.x, leader.y)
            i.draw(screen)

    #Draws background

    pygame.draw.line(screen, (0,0,0), (0,500), (250,500), 5)
    pygame.draw.line(screen, (0,0,0), (250,500), (250,720), 5)
    screen.blit(sanctuaryText, (40,600))

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    pygame.display.flip()  