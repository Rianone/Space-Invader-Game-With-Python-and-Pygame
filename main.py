import pygame

#initialised pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

running = True

#Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False