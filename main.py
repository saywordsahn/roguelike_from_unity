import pygame
from settings import *
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


from animation import Animation
from spritesheet import SpriteSheet
from world import World
from player import Player
from themes import urban_theme







world = World(8, 8, urban_theme)
world.create_world()

player_idle_animation = Animation(urban_theme.sprite_sheet.load_strip((0, 0), 6))
player = Player(player_idle_animation)

clock = pygame.time.Clock()

while True:

    dt = clock.tick(FPS)


    screen.fill((50,50,50))
    world.draw(screen)
    player.draw(screen)

    player.update(dt)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.move(Direction.RIGHT)
            elif event.key == pygame.K_a:
                player.move(Direction.LEFT)
            elif event.key == pygame.K_w:
                player.move(Direction.UP)
            elif event.key == pygame.K_s:
                player.move(Direction.DOWN)




    pygame.display.update()