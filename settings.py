import enum
from typing import Tuple
import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 512
FPS = 60
TILE_SIZE = (32, 32)
SCALE = 2
LERP_BREAK_DISTANCE = 0.1
UNIT_MOVE_SPEED = 10.0


class Direction(enum.Enum):
    LEFT = 1,
    RIGHT = 2,
    UP = 3,
    DOWN = 4

class PlayerState(enum.Enum):
    IDLE = 1,
    MOVING = 2,
    ATTACKING = 3

class Vector2:

    RIGHT = pygame.Vector2(0, 1)
    LEFT = pygame.Vector2(0, -1)
    UP = pygame.Vector2(-1, 0)
    DOWN = pygame.Vector2(1, 0)


def grid_to_world(grid_position) -> Tuple[float, float]:
    return grid_position.y * TILE_SIZE[0] * SCALE, grid_position.x * TILE_SIZE[1] * SCALE

# def grid_to_world(row, col) -> Tuple[int, int]:
#     return col * TILE_SIZE[0] * SCALE, row * TILE_SIZE[1] * SCALE