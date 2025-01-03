

class Player:

    def __init__(self, idle_images):
        self.row = 1
        self.col = 1
        self.idle_images = idle_images
        self.current_image = idle_images[0]

    def draw(self, screen):
        screen.blit(self.current_image, (self.col * 64, self.row * 64))