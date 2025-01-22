
class EnemyImages:

    def __init__(self, idle_images):
        self.idle_images = idle_images

class WorldTheme:

    def __init__(self, sprite_sheet, ground_images, wall_images, obstacle_images, enemy_images):
        self.sprite_sheet = sprite_sheet
        self.obstacle_images = obstacle_images
        self.wall_images = wall_images
        self.ground_images = ground_images
        self.enemy_images = enemy_images




