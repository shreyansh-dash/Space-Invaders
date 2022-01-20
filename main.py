import pygame
import os 
import random
import time
#initializing pygame
pygame.init()

#screen
screen= pygame.display.set_mode((800,600))

bg= pygame.image.load('spacebg.png')

#Icon creation
pygame.display.set_caption('Space Invaders')
Logo= pygame.image.load('logo.png')
pygame.display.set_icon(Logo)

#Player
playerImg = pygame.image.load("player.png")
playerX= 360
playerY= 500
playerX_change = 0
def player(X,Y):
    screen.blit(playerImg, (X, Y))


#Alien
alienImg = pygame.image.load("alien.png")
alienX= random.randint(0,800)
alienY= random.randint(50,150)
alienX_change = 0.3
alienY_change = 40

def alien(X,Y):
    screen.blit(alienImg, (X, Y))


running = True 
while running:
    
    # this will help to keep the screen color constant
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #adding keyboard keys
        if  event.type == pygame.KEYDOWN:  #pressing of key
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3  
        if  event.type == pygame.KEYUP:  #release of key
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            


# defining boundaries of  player
    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736  
# defining boundaries of alien    

    alienX += alienX_change
    
    if alienX <=0:
        alienX_change = 0.2
        alienY += alienY_change
    elif alienX >=736:
        alienX_change = - 0.2
        alienY += alienY_change
    
    player(playerX, playerY)
    alien(alienX, alienY)
    pygame.display.update()