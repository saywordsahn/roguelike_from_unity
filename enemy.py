from animation import Animation

class Enemy:

    def __init__(self, position, idle_animation: Animation):
        self.idle_animation = idle_animation
        self.position = position

    def update(self, dt):
        self.idle_animation.update(dt)

    def draw(self, screen):
        screen.blit(self.idle_animation.get_current_image(), (self.position[1] * 64, self.position[0] * 64))