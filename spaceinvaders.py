import math
import random
import pygame
from pygame import mixer

class SpaceInvaders:
    def __init__(self,image, music, caption, icon):
         self = self
         self.screen = pygame.display.set_mode((800, 600))
         self.image = image
         self.background = None
         self.caption = caption
         self.icon = icon
         self.music = None
         self.initalizeGame()
         if music:
             self.addMusic(music)
        
    def initalizeGame(self):
        pygame.init()
        return self
        
    def setBackground(self):
        self.background = pygame.image.load(self.image)
        return self   
    
    def drawBackground(self):
        if self.background:
            self.screen.blit(self.background, (0, 0))
        return self
    
    def addMusic(self, music):
        self.music = music
        mixer.music.load(self.music)
        mixer.music.play(-1)
        
    def addCaptions(self):
        pygame.display.set_caption(self.caption)
        
    def setIcon(self):
        pygame.image.load(self.icon)
        
    def run(self):
       self.setBackground()
       self.initializePlayer()
       running = True
       while running:
        self.drawBackground()
        pygame.display.update()
        
    def initializePlayer(self):
        # Player
        playerImg = pygame.image.load('player.png')
        playerX = 370
        playerY = 480
        playerX_change = 0
        return self
        
    def initializeEnemy(self):
        # Enemy
        enemyImg = []
        enemyX = []
        enemyY = []
        enemyX_change = []
        enemyY_change = []
        num_of_enemies = 6
        for i in range(num_of_enemies):
            enemyImg.append(pygame.image.load('enemy.png'))
            enemyX.append(random.randint(0, 736))
            enemyY.append(random.randint(50, 150))
            enemyX_change.append(4)
            enemyY_change.append(40)
        return self
    
    def initializeBullet(self):
        # Bullet

        # Ready - You can't see the bullet on the screen
        # Fire - The bullet is currently moving
        bulletImg = pygame.image.load('bullet.png')
        bulletX = 0
        bulletY = 480
        bulletX_change = 0
        bulletY_change = 10
        bullet_state = "ready"
        return self
    
    
            
class Figure:
    def __init__(self, figureImg, figureX, figureY, figureX_change) -> None:
        self.figureImg = figureImg
        self.figureX = figureX
        self.figureY = figureY
        self.figureImg = figureImg

         

     

spaceInvadersGame = SpaceInvaders(image='background.png', music="background.wav", icon='ufo.png', caption='Space Invaders').run()


