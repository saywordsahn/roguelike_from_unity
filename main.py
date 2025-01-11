import pygame
from settings import *
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



from game import Game




game = Game()

clock = pygame.time.Clock()

while True:

    dt = clock.tick(FPS)


    screen.fill((50,50,50))
    game.draw(screen)


    game.update(dt)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        game.handle_input(event)




    pygame.display.update()