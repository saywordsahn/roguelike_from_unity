import random as rand

class World:

    def __init__(self, rows, cols, ground_tiles, wall_tiles, obstacle_tiles):
        self.num_rows = rows
        self.num_cols = cols
        self.ground_tiles = ground_tiles
        self.wall_tiles = wall_tiles
        self.obstacle_tiles = obstacle_tiles
        self.tiles = []

    def create_world(self):
        self.tiles = []
        for j in range(self.num_rows):
            row = []
            for i in range(self.num_cols):

                if j == 0 or j == self.num_rows - 1 or i == 0 or i == self.num_cols - 1:
                    row.append(rand.choice(self.wall_tiles))
                else:
                    row.append(rand.choice(self.ground_tiles))

            self.tiles.append(row)

    def draw(self, screen):

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                screen.blit(self.tiles[i][j], (j * 64, i * 64))
