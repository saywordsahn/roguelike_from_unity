from settings import *

class Player:

    def __init__(self, idle_animation):
        self.row = 1
        self.col = 1
        self.idle_animation = idle_animation
        self.state = PlayerState.IDLE

    def draw(self, screen) -> None:
        screen.blit(self.idle_animation.get_current_image(), grid_to_world(self.row, self.col))

    def update(self, dt):
        self.idle_animation.update(dt)

        if self.state == PlayerState.MOVING:
            print('Im moving')

    def move(self, direction: Direction) -> None:

        if direction == Direction.RIGHT:
            self.col += 1
        elif direction == Direction.LEFT:
            self.col -= 1
        elif direction == Direction.UP:
            self.row -= 1
        else:
            self.row += 1


