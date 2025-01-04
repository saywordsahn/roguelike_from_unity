import pygame

from animation import Animation
from spritesheet import SpriteSheet
from world import World
from player import Player

pygame.init()


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 512

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


urban_theme_image = pygame.image.load('./Sprites/UrbanTheme.png')


sprite_sheet = SpriteSheet(urban_theme_image, (32, 32), 7, 8, 2)

ground_images = sprite_sheet.load_strip((4, 0), 8)
wall_images = sprite_sheet.load_strip((3, 1), 2)
obstacle_images = sprite_sheet.load_strip((2, 5), 4)
obstacle_images.append(sprite_sheet.load_strip((3, 3), 5))


world = World(8, 8, ground_images, wall_images, obstacle_images)
world.create_world()

player_idle_animation = Animation(sprite_sheet.load_strip((0, 0), 6))
player = Player(player_idle_animation)

while True:

    screen.fill((50,50,50))



    world.draw(screen)
    player.draw(screen)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


    pygame.display.update()