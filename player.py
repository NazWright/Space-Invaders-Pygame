import pygame
from pygame import mixer
from bullet import Bullet

class Player:
    def __init__(self, playerImg, playerX, playerY, playerX_change) -> None:
        self.playerImg = pygame.image.load(playerImg)
        self.playerX = playerX
        self.playerY = playerY
        self.playerX_change = playerX_change
        self.bullet = Bullet()
    
    def draw_player(self, screen):
        screen.blit(self.playerImg, (self.playerX, self.playerY))
        
    def move_player(self):
        self.playerX += self.playerX_change
        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 736:
            self.playerX = 736
            
    def move_right(self):
        self.playerX_change = 5

    def move_left(self):
        self.playerX_change = -5
        
    def stop(self):
        self.playerX_change = 0
        
    
        