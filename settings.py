import enum
from typing import Tuple

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 512
FPS = 60
TILE_SIZE = (32, 32)
SCALE = 2

class Direction(enum.Enum):
    LEFT = 1,
    RIGHT = 2,
    UP = 3,
    DOWN = 4

class PlayerState(enum.Enum):
    IDLE = 1,
    MOVING = 2,
    ATTACKING = 3

def grid_to_world(row, col) -> Tuple[int, int]:
    return col * TILE_SIZE[0] * SCALE, row * TILE_SIZE[1] * SCALE