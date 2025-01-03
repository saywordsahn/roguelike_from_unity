import pygame

pygame.init()


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


urban_theme_image = pygame.image.load('./Sprites/UrbanTheme.png')


def get_image(sprite_sheet, row, col, width, height):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sprite_sheet, (0, 0), (row * width, col * width, width, height))

    image = pygame.transform.scale(image, (64, 64))
    image.set_colorkey((0, 0, 0))
    return image


while True:

    screen.fill((50,50,50))
    screen.blit(get_image(urban_theme_image, 1, 1, 32, 32), (0, 0))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()