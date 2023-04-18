import pygame
import random

# initialised pygame
pygame.init()

# Create the screen width * height
screen = pygame.display.set_mode((800, 600))

running = True

# Title and Image game icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("fusee.png")
pygame.display.set_icon(icon)

# Player image info
playerImg = pygame.image.load("avatar.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy image info
enemyImg = pygame.image.load("alien" + str(random.randint(1, 4)) + ".png")
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40


# Inserting player
def player(x, y):
    screen.blit(playerImg, (x, y))


# Inserting Enemyplayer
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game loop
while running:
    # Screen fill, rgb values
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key pressed event condition, check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

        # Key released event condition, stop spaceship movement when key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 => 5 - 0.1
    # 5 = 5 + 0.1 Player movements
    playerX += playerX_change

    #Checking for player boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Enemy movement
    enemyX += enemyX_change
    #Checking for enemy boundaries
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    # Adding player
    player(playerX, playerY)
    # Adding enemy
    enemy(enemyX, enemyY)

    pygame.display.update()
