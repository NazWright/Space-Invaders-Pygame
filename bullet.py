import pygame 


class Bullet:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect()
    
    def fire_bullet(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.image, (self.rect.x, self.rect.y))
