from settings import *
import pygame

class Player:

    def __init__(self, idle_animation):
        self.grid_position = pygame.Vector2(1, 1)
        self.idle_animation = idle_animation
        self.state = PlayerState.IDLE
        self.move_speed = 3

    def draw(self, screen) -> None:
        screen.blit(self.idle_animation.get_current_image(), grid_to_world(self.grid_position))

    def update(self, dt):
        self.idle_animation.update(dt)

        # if self.state == PlayerState.MOVING:
        #     self.col += self.move_speed * dt / 1000.0


    def move(self, direction: Direction) -> None:

        if direction == Direction.RIGHT:
            self.grid_position += Vector2.RIGHT
        elif direction == Direction.LEFT:
            self.grid_position += Vector2.LEFT
        elif direction == Direction.UP:
            self.grid_position += Vector2.UP
        else:
            self.grid_position += Vector2.DOWN

        self.state = PlayerState.MOVING


