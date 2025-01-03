import pygame
from spritesheet import SpriteSheet

pygame.init()


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


urban_theme_image = pygame.image.load('./Sprites/UrbanTheme.png')


sprite_sheet = SpriteSheet(urban_theme_image, (32, 32))

image = sprite_sheet.get_image(0, 0, 64, 64)


while True:

    screen.fill((50,50,50))
    screen.blit(image, (0, 0))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()