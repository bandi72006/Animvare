#Bandar Al Aish

import pygame
import random
from species import * 

pygame.init()  
screen = pygame.display.set_mode((1280,720))  
run = True

target = [random.randint(0,1280), random.randint(0,720)]

leader = Species(random.randint(0,1280), random.randint(0,720), target, (0,0,255))
species = [Species(random.randint(0,1280), random.randint(0,720), [leader.x, leader.y], (255,0,0)) for i in range(10)]

frames = 0

while True:  
    screen.fill((0,200,0))
    
    frames += 1
    pygame.draw.circle(screen, (255,255,0), (target[0], target[1]), 7)

    if frames > 2000:
        target = [random.randint(0,1280), random.randint(0,720)]
        frames = 0

    for i in species:
        i.move(leader.x, leader.y)
        i.draw(screen)
    
    leader.move(target[0], target[1])
    leader.draw(screen)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    pygame.display.flip()  