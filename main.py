import pygame
import random
import math

# initialised pygame
pygame.init()

# Create the screen width * height
screen = pygame.display.set_mode((800, 600))

running = True

# Title and Image game icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("fusee.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("background.png")

# Player image info
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy image info
enemyImg = pygame.image.load("alien" + str(random.randint(1, 4)) + ".png")
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 2
enemyY_change = 40

# Bullet image info
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
# Ready state - You can't see bullet onscreen
# Fire - Bullet currently moving
bullet_state = "ready"


# Inserting player
def player(x, y):
    screen.blit(playerImg, (x, y))


# Inserting Enemy player
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Firing bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

#Find wheter there is collision btw the bullet and the enemy
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game loop
while running:
    # Screen fill, rgb values
    screen.fill((0, 0, 0))

    # BG image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key pressed event condition, check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    #Getting the current X coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        # Key released event condition, stop spaceship movement when key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 => 5 - 0.1
    # 5 = 5 + 0.1 Player movements
    playerX += playerX_change

    # Checking for player boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change
    # Checking for enemy boundaries
    if enemyX <= 0:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -2
        enemyY += enemyY_change

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Adding player
    player(playerX, playerY)
    # Adding enemy
    enemy(enemyX, enemyY)

    pygame.display.update()
