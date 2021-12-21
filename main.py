import pygame
from pygame import mixer
import random
import math


# Initialisieren
pygame.init()



# Display
screen = pygame.display.set_mode((840,900))
pygame.display.set_caption("StreetRacer")
icon = pygame.image.load('resources/imageicon.jpg')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


# Background
ground_Y = 0
background = pygame.image.load('resources/streetlong.png')

# Background sound
mixer.music.load('resources/music.mp3')
mixer.music.play(-1)

# Player
playerImg = pygame.image.load('resources/mclaren.png')
playerX = 560
playerY = 550
playerY_change = 0
playerX_change = 0

# Variables
btc_value = 0
leben = 3
strecke = 0
font = pygame.font.Font('freesansbold.ttf',20)
font2 = pygame.font.Font('freesansbold.ttf',76)

textX = 20
textY = 60

game_speed = 5
enemy1_speed = 6
enemy3_speed = 3
enemy4_speed = 3


# Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemys = 1

for i in range (number_of_enemys):
    # Enemy one (right side)
    enemyImg.append(pygame.image.load('resources/mclaren2.png'))
    enemyX.append(random.randint(620, 650))
    enemyY.append(-280)
    enemyX_change = 4
    enemyY_change = 10


# Enemy two (left side)
enemy2Img = pygame.image.load('resources/auto2.png')
enemy2X = random.randint(60, 300)
enemy2Y = -250

enemy3Img = pygame.image.load('resources/mclaren2.png')
enemy3X = 420
enemy3Y = 1000

#enemy4 test
enemy4Img = pygame.image.load('resources/auto1.png')
enemy4X = random.randint(620, 650)
enemy4Y = -280


# Game wall (invisible)
left_wall = pygame.draw.rect(screen, (0,0,0),(0,0,100,900),0)
right_wall = pygame.draw.rect(screen, (0,0,0),(825,0,50,900),0)
top_wall = pygame.draw.rect(screen, (0,0,0), (0,0,900,1))
bottom_wall = pygame.draw.rect(screen, (0,0,0), (0,850,840,20))

# Bitcoin
btcImg = pygame.image.load('resources/bitcoin.png')
btcX = random.randint(60,650)
btcY = -100

# functions
#player and enemys
def player(x,y):
    screen.blit(playerImg,(x,y))

#def enemy(x,y,i):
    #screen.blit(enemyImg[i], (x,y))

def enemy2(x,y):
    screen.blit(enemy2Img, (x,y))

def enemy3(x,y):
    screen.blit(enemy3Img, (x,y))

def enemy4(x,y):
    screen.blit(enemy4Img, (x,y))

#items
def btc(x,y):
    screen.blit(btcImg, (x,y))


# Collisions
def collission(enemyX2, enemyY2, playerX,playerY):
    distance = math.sqrt((math.pow(enemy2X - playerX, 2)) + (math.pow(enemy2Y - playerY, 2)))
    if distance <= 100:
        return True
    else:
        return False

def collision_right(enemyX, enemyY, playerX, playerY):
    distance2 = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - playerY, 2)))
    if distance2 <= 100:
        return True
    else:
        return False

def collission3(enemyX2, enemyY2, playerX,playerY):
    distance = math.sqrt((math.pow(enemy3X - playerX, 2)) + (math.pow(enemy3Y - playerY, 2)))
    if distance <= 100:
        return True
    else:
        return False

def collision4(enemy4X, enemy4Y, playerX, playerY):
    distance = math.sqrt((math.pow(enemy4X - playerX, 2)) + (math.pow(enemy4Y - playerY, 2)))
    if distance <= 100:
        return True
    else:
        return False



def collision_bitcoin(btcX, btcY, playerX, playerY):
    distance_btc = math.sqrt((math.pow(btcX - playerX, 2)) + (math.pow(btcY - playerY, 2)))
    if distance_btc <= 90:
        return True
    else:
        return False


# Point system
def score():
    global strecke, game_speed, enemy1_speed, enemy3Y, enemy4_speed
    strecke += 1
    #print(strecke)
    #if strecke % 100 == 0:
        #game_speed += 0.3
        #enemy1_speed += 0.4
        #enemy3Y -= 0.5
        #enemy4_speed += 0.5

    if strecke % 200 == 0:
        game_speed += 0.3
        enemy1_speed += 0.4
        enemy3Y -= 0.7
        enemy4_speed += 0.5



    # training 17:30 kura

    text = font.render("Meter: " + str(strecke), True,(0,0,255))
    textRect = text.get_rect()
    textRect.center = (60,29)
    screen.blit(text, textRect)

