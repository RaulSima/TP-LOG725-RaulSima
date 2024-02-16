import pygame

class Exit():
  def __init__(self, x, y):
    pygame.font.init()
    self.pos_x = x
    self.pos_y = y
    self.color = (220, 199, 199)
    
  def draw(self, screen):
    pygame.draw.rect(screen, self.color, (self.pos_x, self.pos_y, 96, 96))
    my_font = pygame.font.SysFont('Cascadia code', 30)
    text_surface = my_font.render('Sortie', False, (255, 0, 0))
    screen.blit(text_surface, (self.pos_x + 18, self.pos_y + 37))