import math
import random
import pygame
from enemy import Enemy
from pygame import mixer
from player import Player


class SpaceInvaders:
    def __init__(self,image, music, caption, icon, numEnemies):
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
         self.numEnemies = numEnemies
         self.enemies = self.loadEnemies()
         pygame.font.init()
         self.font = pygame.font.Font('freesansbold.ttf', 32)
         self.scoreValue = 0;
         self.scoreText = None;
         self.initalizeGame()
        
    def initalizeGame(self):
        pygame.init()
        return self
    
    def isCollision(self, bullet, enemy):
        if bullet.rect.colliderect(enemy.rect):
            return False
        return True
    
    def drawBackground(self):
        if self.background:
            self.screen.blit(self.background, (0, 0))
        return self

    def closeGame(self):
        self.running = False
        
    def loadEnemies(self):
        enemies = []
        for i in range(self.numEnemies):
           enemies.append(Enemy("enemy.png", random.randint(0, 736), random.randint(50, 150), 4, 40))
        return enemies   
    
    def show_score(self, x, y):
        self.scoreText = self.font.render("Score : " + str(self.scoreValue), True, (255, 255, 255))
        self.screen.blit(self.scoreText, (x, y))
        
    def gameLoop(self):
        while self.running:
            self.drawBackground()
            # draw and move the player.
            self.player.move_player()
            self.player.draw_player(screen=self.screen)
            for enemy in self.enemies:
                enemy.control_enemy()
                enemy.spawn_enemy(self.screen)
                bullet = self.player.bullet
                if enemy.rect.colliderect(bullet.rect):
                    print("Collision detected!", bullet.rect, enemy.rect)
                    # respawn
                    enemy.playerX = random.randint(0, 736)
                    enemy.playerY = random.randint(50, 150)
                    # points
                    self.scoreValue += 10
            self.show_score(10,10)        
            self.handleEvents()
            # Bullet Movement
            bullet = self.player.bullet
            if bullet.bulletY <= 0:
                bullet.bulletY = 480
                bullet.bullet_state = "ready"
                bullet.rect.y = bullet.bulletY

            if bullet.bullet_state == "fire":
                bullet.fire_bullet(self.screen, self.player.playerX, bullet.bulletY)
                bullet.bulletY -= bullet.bulletY_change
                bullet.rect.y = bullet.bulletY
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

