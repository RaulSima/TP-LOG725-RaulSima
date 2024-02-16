import pygame

class Projectile(pygame.sprite.Sprite):
  def __init__(self, x, y, s_x, s_y, color):
    super().__init__()
    self.rayon = 10
    self.image = pygame.image.load('./assets/tank.png') #hack to have a sprite rect but we wont draw the image
    self.rect = self.image.get_rect()
    self.rect.x = x - self.rayon
    self.rect.y = y - self.rayon
    self.rect.w = self.rayon*2
    self.rect.h = self.rayon*2
    self.speed_x = s_x
    self.speed_y = s_y
    self.color = color
    
  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (self.rect.x, self.rect.y), self.rayon, 0)
    
  def update(self):
    self.rect.x += self.speed_x
    self.rect.y += self.speed_y