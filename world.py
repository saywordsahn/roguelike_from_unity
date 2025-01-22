import random as rand
from enemy import Enemy
import pygame

from enemy_manager import EnemyManager
from settings import *


class CellData:

    def __init__(self, position, tile, is_passable, game_object=None):
        self.position = position
        self.tile = tile
        self.is_passable = is_passable
        self.game_object = game_object

    def has_game_object(self) -> bool:
        return self.game_object is not None

class World:

    def __init__(self, rows, cols, world_theme):
        self.num_rows = rows
        self.num_cols = cols
        self.ground_tiles = world_theme.ground_images
        self.wall_tiles = world_theme.wall_images
        self.obstacle_tiles = world_theme.obstacle_images
        self.tiles: list[list[CellData]] = []
        self.empty_cells = []
        self.enemy_manager = EnemyManager()

    def create_world(self):
        self.tiles = []
        for j in range(self.num_rows):
            row = []
            for i in range(self.num_cols):

                if j == 0 or j == self.num_rows - 1 or i == 0 or i == self.num_cols - 1:
                    row.append(CellData((j, i), rand.choice(self.wall_tiles), False))
                else:
                    cell = CellData((j, i), rand.choice( self.ground_tiles), True)
                    row.append(cell)
                    self.empty_cells.append(cell)

            self.tiles.append(row)

    def spawn_obstacles(self):

        for i in range(3):
            cell: CellData = rand.choice(self.empty_cells)
            cell.tile = rand.choice(self.obstacle_tiles)
            cell.is_passable = False
            self.empty_cells.remove(cell)

    def spawn_enemies(self):
        for i in range(3):
            cell: CellData = rand.choice(self.empty_cells)
            cell.is_passable = False
            cell.game_object = Enemy(cell.position, EnemyManager.get_animation())
            self.empty_cells.remove(cell)

    def draw(self, screen):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                screen.blit(self.tiles[i][j].tile, (j * 64, i * 64))
                if self.tiles[i][j].has_game_object():
                    self.tiles[i][j].game_object.draw(screen)

    @staticmethod
    def get_adjacent_pos(position: pygame.Vector2, direction: Direction):

        if direction == Direction.RIGHT:
            return position + Vector2.RIGHT
        elif direction == Direction.LEFT:
            return position + Vector2.LEFT
        elif direction == Direction.UP:
            return position + Vector2.UP
        else:
            return position + Vector2.DOWN

    def is_passable(self, position: pygame.Vector2):
        return self.tiles[int(position.x)][int(position.y)].is_passable