import pygame
import sys
from src.player import Player
from src.menu import Menu
from src.exit import Exit
from src.mapReader import readWallMap
from src.mapReader import readFloorMap
from src.mapReader import readAmmoMap

pygame.init()

# Define colors
BG_COLOR = (153, 178, 178)

# Initialize Pygame
screen = pygame.display.set_mode((768, 570))
clock = pygame.time.Clock()


# Create entities
player = Player()
walls = readWallMap('./maps/walls.csv')
floors = readFloorMap('./maps/floors.csv')
groundAmmos = readAmmoMap('./maps/ammo.csv')

menu = Menu(player)
exit = Exit(96 * 2, 96 * 3)

# Main game loop
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    # before player update
    previous_x = player.rect.x
    previous_y = player.rect.y

    # player update 
    player.update()
    menu.update(player)
    projectiles = player.projectiles

    for proj in projectiles:
        proj.update()
    # check for collisions between player and walls
    wall_collisions = pygame.sprite.spritecollide(player, walls, False)
    for wall_collision in wall_collisions:
        print("Collided")

        # fall back to previous position
        player.rect.x = previous_x
        player.rect.y = previous_y
        break
    
    # check for collisions between projectiles and walls
    for proj in projectiles:
        wall_collisions = pygame.sprite.spritecollide(proj, walls, False)
        for wall_collision in wall_collisions:
            if( wall_collision.type == 'red' and proj.color == (255, 0, 0)):
                wall_collision.kill()
            if( wall_collision.type == 'blue' and proj.color == (0, 0, 255)):
                wall_collision.kill()
            if( wall_collision.type == 'green' and proj.color == (0, 255, 0)):
                wall_collision.kill()
            
            proj.kill()
                
            break
        
    # check collisions between player and ground ammos
    ammo_collisions = pygame.sprite.spritecollide(player, groundAmmos, False)
    for ammo in ammo_collisions:
        if(ammo.color == (255, 0, 0)):
            player.redBullets +=1
        if(ammo.color == (0, 255, 0)):
            player.greenBullets +=1
        if(ammo.color == (0, 0, 255)):
            player.blueBullets +=1
        ammo.kill()
        break   

    # draw
    screen.fill(BG_COLOR)
    
    # draw the floor before the player
    floors.draw(screen)

    # single sprites are drawn with screen.blit()
    screen.blit(player.image, (player.rect.x, player.rect.y))

    # groups of sprites can be drawn with group.draw()
    walls.draw(screen)
    exit.draw(screen)
    for proj in projectiles:
        proj.draw(screen)
    menu.draw(screen)
    for ammo in groundAmmos:
        ammo.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()