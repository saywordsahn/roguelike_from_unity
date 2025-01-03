import random as rand

class World:

    def __init__(self, rows, cols, ground_tiles):
        self.num_rows = rows
        self.num_cols = cols
        self.ground_tiles = ground_tiles
        self.tiles = []

    def create_world(self):
        self.tiles = []
        for j in range(self.num_rows):
            row = []
            for i in range(self.num_cols):
                row.append(rand.choice(self.ground_tiles))
            self.tiles.append(row)

    def draw(self, screen):

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                screen.blit(self.tiles[i][j], (j * 64, i * 64))
