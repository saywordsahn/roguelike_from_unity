import pygame

pygame.init()


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quit(0)


    pygame.display.update()