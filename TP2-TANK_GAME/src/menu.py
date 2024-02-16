import pygame

class Menu():
  def __init__(self, player):
    pygame.font.init()
    self.redBullets = player.redBullets
    self.blueBullets = player.blueBullets
    self.greenBullets = player.greenBullets
    
  
  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 96 * 2 , 570))
    
    # drawing the number of bullets per color
    my_font = pygame.font.SysFont('Comic Sans MS', 70)
    
    # red bullets
    text_surface = my_font.render(str(self.redBullets), False, (0, 0, 0))
    screen.blit(text_surface, (0,-20))
    text_surface = my_font.render('R', False, (255, 0, 0))
    screen.blit(text_surface, (100,-20))
    
    # green bullets
    text_surface = my_font.render(str(self.greenBullets), False, (0, 0, 0))
    screen.blit(text_surface, (0,40))
    text_surface = my_font.render('G', False, (0, 255, 0))
    screen.blit(text_surface, (100,40))
    
    # blue bullets
    text_surface = my_font.render(str(self.blueBullets), False, (0, 0, 0))
    screen.blit(text_surface, (0,100))
    text_surface = my_font.render('B', False, (0, 0, 255))
    screen.blit(text_surface, (100,100))
    
  def update(self, player):
    self.redBullets = player.redBullets
    self.blueBullets = player.blueBullets
    self.greenBullets = player.greenBullets