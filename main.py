import pygame
from spritesheet import SpriteSheet

pygame.init()


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


urban_theme_image = pygame.image.load('./Sprites/UrbanTheme.png')


sprite_sheet = SpriteSheet(urban_theme_image, (32, 32), 7, 8)

image = sprite_sheet.get_image(0, 0, 64, 64)

ground_images = sprite_sheet.load_strip((4, 0), 8, 64, 64)


while True:

    screen.fill((50,50,50))

    for i in range(len(ground_images)):
        screen.blit(ground_images[i], (i * 64, 0))



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()