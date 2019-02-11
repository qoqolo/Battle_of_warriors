import pygame,os

class Land(pygame.sprite.Sprite):
    def __init__(self, x, y,group):
        super().__init__(group)
        self.x = x
        self.y = y
        self.image = pygame.Surface([1600,50])
        self.image.fill(pygame.Color('green'))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)
