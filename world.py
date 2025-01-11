import random as rand

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
