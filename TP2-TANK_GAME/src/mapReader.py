from csv import reader
import pygame
from src.wall import Wall
from src.groundAmmo import GroundAmmo

def readWallMap(path):
  size = 96
  startingX = size * 2
  walls = pygame.sprite.Group()
  with open(path) as level_map:
      layout = reader(level_map, delimiter = ',')
      i = 0
      for row in layout:
        j = 0
        for col in row:
          if(col == '1'):
            walls.add(Wall(startingX + size * j, size * i, 'wall'))
          elif(col == '2'):
            walls.add(Wall(startingX + size * j, size * i, 'red'))
          elif(col == '3'):
            walls.add(Wall(startingX + size * j, size * i, 'blue'))
          elif(col == '4'):
            walls.add(Wall(startingX + size * j, size * i, 'green'))
          j += 1
        i += 1
      return walls
      
def readFloorMap(path):
  size = 96
  startingX = size * 2
  floors = pygame.sprite.Group()
  with open(path) as level_map:
      layout = reader(level_map, delimiter = ',')
      i = 0
      for row in layout:
        j = 0
        for col in row:
          if(col == '1'):
            floors.add(Wall(startingX + size * j, size * i, 'floor'))
          j += 1
        i += 1
      return floors
    
def readAmmoMap(path):
  size = 96
  startingX = size * 2
  ammos = pygame.sprite.Group()
  with open(path) as level_map:
      layout = reader(level_map, delimiter = ',')
      i = 0
      for row in layout:
        j = 0
        for col in row:
          if(col == '1'):
            ammos.add(GroundAmmo(startingX + size * j + size/2, size * i + size/2, (255, 0, 0)))
          elif(col == '2'):
            ammos.add(GroundAmmo(startingX + size * j + size/2, size * i + size/2, (0, 255, 0)))
          elif(col == '3'):
            ammos.add(GroundAmmo(startingX + size * j + size/2, size * i + size/2, (0, 0, 255)))
          j += 1
        i += 1
      return ammos