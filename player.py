

class Player:

    def __init__(self, idle_animation):
        self.row = 1
        self.col = 1
        self.idle_animation = idle_animation
        self.current_image = self.idle_animation.get_current_image()

    def draw(self, screen):
        screen.blit(self.idle_animation.get_current_image(), (self.col * 64, self.row * 64))

    def update(self, dt):
        self.idle_animation.update(dt)
