import pygame

class SpriteSheet:

    def __init__(self, image, cell_size):
        self.image = image
        self.cell_size = cell_size

    def get_image(self, row, col, width, height):
        image = pygame.Surface((self.cell_size[0], self.cell_size[1])).convert_alpha()
        image.blit(self.image, (0, 0), (row * self.cell_size[0], col * self.cell_size[1], self.cell_size[0], self.cell_size[1]))

        image = pygame.transform.scale(image, (width, height))
        image.set_colorkey((0, 0, 0))
        return image