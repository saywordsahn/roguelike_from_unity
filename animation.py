class Animation:

    def __init__(self, frames):

        if len(frames) <= 0:
            raise Exception('frames should not be empty.')

        self.frames = frames
        self.time = 0
        self.last_updated_time = 0
        self.animation_time = 200
        self.current_image_index = 0

    def get_current_image(self):
        return self.frames[self.current_image_index]

    def update(self, dt):
        self.time += dt

        if self.time - self.last_updated_time >= self.animation_time:
            self.current_image_index = (self.current_image_index + 1) % len(self.frames)
            self.last_updated_time = self.time