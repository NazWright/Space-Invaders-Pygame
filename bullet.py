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
        self.rect = self.bulletImg.get_rect()
        self.rect.x = self.bulletX
        self.rect.y = self.bulletY

    
    def fire_bullet(self, screen, x, y):
        self.bullet_state = "fire"
        screen.blit(self.bulletImg, (x + 16, y + 10))