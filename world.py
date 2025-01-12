import random as rand

import pygame

from settings import *


class CellData:

    def __init__(self, tile, is_passable):
        self.tile = tile
        self.is_passable = is_passable

class World:

    def __init__(self, rows, cols, world_theme):
        self.num_rows = rows
        self.num_cols = cols
        self.ground_tiles = world_theme.ground_images
        self.wall_tiles = world_theme.wall_images
        self.obstacle_tiles = world_theme.obstacle_images
        self.tiles = []

    def create_world(self):
        self.tiles = []
        for j in range(self.num_rows):
            row = []
            for i in range(self.num_cols):

                if j == 0 or j == self.num_rows - 1 or i == 0 or i == self.num_cols - 1:
                    row.append(CellData(rand.choice(self.wall_tiles), False))
                else:
                    row.append(CellData(rand.choice(self.ground_tiles), True))

            self.tiles.append(row)

    def draw(self, screen):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                screen.blit(self.tiles[i][j].tile, (j * 64, i * 64))

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