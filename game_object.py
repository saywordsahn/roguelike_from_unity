import enum
from enum import Enum

class GameObjectType(enum.Enum):
    Enemy = 1,
    Item = 2

class GameObject:

    def __init__(self, game_object_type: GameObjectType):
        self.game_object_type = game_object_type