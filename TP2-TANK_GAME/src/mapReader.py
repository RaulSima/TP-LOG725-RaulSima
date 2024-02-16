from csv import reader
import pygame
from src.wall import Wall

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