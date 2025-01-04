class Animation:

    def __init__(self, frames):
        self.frames = frames

    def get_current_image(self):

        if len(self.frames) <= 0:
            raise Exception('frames should not be empty.')

        return self.frames[0]