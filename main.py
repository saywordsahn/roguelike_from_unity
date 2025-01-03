import pygame
from spritesheet import SpriteSheet
from world import World

pygame.init()


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 512

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


urban_theme_image = pygame.image.load('./Sprites/UrbanTheme.png')


sprite_sheet = SpriteSheet(urban_theme_image, (32, 32), 7, 8)

image = sprite_sheet.get_image(0, 0, 64, 64)

ground_images = sprite_sheet.load_strip((4, 0), 8, 64, 64)
wall_images = sprite_sheet.load_strip((3, 1), 2, 64, 64)

world = World(8, 8, ground_images, wall_images)
world.create_world()

while True:

    screen.fill((50,50,50))



    world.draw(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()