import pygame

class SpriteSheet:

    def __init__(self, image):
        self.image = image

    def get_image(self, row, col, width, height):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.image, (0, 0), (row * width, col * width, width, height))

        image = pygame.transform.scale(image, (64, 64))
        image.set_colorkey((0, 0, 0))
        return image