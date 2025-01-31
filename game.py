import pygame

from enemy_manager import EnemyManager
from game_object import GameObjectType
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
        self.world.spawn_enemies()

    def draw(self, screen):
        self.world.draw(screen)
        self.player.draw(screen)

    def update(self, dt):
        self.player.update(dt)
        self.world.update(dt)

    def player_can_move_to(self, direction: Direction):
        if self.world.is_passable(self.world.get_adjacent_pos(self.player.grid_position, direction)):
            return True

        return False

    def enemy_turn(self):
        enemies = self.world.get_game_objects_of_type(GameObjectType.Enemy)

        for enemy in enemies:
            print('enemy', enemy, 'takes turn')

    def get_player_move(self, direction: Direction) -> PlayerAction:
        # if enemy or debris attack
        # if open space move
        # else return false


        if self.player_can_move_to(direction):
            return PlayerAction.MOVE


    def handle_input(self, event):
        if event.type == pygame.KEYDOWN and self.player.state == PlayerState.IDLE:

            player_has_moved = False
            if event.key == pygame.K_d:
                if self.player_can_move_to(Direction.RIGHT):
                    self.player.move(Direction.RIGHT)
                    player_has_moved = True
            elif event.key == pygame.K_a:
                if self.player_can_move_to(Direction.LEFT):
                    self.player.move(Direction.LEFT)
                    player_has_moved = True
            elif event.key == pygame.K_w:
                if self.player_can_move_to(Direction.UP):
                    self.player.move(Direction.UP)
                    player_has_moved = True
            elif event.key == pygame.K_s:
                if self.player_can_move_to(Direction.DOWN):
                    self.player.move(Direction.DOWN)
                    player_has_moved = True

            if player_has_moved:
                self.enemy_turn()