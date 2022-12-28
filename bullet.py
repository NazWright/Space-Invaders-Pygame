import pygame 


class Bullet:
    def __init__(self) -> None:
        self.bulletImg = pygame.image.load('bullet.png')
        self.bulletX = 0
        self.bulletY = 480
        self.bulletX_change = 0
        self.bulletY_change = 10
        self.bullet_state = "ready"
        self.bulletSound = None;
    
    def fire_bullet(self, screen, x, y):
        self.bullet_state = "fire"
        screen.blit(self.bulletImg, (x + 16, y + 10))