#game over
def game_over():
    print("gamer over, loser!")
    over_text = font2.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (195,420))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False
    playerrect = pygame.Rect(playerX,playerY,200,80)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and not playerrect.colliderect(right_wall):
        playerX  += 8
    if pressed[pygame.K_LEFT] and not playerrect.colliderect(left_wall):
        playerX -= 8
    if pressed[pygame.K_UP] and not playerrect.colliderect(top_wall):
        playerY -= 7
    if pressed[pygame.K_DOWN] and not playerrect.colliderect(bottom_wall):
        playerY += 5

    playerX += playerX_change

    # Enemy1 (right) moevement
    #enemyY[i] += 3
    #for i in range(number_of_enemys):
        #enemyY[i] += 3
        #if enemyX[i] >= 500 and not enemyX[i] >= 620:
            #enemyX[i] +=0.2

        #elif enemyX[i] <= 500 and not enemyX[i] <= 400:
            #enemyX[i] -= 0.2


    enemy2Y += enemy1_speed
    enemy3Y -= enemy3_speed
    enemy4Y += enemy4_speed
    btcY += 6


    # Collision
    crash = collission(enemy2X, enemy2Y,playerX,playerY)
    crash_right = collision_right(enemyX[i],enemyY[i],playerX,playerY)
    crash3 = collission3(enemy3X, enemy3Y, playerX, playerY)
    crash4 = collision4(enemy4X, enemy4Y, playerX, playerY)


    # Collision bitcoin
    crash_btc = collision_bitcoin(btcX, btcY, playerX,playerY)
    score()

    # left side
    if crash:
        crash_sound = mixer.Sound('resources/soundcrash.mp3')
        crash_sound.play()
        print("crash left")
        enemy2X = random.randint(60, 300)
        leben -= 1
        enemy2Y = -250
        print("leben = ",leben)
        #if leben == 0:
            #game_over()
    # enemy left
    if enemy2Y > 1000:
        print("spawn left")
        enemy2X = random.randint(60, 300)
        enemy2Y = -250

    # right side
    #if crash_right:
        #print("crash right")
        #enemyX[i] = random.randint(620, 650)
        #enemyY[i] = - 280
        #leben -= 1
        #print("leben = ",leben)

    if enemyY[i] >= 1000:
        enemyX[i] = random.randint(620, 650)
        enemyY[i] = - 280

    if crash3:
        crash_sound = mixer.Sound('resources/soundcrash.mp3')
        crash_sound.play()
        enemy3X = 420
        enemy3Y = 1000
        leben -= 1
        print("leben = ",leben)

    if enemy3Y < -600:
        enemy3X = 420
        enemy3Y = 1000
        print("spawn right")

    if enemy4Y >= 1000:
        enemy4X = random.randint(620, 650)
        enemy4Y = -320
    if crash4:
        crash_sound = mixer.Sound('resources/soundcrash.mp3')
        crash_sound.play()
        enemy4X = random.randint(620, 650)
        enemy4Y = -320
        leben -= 1
        print("leben = ", leben)
        print("crash right")


    # Draw
    screen.fill((255, 255, 255))
    ground_Y += game_speed

    #ground_Y += 5
    screen.blit(background, (0, ground_Y))
    screen.blit(background, (0, -900 + ground_Y ))

    if ground_Y >= 900:
        ground_Y = 0



    # Draw
    screen.blit(playerImg,(playerX,playerY))
    #enemy(enemyX[i], enemyY[i],i)
    enemy2(enemy2X, enemy2Y)
    enemy3(enemy3X, enemy3Y)
    enemy4(enemy4X, enemy4Y)
    btc(btcX, btcY)


    # Bitcoin movement und Draw score
    score_btc = font.render("Bitcoin: " + str(btc_value), True, (0, 0, 255))
    leben_score = font.render('Leben = '+str(leben), True,(0,0,255))


    # call game over funktion
    if leben == 0:

        # game over items, enemies and plaxyer
        enemy2Y = 2000
        enemy4Y = 2000
        enemy3Y = 2000
        btcY = 2000
        playerX = 10000
        game_over()

    # bitcoin movement
    if crash_btc:
        coin_sound = mixer.Sound('resources/mariosound.mp3')
        coin_sound.play()
        btc_value += 1
        print("btc eingesammelt")
        btcX = random.randint(60, 650)
        btcY = -2000
    if btcY >= 1000:
        btcX = random.randint(60, 650)
        btcY = -2000

    # gui top left
    rechteck = pygame.draw.rect(screen, (0, 0, 255), (0, 0, 125, 100), 6)
    filled = 0
    rechteck = pygame.draw.rect(screen, (100, 100, 100), (0, 0, 125, 100), filled)

    #draw the rest
    screen.blit(score_btc, (10, 45))
    screen.blit(leben_score, (10, 70))
    score()
    filled = 0


    pygame.display.update()
    clock.tick(300)
