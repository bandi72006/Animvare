#Bandar Al Aish

import pygame

from species import * 

pygame.init()  
screen = pygame.display.set_mode((1280,720))  
run = True

target = [500,500]

leader = Species(1001,1001, target, (0,0,255))
species = [Species(100*i, 600, [leader.x, leader.y], (255,0,0)) for i in range(10)]

while True:  
    screen.fill((0,200,0))
    pygame.draw.circle(screen, (255,255,0), (target[0], target[1]), 7)

    for i in species:
        i.move(leader)
        i.draw(screen)
    
    leader.move(leader)
    leader.draw(screen)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    pygame.display.flip()  