import pygame

from settings import *
from themes import urban_theme
from world import World
from animation import Animation
from player import Player


class Game:

    def __init__(self):
        self.world = World(8, 8, urban_theme)
        player_idle_animation = Animation(urban_theme.sprite_sheet.load_strip((0, 0), 6))
        self.player = Player(player_idle_animation)
        self.reset()

    def reset(self):
        self.world.create_world()
        self.world.spawn_obstacles()

    def draw(self, screen):
        self.world.draw(screen)
        self.player.draw(screen)

    def update(self, dt):
        self.player.update(dt)

    def player_can_move_to(self, direction: Direction):
        if self.world.is_passable(self.world.get_adjacent_pos(self.player.grid_position, direction)):
            return True

        return False

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN and self.player.state == PlayerState.IDLE:
            if event.key == pygame.K_d:
                if self.player_can_move_to(Direction.RIGHT):
                    self.player.move(Direction.RIGHT)
            elif event.key == pygame.K_a:
                if self.player_can_move_to(Direction.LEFT):
                    self.player.move(Direction.LEFT)
            elif event.key == pygame.K_w:
                if self.player_can_move_to(Direction.UP):
                    self.player.move(Direction.UP)
            elif event.key == pygame.K_s:
                if self.player_can_move_to(Direction.DOWN):
                    self.player.move(Direction.DOWN)