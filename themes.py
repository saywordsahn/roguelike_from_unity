import pygame

from spritesheet import SpriteSheet
from world_theme import WorldTheme

urban_theme_image = pygame.image.load('./Sprites/UrbanTheme.png')

sprite_sheet = SpriteSheet(urban_theme_image, (32, 32), 7, 8, 2)

ground_images = sprite_sheet.load_strip((4, 0), 8)
wall_images = sprite_sheet.load_strip((3, 1), 2)
obstacle_images = sprite_sheet.load_strip((2, 5), 4)
obstacle_images.append(sprite_sheet.load_strip((3, 3), 5))

urban_theme = WorldTheme(sprite_sheet, ground_images, wall_images, obstacle_images)