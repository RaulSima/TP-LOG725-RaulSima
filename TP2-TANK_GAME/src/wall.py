import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.type = type
        self.image = pygame.image.load('./assets/' + type + '.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
