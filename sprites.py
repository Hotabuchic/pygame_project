import arcade


class Coin(arcade.Sprite):
    def __init__(self, texture_list):
        super(Coin, self).__init__()
        self.textures = texture_list
        self.texture_index = 0
        self.set_texture(self.texture_index)
        self.frame_count = 0

    def update(self):
        self.frame_count += 1
        if self.frame_count % 5 == 0:
            self.texture_index += 1
            if self.texture_index < len(self.textures):
                self.set_texture(self.texture_index)
            else:
                self.texture_index = 0