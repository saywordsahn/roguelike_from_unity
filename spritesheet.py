import pygame

class SpriteSheet:

    def __init__(self, image, cell_size, num_rows, num_cols):
        self.image = image
        self.cell_size = cell_size
        self.num_rows = num_rows
        self.num_cols = num_cols

    def get_image(self, row, col, width, height):
        image = pygame.Surface((self.cell_size[0], self.cell_size[1])).convert_alpha()
        image.blit(self.image, (0, 0), (col * self.cell_size[0], row * self.cell_size[1], self.cell_size[0], self.cell_size[1]))

        image = pygame.transform.scale(image, (width, height))
        image.set_colorkey((0, 0, 0))
        return image

    def load_strip(self, start, num_frames, width, height):

        strip = []

        row = start[0]
        col = start[1]

        while num_frames > 0:

            if col >= self.num_cols:
                row += 1
                col = 0
            else:
                image = self.get_image(row, col, width, height)
                strip.append(image)
                col += 1
                num_frames -= 1

        return strip





