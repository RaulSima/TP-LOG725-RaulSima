import pygame
from src.projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./assets/tank.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (200, 100)
        self.speed = 6
        self.redBullets = 10
        self.blueBullets = 10
        self.greenBullets = 10
        self.angle = 0
        self.projectiles = pygame.sprite.Group()
        self.cooldown = 10
        self.attacked = False

    def update(self):
        if(self.cooldown > 0 and self.attacked == True):
            self.cooldown -= 1
        else:
            self.cooldown = 10
            self.attacked = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if(self.angle != 180):
                self. image = pygame.transform.rotate(self.image, 180 - self.angle)
                self.angle = 180
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            if(self.angle != 0):
                self. image = pygame.transform.rotate(self.image, 0 - self.angle)
                self.angle = 0
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            if(self.angle != 90):
                self. image = pygame.transform.rotate(self.image, 90 - self.angle)
                self.angle = 90
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            if(self.angle != 270):
                self. image = pygame.transform.rotate(self.image, 270 - self.angle)
                self.angle = 270
            self.rect.y += self.speed
        if keys[pygame.K_z]:
            if(self.attacked == False and self.redBullets > 0):
                self.shoot('z')
                self.redBullets -= 1
                self.attacked = True
        if keys[pygame.K_x]:
            if(self.attacked == False and self.greenBullets > 0):
                self.shoot('x')
                self.greenBullets -= 1
                self.attacked = True
        if keys[pygame.K_c]:
            if(self.attacked == False and self.blueBullets > 0):
                self.shoot('c')
                self.blueBullets -= 1
                self.attacked = True
            
    def shoot(self, key):
        s_x = 0
        s_y = 0
        if(self.angle == 0):
            s_x = self.speed
            s_y = 0
        elif(self.angle == 90):
            s_x = 0
            s_y = -self.speed
        elif(self.angle == 180):
            s_x = -self.speed
            s_y = 0
        elif(self.angle == 270):
            s_x = 0
            s_y = self.speed
            
        if(key == 'z'):
            self.projectiles.add(Projectile(self.rect.x + (self.rect.w / 2), self.rect.y + (self.rect.h / 2), s_x, s_y, (255, 0, 0)))
        if(key == 'x'):
            self.projectiles.add(Projectile(self.rect.x + (self.rect.w / 2), self.rect.y + (self.rect.h / 2), s_x, s_y, (0, 255, 0)))
        if(key == 'c'):
            self.projectiles.add(Projectile(self.rect.x + (self.rect.w / 2), self.rect.y + (self.rect.h / 2), s_x, s_y, (0, 0, 255)))