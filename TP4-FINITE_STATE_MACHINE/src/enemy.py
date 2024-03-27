import pygame
import time
import math


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # l'état initiale
        self.state = 0
        self.is_hit = False
        self.current_sprite = pygame.image.load('./assets/enemy.png')
        self.rect = self.current_sprite.get_rect()
        # la position initiale est au centre de l'écran
        self.starting_position = (400, 100)
        self.behind_left_rock_position = (150, 100)
        self.behind_right_rock_position = (600, 100)
        self.rect.center = self.starting_position
        self.speed = 2
        self.backoff_time = 1

    # Tip : pour calculer la distance (x, y) entre l'ennemi et les projectiles, calculez la différence entre les coordonnées. Par exemple : (position x du sprite 1) - (position x du sprite 2)
    def compute_distance(self, bullet):
        distance_x = bullet.rect.center[0] - self.rect.center[0]
        distance_y = bullet.rect.center[1] - self.rect.center[1] 
        return math.sqrt(distance_x*distance_x + distance_y*distance_y)
    
    def compute_horizontal_distance(self, bullet) :
        return self.rect.center[0] - bullet.rect.center[0]

    # Utilisez les règles dans la machine à états de réference comme base pour construire la structure de if/else nécessaire
    def update(self, bullets):
        if (not bullets) :
            if(self.is_hit) :
                time.sleep(self.backoff_time)
                self.is_hit = False
            self.state = 0
        previous_condition = None
        for bullet in bullets:
            condition_de_changement = self.compute_distance(bullet)
            if condition_de_changement > 0:
                if(self.compute_horizontal_distance(bullet) <= 0):
                    self.state = 1
                else :
                    self.state = 2
        # print(self.state)
        match self.state:
            case 0:
                self.walk_towards(self.starting_position)
            case 1:
                self.walk_towards(self.behind_left_rock_position)
            case 2:
                self.walk_towards(self.behind_right_rock_position)
                
    def walk_towards(self, target_pos):
        distance_x = target_pos[0] - self.rect.center[0]
        distance_y = target_pos[1] - self.rect.center[1]
        # print(distance_x)
        
        if(distance_x != 0):
            self.rect.x += distance_x / abs(distance_x) * self.speed
        
        if(distance_y != 0):
            self.rect.y += distance_y / abs(distance_y) * self.speed
        pass
