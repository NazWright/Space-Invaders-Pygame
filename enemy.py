import random
from player import Player

class Enemy(Player):
    def __init__(self, enemyImg, enemyX, enemyY, enemyX_change, enemyY_change):
        super().__init__(enemyImg, enemyX, enemyY, enemyX_change)
        # additional initialization code for the Enemy class
        self.playerY_change = enemyY_change
    
    def spawn_enemy(self, screen):
        screen.blit(self.playerImg, (self.playerX, self.playerY))

