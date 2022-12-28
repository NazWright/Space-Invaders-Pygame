import random
from player import Player

class Enemy(Player):
    def __init__(self, enemyImg, enemyX, enemyY, enemyX_change, enemyY_change):
        super().__init__(enemyImg, enemyX, enemyY, enemyX_change)
        # additional initialization code for the Enemy class
        self.playerY_change = enemyY_change
    
    def spawn_enemy(self, screen):
        screen.blit(self.playerImg, (self.playerX, self.playerY))
        
    def control_enemy(self):
        self.playerX += self.playerX_change
        if self.playerX <= 0:
            self.playerX_change = 4
            self.playerY += self.playerY_change
        elif self.playerX >= 736:
            self.playerX_change = -4
            self.playerY += self.playerY_change
        self.rect.x = self.playerX
        self.rect.y = self.playerY

