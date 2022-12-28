import math
import random
import pygame
from pygame import mixer
from player import Player


class SpaceInvaders:
    def __init__(self,image, music, caption, icon):
         self = self
         self.screen = pygame.display.set_mode((800, 600))
         self.image = image
         self.background = None
         self.caption = caption
         self.icon = icon
         self.music = None
         self.player = Player(playerImg='player.png', playerX=370, playerY=480, playerX_change=0)
         self.background = pygame.image.load(image)
         self.running = False
         self.initalizeGame()
        
    def initalizeGame(self):
        pygame.init()
        return self
    
    def drawBackground(self):
        if self.background:
            self.screen.blit(self.background, (0, 0))
        return self

    def closeGame(self):
        self.running = False
        
    def gameLoop(self):
        while self.running:
            self.drawBackground()
            # draw and move the player.
            self.player.move_player()
            self.player.draw_player(screen=self.screen)
            self.handleEvents()
            # Bullet Movement
            bullet = self.player.bullet
            if bullet.bulletY <= 0:
                bullet.bulletY = 480
                bullet.bullet_state = "ready"

            if bullet.bullet_state == "fire":
                bullet.fire_bullet(self.screen, self.player.playerX, bullet.bulletY)
                bullet.bulletY -= bullet.bulletY_change
            pygame.display.update()   
    
    def handleEvents(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.closeGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.move_left()
                    if event.key == pygame.K_RIGHT:
                        self.player.move_right()
                    if event.key == pygame.K_SPACE:
                        if self.player.bullet.bullet_state is "ready":
                            self.bulletSound = mixer.Sound("laser.wav")
                            self.bulletSound.play()
                            # Get the current x cordinate of the spaceship
                            bulletX = self.player.playerX
                            self.player.bullet.fire_bullet(self.screen, bulletX, self.player.bullet.bulletY)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.player.stop()
                        
    def run(self):
       self.running = True
       self.gameLoop()

