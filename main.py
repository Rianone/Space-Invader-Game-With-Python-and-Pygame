import pygame

#initialised pygame
pygame.init()

#Create the screen width * height
screen = pygame.display.set_mode((800,600))

running = True

#Title and Image game icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("fusee.png")
pygame.display.set_icon(icon)

#Player image info
playerImg = pygame.image.load("avatar.png")
playerX = 370
playerY = 480

#Inserting player
def player():
    screen.blit(playerImg, (playerX, playerY))

#Game loop
while running:
    #Screen fill, rgb values
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()