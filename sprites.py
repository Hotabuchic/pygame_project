from arcade import Sprite, load_texture


class Coin(Sprite):
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


class Enemy(Sprite):
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


class VerticalEnemy(Sprite):
    def __init__(self, image, speed_y):
        super(VerticalEnemy, self).__init__(filename=image)
        self.speed_y = speed_y

    def update(self):
        self.center_y += self.speed_y

    def set_speed(self):
        self.speed_y = -self.speed_y


class Player(Sprite):
    def __init__(self, path_to_textures):
        super(Player, self).__init__(hit_box_algorithm="Detailed")
        self.path_to_textures = ":resources:images/animated_characters/" + path_to_textures
        self.textures = [load_texture(f"{self.path_to_textures}_idle.png"),
                         load_texture(f"{self.path_to_textures}_walk5.png"),
                         load_texture(f"{self.path_to_textures}_walk5.png",
                                      mirrored=True),
                         load_texture(f"{self.path_to_textures}_climb0.png")]
        self.texture_index = 0
        self.set_texture(self.texture_index)

    def update(self):
        self.set_texture(self.texture_index)

    def index(self, index):
        self.texture_index = index
