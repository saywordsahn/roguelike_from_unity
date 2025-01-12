from settings import *
import pygame

class Player:

    def __init__(self, idle_animation):
        self.grid_position = pygame.Vector2(1, 1)
        self.idle_animation = idle_animation
        self.state = PlayerState.IDLE
        self.destination = self.grid_position

    def draw(self, screen) -> None:
        screen.blit(self.idle_animation.get_current_image(), grid_to_world(self.grid_position))

    def update(self, dt):
        self.idle_animation.update(dt)

        if self.state == PlayerState.MOVING:
            self.grid_position = self.grid_position.lerp(self.destination, dt * UNIT_MOVE_SPEED / 1000)

            if self.grid_position.distance_to(self.destination) <= LERP_BREAK_DISTANCE:
                self.grid_position = self.destination
                self.state = PlayerState.IDLE

    def move(self, direction: Direction) -> None:

        if direction == Direction.RIGHT:
            self.destination = self.grid_position + Vector2.RIGHT
        elif direction == Direction.LEFT:
            self.destination = self.grid_position + Vector2.LEFT
        elif direction == Direction.UP:
            self.destination = self.grid_position + Vector2.UP
        else:
            self.destination = self.grid_position + Vector2.DOWN

        self.state = PlayerState.MOVING




