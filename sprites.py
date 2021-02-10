import arcade


class Coin(arcade.Sprite):
    def __init__(self, texture_list):
        super(Coin, self).__init__(hit_box_algorithm="Detailed")
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


class Enemy(arcade.Sprite):
    def __init__(self, texture_list, mirrored, speed):
        super(Enemy, self).__init__(hit_box_algorithm="Detailed")
        self.mirrored = mirrored
        self.textures = texture_list
        self.texture_index = 0
        self.set_texture(self.texture_index)
        self.frame_count = 0
        self.speed = speed

    def update(self):
        self.frame_count += 1
        if self.frame_count % 4 == 0:
            self.texture_index += 1
            self.center_x += self.speed
            if self.texture_index < len(self.textures):
                self.set_texture(self.texture_index)
            else:
                self.texture_index = 0

    def data(self):
        return self.mirrored, self.center_x, self.center_y, self.speed


class Player(arcade.Sprite):
    def __init__(self, path_to_textures):
        super(Player, self).__init__(hit_box_algorithm="Detailed")
        self.path_to_textures = ":resources:images/animated_characters/" + path_to_textures
        self.textures = [arcade.load_texture(f"{self.path_to_textures}_idle.png"),
                         arcade.load_texture(f"{self.path_to_textures}_walk5.png"),
                         arcade.load_texture(f"{self.path_to_textures}_walk5.png",
                                             mirrored=True)]
        self.texture_index = 0
        self.set_texture(self.texture_index)

    def update(self):
        self.set_texture(self.texture_index)

    def index(self, index):
        self.texture_index = index
