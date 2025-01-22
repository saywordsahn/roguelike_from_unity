from animation import Animation
from enemy import Enemy
from themes import enemy_idle_images


class EnemyManager:

    def __init__(self):
        self.enemy_idle_images = enemy_idle_images
        self.enemies: list[Enemy] = []


    @staticmethod
    def get_animation():
        return Animation(enemy_idle_images)