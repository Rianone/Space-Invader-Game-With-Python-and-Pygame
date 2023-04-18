import pygame

#initialised pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

running = True

#Title and Image game icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("fusee.png")
pygame.display.set_icon(icon)

#Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Screen fill, rgb values
    screen.fill((0, 0, 0))
    pygame.display.update()