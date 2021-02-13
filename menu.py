from time import sleep

from arcade.gui import UIManager, UILabel, UIFlatButton, UIImageButton

from constants import *
from databse import DataBase
from sprites import *

help_dict_for_stars = {"False": 0, "лёгкий": 1, "средний": 2, "сложный": 3}


def think_stars(data):
    count = 0
    for i in data:
        count += help_dict_for_stars[i[0]]
    return count


def think_coins(data):
    count = 0
    for i in data:
        count += i[0].count("-")
    return count


database = DataBase()
count_coins = think_coins(database.get_data("levels", "all_coins"))
count_stars = think_stars(database.get_data("levels", "completed"))
level = database.get_data("player_info", "current_level")[0][0]
all_levels = database.get_data("levels")
player = database.get_data("player_info, persons",
                           "persons.path",
                           "player_info.person_id = persons.id")[0][0]


class MainMenuView(arcade.View):
    def __init__(self):
        super(MainMenuView, self).__init__()
        self.background = None
        self.coin = None
        self.star = None
        self.ui_manager = UIManager(self.window)
        self.setup()
        self.cursor = CURSOR
        self.btn = BUTTON_SOUND
        self.btn_settings = SETTINGS_SOUND
        self.btn_exit = EXIT_SOUND

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cursor.center_x = x
        self.cursor.center_y = y

    def setup(self):
        self.ui_manager.purge_ui_elements()

        text = UILabel("Главное меню",
                       center_x=SCREEN_WIDTH // 2,
                       center_y=SCREEN_HEIGHT - 100)
        text.set_style_attrs(font_color=arcade.color.BABY_BLUE, font_size=44)
        self.ui_manager.add_ui_element(text)

        btn_new = UIFlatButton("Новая игра", center_x=SCREEN_WIDTH // 2, center_y=550,
                               height=100, width=300)
        btn_new.set_style_attrs(
            font_color=arcade.color.WHITE,
            font_color_hover=arcade.color.WHITE,
            font_color_press=arcade.color.WHITE,
            bg_color=(255, 165, 10),
            bg_color_hover=(255, 165, 10),
            bg_color_press=(230, 145, 0),
            border_color=(255, 165, 10),
            border_color_hover=arcade.color.WHITE,
            border_color_press=arcade.color.WHITE,
            font_size=22
        )
        btn_new.set_handler("on_click", self.new_game)
        self.ui_manager.add_ui_element(btn_new)

        btn_resume = UIFlatButton("Продолжить", center_x=SCREEN_WIDTH // 2, center_y=400,
                                  height=100, width=300)
        btn_resume.set_style_attrs(
            font_color=arcade.color.WHITE,
            font_color_hover=arcade.color.WHITE,
            font_color_press=arcade.color.WHITE,
            bg_color=(51, 139, 57),
            bg_color_hover=(51, 139, 57),
            bg_color_press=(28, 71, 32),
            border_color=(51, 139, 57),
            border_color_hover=arcade.color.WHITE,
            border_color_press=arcade.color.WHITE,
            font_size=22
        )
        btn_resume.set_handler("on_click", self.resume)
        self.ui_manager.add_ui_element(btn_resume)

        btn_end = UIFlatButton("Выйти из игры", center_x=SCREEN_WIDTH // 2, center_y=250,
                               height=100, width=300)
        btn_end.set_style_attrs(
            font_color=arcade.color.WHITE,
            font_color_hover=arcade.color.WHITE,
            font_color_press=arcade.color.WHITE,
            bg_color=(135, 21, 25),
            bg_color_hover=(135, 21, 25),
            bg_color_press=(122, 21, 24),
            border_color=(135, 21, 25),
            border_color_hover=arcade.color.WHITE,
            border_color_press=arcade.color.WHITE,
            font_size=22
        )
        btn_end.set_handler("on_click", self.end)
        self.ui_manager.add_ui_element(btn_end)

        btn_settings = UIImageButton(center_x=35, center_y=SCREEN_HEIGHT - 35,
                                     normal_texture=arcade.load_texture(SETTINGS),
                                     press_texture=arcade.load_texture(SETTINGS2))
        btn_settings.set_handler("on_click", self.settings)
        self.ui_manager.add_ui_element(btn_settings)

        btn_instruction = UIImageButton(center_x=50,
                                        center_y=45,
                                        normal_texture=arcade.load_texture(INSTRUCTION_IMAGE),
                                        press_texture=arcade.load_texture(INSTRUCTION_IMAGE_2))
        btn_instruction.set_handler("on_click", self.instruction)
        self.ui_manager.add_ui_element(btn_instruction)

    def new_game(self):
        self.btn.play()
        self.ui_manager.purge_ui_elements()
        view = NewGameView()
        self.window.show_view(view)

    def resume(self):
        self.btn.play()
        self.ui_manager.purge_ui_elements()
        view = LevelsMenuView()
        self.window.show_view(view)

    def end(self):
        self.btn_exit.play(1.7)
        sleep(0.9)
        arcade.close_window()

    def settings(self):
        self.btn_settings.play()
        self.ui_manager.purge_ui_elements()
        view = SettingsView()
        self.window.show_view(view)

    def instruction(self):
        self.btn_settings.play()
        self.ui_manager.purge_ui_elements()
        view = InstructionView()
        self.window.show_view(view)

    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.background = BACKGROUND
        self.coin = COIN
        self.star = STAR

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.coin.draw()
        self.star.draw()
        arcade.draw_text(str(count_coins), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 82, anchor_x="right",
                         color=arcade.color.WHITE, font_size=60, bold=True)
        arcade.draw_text(str(count_stars), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 165, anchor_x="right",
                         color=arcade.color.WHITE, font_size=60, bold=True)
        self.cursor.draw()


class SettingsView(arcade.View):
    def __init__(self):
        super(SettingsView, self).__init__()
        self.background = None
        self.coin = None
        self.star = None
        self.ui_manager = UIManager(self.window)
        self.setup()
        self.cursor = CURSOR
        self.btn = BUTTON_SOUND
        self.btn_settings = SETTINGS_SOUND

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cursor.center_x = x
        self.cursor.center_y = y

    def setup(self):
        self.ui_manager.purge_ui_elements()

        text = UILabel("Настройки",
                       center_x=SCREEN_WIDTH // 2,
                       center_y=SCREEN_HEIGHT - 100)
        text.set_style_attrs(font_color=arcade.color.BABY_BLUE, font_size=44)
        self.ui_manager.add_ui_element(text)

        btn_settings = UIImageButton(center_x=35, center_y=SCREEN_HEIGHT - 35,
                                     normal_texture=arcade.load_texture(SETTINGS),
                                     press_texture=arcade.load_texture(SETTINGS2))
        btn_settings.set_handler("on_click", self.settings)
        self.ui_manager.add_ui_element(btn_settings)

        text_level = UILabel("Выбор уровня сложности:",
                             center_x=SCREEN_WIDTH // 2,
                             center_y=SCREEN_HEIGHT - 220)
        text_level.set_style_attrs(font_color=arcade.color.BABY_BLUE, font_size=30)
        self.ui_manager.add_ui_element(text_level)

        level_easy = UIFlatButton("Лёгкий",
                                  center_x=200, center_y=SCREEN_HEIGHT - 325,
                                  width=180, height=100)
        level_easy.set_handler("on_click", self.easy)
        level_easy.set_style_attrs(
            font_color=arcade.color.WHITE,
            font_color_hover=arcade.color.WHITE,
            font_color_press=arcade.color.WHITE,
            bg_color=(51, 139, 57),
            bg_color_hover=(51, 139, 57),
            bg_color_press=(28, 71, 32),
            border_color=(51, 139, 57),
            border_color_hover=arcade.color.WHITE,
            border_color_press=arcade.color.WHITE,
            font_size=22
        )
        self.ui_manager.add_ui_element(level_easy)

        level_medium = UIFlatButton("Средний",
                                    center_x=400, center_y=SCREEN_HEIGHT - 325,
                                    width=180, height=100)
        level_medium.set_handler("on_click", self.medium)
        level_medium.set_style_attrs(
            font_color=arcade.color.WHITE,
            font_color_hover=arcade.color.WHITE,
            font_color_press=arcade.color.WHITE,
            bg_color=(255, 185, 10),
            bg_color_hover=(255, 185, 10),
            bg_color_press=(230, 160, 0),
            border_color=(255, 185, 10),
            border_color_hover=arcade.color.WHITE,
            border_color_press=arcade.color.WHITE,
            font_size=22
        )
        self.ui_manager.add_ui_element(level_medium)

        level_hard = UIFlatButton("Сложный",
                                  center_x=600, center_y=SCREEN_HEIGHT - 325,
                                  width=180, height=100)
        level_hard.set_handler("on_click", self.hard)
        level_hard.set_style_attrs(
            font_color=arcade.color.WHITE,
            font_color_hover=arcade.color.WHITE,
            font_color_press=arcade.color.WHITE,
            bg_color=(155, 21, 25),
            bg_color_hover=(155, 21, 25),
            bg_color_press=(135, 21, 24),
            border_color=(155, 21, 25),
            border_color_hover=arcade.color.WHITE,
            border_color_press=arcade.color.WHITE,
            font_size=22
        )
        self.ui_manager.add_ui_element(level_hard)

    def easy(self):
        global level
        self.btn.play()
        database.change_data("player_info", "current_level = 'лёгкий'")
        level = database.get_data("player_info", "current_level")[0][0]

    def medium(self):
        global level
        self.btn.play()
        database.change_data("player_info", "current_level = 'средний'")
        level = database.get_data("player_info", "current_level")[0][0]

    def hard(self):
        global level
        self.btn.play()
        database.change_data("player_info", "current_level = 'сложный'")
        level = database.get_data("player_info", "current_level")[0][0]

    def settings(self):
        self.btn_settings.play()
        self.ui_manager.purge_ui_elements()
        view = MainMenuView()
        self.window.show_view(view)

    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.background = BACKGROUND
        self.coin = COIN
        self.star = STAR

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.coin.draw()
        self.star.draw()
        arcade.draw_text(str(count_coins), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 82, anchor_x="right",
                         color=arcade.color.WHITE, font_size=60, bold=True)
        arcade.draw_text(str(count_stars), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 165, anchor_x="right",
                         color=arcade.color.WHITE, font_size=60, bold=True)
        arcade.draw_text(f"Сейчас выбран\n{level} уровень сложности", 150, 300,
                         color=arcade.color.BABY_BLUE, font_size=34)
        self.cursor.draw()


class NewGameView(arcade.View):
    def __init__(self):
        super(NewGameView, self).__init__()
        self.background = None
        self.ui_manager = UIManager(self.window)
        self.setup()
        self.cursor = CURSOR
        self.btn = BUTTON_SOUND
        self.btn_2 = GAMEOVER_SOUND

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cursor.center_x = x
        self.cursor.center_y = y

    def setup(self):
        self.ui_manager.purge_ui_elements()

        text = UILabel("Вы точно хотите начать новую игру?",
                       center_x=SCREEN_WIDTH // 2,
                       center_y=SCREEN_HEIGHT - 100)
        text.set_style_attrs(font_color=arcade.color.BABY_BLUE, font_size=34)
        self.ui_manager.add_ui_element(text)

        btn_ok = UIFlatButton("Да",
                              center_x=225, center_y=SCREEN_HEIGHT // 2 - 75,
                              width=225, height=100)
        btn_ok.set_handler("on_click", self.ok)
        btn_ok.set_style_attrs(
            font_color=arcade.color.WHITE,
            font_color_hover=arcade.color.WHITE,
            font_color_press=arcade.color.WHITE,
            bg_color=(51, 139, 57),
            bg_color_hover=(51, 139, 57),
            bg_color_press=(28, 71, 32),
            border_color=(51, 139, 57),
            border_color_hover=arcade.color.WHITE,
            border_color_press=arcade.color.WHITE,
            font_size=22
        )
        self.ui_manager.add_ui_element(btn_ok)

        btn_cancel = UIFlatButton("Отмена",
                                  center_x=575, center_y=SCREEN_HEIGHT // 2 - 75,
                                  width=225, height=100)
        btn_cancel.set_handler("on_click", self.cancel)
        btn_cancel.set_style_attrs(
            font_color=arcade.color.WHITE,
            font_color_hover=arcade.color.WHITE,
            font_color_press=arcade.color.WHITE,
            bg_color=(135, 21, 25),
            bg_color_hover=(135, 21, 25),
            bg_color_press=(122, 21, 24),
            border_color=(135, 21, 25),
            border_color_hover=arcade.color.WHITE,
            border_color_press=arcade.color.WHITE,
            font_size=22
        )
        self.ui_manager.add_ui_element(btn_cancel)

    def ok(self):
        global count_coins, count_stars, all_levels
        self.btn_2.play(1.25)
        database.change_data("levels", "completed = 'False', all_coins = '+++'")
        count_coins = think_coins(database.get_data("levels", "all_coins"))
        count_stars = think_stars(database.get_data("levels", "completed"))
        all_levels = database.get_data("levels")
        self.cancel()

    def cancel(self):
        self.btn.play()
        self.ui_manager.purge_ui_elements()
        view = MainMenuView()
        self.window.show_view(view)

    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.background = BACKGROUND

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        arcade.draw_text("Если вы начнёте новую игру,\nто потеряете весь текущий прогресс!",
                         start_x=125, start_y=520, color=arcade.color.RED, font_size=30)
        self.cursor.draw()


class LevelsMenuView(arcade.View):
    def __init__(self, num_level=0):
        super(LevelsMenuView, self).__init__()
        self.background = None
        self.coin = None
        self.star = None
        self.first_star, self.second_star, self.third_star = None, None, None
        self.num_level = num_level
        self.ui_manager = UIManager(self.window)
        self.set_star()
        self.setup()
        self.cursor = CURSOR
        self.btn = BUTTON_SOUND_2
        self.back = SETTINGS_SOUND
        self.btn_play = PLAY_SOUND

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cursor.center_x = x
        self.cursor.center_y = y

    def setup(self):
        self.ui_manager.purge_ui_elements()

        btn_exit = UIImageButton(center_x=40, center_y=SCREEN_HEIGHT - 50,
                                 normal_texture=arcade.load_texture(DOOR),
                                 press_texture=arcade.load_texture(DOOR2))
        btn_exit.set_handler("on_click", self.exit)
        self.ui_manager.add_ui_element(btn_exit)

        btn_left = UIImageButton(center_x=50, center_y=SCREEN_HEIGHT // 2,
                                 normal_texture=arcade.load_texture(ARROW, flipped_horizontally=True),
                                 press_texture=arcade.load_texture(ARROW2, flipped_horizontally=True))
        btn_left.set_handler("on_click", self.left)
        self.ui_manager.add_ui_element(btn_left)

        btn_right = UIImageButton(center_x=SCREEN_WIDTH - 50, center_y=SCREEN_HEIGHT // 2,
                                  normal_texture=arcade.load_texture(ARROW),
                                  press_texture=arcade.load_texture(ARROW2))
        btn_right.set_handler("on_click", self.right)
        self.ui_manager.add_ui_element(btn_right)

        btn_play = UIFlatButton("Играть", center_x=SCREEN_WIDTH // 2, center_y=SCREEN_HEIGHT // 2,
                                height=120, width=280)
        btn_play.set_handler("on_click", self.play)
        btn_play.set_style_attrs(
            font_color=arcade.color.WHITE,
            font_color_hover=arcade.color.WHITE,
            font_color_press=arcade.color.WHITE,
            bg_color=(51, 139, 57),
            bg_color_hover=(51, 139, 57),
            bg_color_press=(28, 71, 32),
            border_color=(51, 139, 57),
            border_color_hover=arcade.color.WHITE,
            border_color_press=arcade.color.WHITE,
            font_size=34
        )
        self.ui_manager.add_ui_element(btn_play)

    def set_star(self):
        completed = all_levels[self.num_level][3]
        self.first_star = arcade.Sprite(STAR2_IMAGE, center_x=300, center_y=230)
        self.second_star = arcade.Sprite(STAR2_IMAGE, center_x=400, center_y=230)
        self.third_star = arcade.Sprite(STAR2_IMAGE, center_x=500, center_y=230)
        if completed == "лёгкий":
            self.first_star = arcade.Sprite(STAR_IMAGE, SCALING_STAR,
                                            center_x=300, center_y=230)
        elif completed == "средний":
            self.first_star = arcade.Sprite(STAR_IMAGE, SCALING_STAR,
                                            center_x=300, center_y=230)
            self.second_star = arcade.Sprite(STAR_IMAGE, SCALING_STAR,
                                             center_x=400, center_y=230)
        elif completed == "сложный":
            self.first_star = arcade.Sprite(STAR_IMAGE, SCALING_STAR,
                                            center_x=300, center_y=230)
            self.second_star = arcade.Sprite(STAR_IMAGE, SCALING_STAR,
                                             center_x=400, center_y=230)
            self.third_star = arcade.Sprite(STAR_IMAGE, SCALING_STAR,
                                            center_x=500, center_y=230)

    def play(self):
        self.btn_play.play(1.2)
        self.ui_manager.purge_ui_elements()
        view = GameView(all_levels[self.num_level])
        self.window.show_view(view)

    def exit(self):
        self.back.play()
        self.ui_manager.purge_ui_elements()
        view = MainMenuView()
        self.window.show_view(view)

    def left(self):
        self.btn.play()
        if self.num_level == 0:
            self.num_level = len(all_levels) - 1
        else:
            self.num_level -= 1
        self.set_star()

    def right(self):
        self.btn.play()
        if self.num_level == len(all_levels) - 1:
            self.num_level = 0
        else:
            self.num_level += 1
        self.set_star()

    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.background = BACKGROUND2
        self.coin = COIN
        self.star = STAR

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.coin.draw()
        self.star.draw()
        self.first_star.draw()
        self.second_star.draw()
        self.third_star.draw()
        arcade.draw_text(str(count_coins), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 82, anchor_x="right",
                         color=arcade.color.WHITE, font_size=60, bold=True)
        arcade.draw_text(str(count_stars), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 165, anchor_x="right",
                         color=arcade.color.WHITE, font_size=60, bold=True)
        arcade.draw_text(all_levels[self.num_level][1], start_x=SCREEN_WIDTH // 2, start_y=SCREEN_HEIGHT - 200,
                         anchor_x="center", color=arcade.color.ORANGE, font_size=44, font_name="")
        count = all_levels[self.num_level][4].count("-")
        text = f"Собрано монет на уровне: {count}"
        if count == 3:
            text = "На уровне уже собраны все монеты"
        arcade.draw_text(text=text,
                         start_x=SCREEN_WIDTH // 2,
                         start_y=SCREEN_HEIGHT - 260,
                         anchor_x="center", color=arcade.color.YELLOW_ORANGE,
                         font_size=24, font_name="")

        self.cursor.draw()


def load_level(filename):
    filename = "levels/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class GameView(arcade.View):
    def __init__(self, data_level):
        super(GameView, self).__init__()
        self.data_level = data_level
        self.id = data_level[0]
        self.level = load_level(data_level[2])
        self.completed = data_level[3]
        self.count_hit = help_dict_for_stars[level]
        self.level_coins = list(data_level[4])
        self.wall_image = data_level[5]
        self.floor_image = data_level[6]
        self.all_sprites = arcade.SpriteList()
        self.hearts = arcade.SpriteList()
        self.coins = arcade.SpriteList()
        self.coins_list = []
        self.get_coin = []
        self.floors = arcade.SpriteList()
        self.walls = arcade.SpriteList()
        self.horizontal_enemies = arcade.SpriteList()
        self.vertical_enemies = arcade.SpriteList()
        self.player = None
        self.exitt = None
        self.music = BACKGROUND_SOUND
        self.coin_sound = COINS_SOUND
        self.hit_sound = HIT_SOUND
        self.died_sound = DIED_SOUND
        self.win_sound = WIN_SOUND
        self.count_coin = 0
        self.time_after_hit = 0.7
        self.setup()

    def setup(self):
        self.play_song()

        for i in range(1, 4):
            heart = arcade.Sprite(HEART_IMAGE,
                                  center_x=SCREEN_WIDTH - i * 40,
                                  center_y=SCREEN_HEIGHT - 25)
            self.hearts.append(heart)
            self.all_sprites.append(heart)

        for y, string in enumerate(self.level):
            for x, column in enumerate(string):
                if column in ".@123OEV":
                    floor = arcade.Sprite(f"images/{self.floor_image}",
                                          center_x=x * TILE_SIZE + TILE_SIZE // 2,
                                          center_y=(len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 2)
                    self.floors.append(floor)
                    self.all_sprites.append(floor)
                elif column == "#":
                    wall = arcade.Sprite(f"images/{self.wall_image}",
                                         center_x=x * TILE_SIZE + TILE_SIZE // 2,
                                         center_y=(len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 2)
                    self.walls.append(wall)
                    self.all_sprites.append(wall)

        for y, string in enumerate(self.level):
            for x, column in enumerate(string):
                if column == "E":
                    self.exitt = arcade.Sprite(EXIT_IMAGE,
                                               center_x=x * TILE_SIZE + TILE_SIZE // 2,
                                               center_y=(len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 2.2,
                                               scale=0.35)
                    self.all_sprites.append(self.exitt)
                elif column in "123":
                    textures = [arcade.load_texture(COIN_IMAGE),
                                arcade.load_texture(COIN_IMAGE_2),
                                arcade.load_texture(COIN_IMAGE_3),
                                arcade.load_texture(COIN_IMAGE_4),
                                arcade.load_texture(COIN_IMAGE_3, mirrored=True),
                                arcade.load_texture(COIN_IMAGE_2, mirrored=True)]
                    coin = Coin(textures)
                    coin.center_x = x * TILE_SIZE + TILE_SIZE // 2
                    coin.center_y = (len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 2
                    coin.scale = 0.7
                    self.coins_list.append(int(column))
                    self.coins.append(coin)
                    self.all_sprites.append(coin)
                elif column == "O":
                    textures = [arcade.load_texture(f"{ENEMY_IMAGE}_walk{i}.png",
                                                    mirrored=True) for i in range(8)]
                    enemy = Enemy(textures, True, -5)
                    enemy.center_x = x * TILE_SIZE + TILE_SIZE // 2
                    enemy.center_y = (len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 2 + 5
                    enemy.scale = 0.45
                    self.horizontal_enemies.append(enemy)
                    self.all_sprites.append(enemy)
                elif column == "V":
                    enemy = VerticalEnemy(f"{ENEMY_IMAGE}_idle.png", 1)
                    enemy.center_x = x * TILE_SIZE + TILE_SIZE // 2
                    enemy.center_y = (len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 2 + 5
                    enemy.scale = 0.45
                    self.vertical_enemies.append(enemy)
                    self.all_sprites.append(enemy)
                elif column == "@":
                    self.player = Player(path_to_textures=player)
                    self.player.center_x = x * TILE_SIZE + TILE_SIZE // 2
                    self.player.center_y = (len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 2 + 5
                    self.player.scale = 0.45
                    self.all_sprites.append(self.player)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            view = PauseView(self, self.data_level)
            self.window.show_view(view)
        if symbol == arcade.key.LEFT:
            self.player.center_x -= 50
            if self.player.collides_with_list(self.walls) or self.player.left <= 0:
                self.player.center_x += 50
            self.player.index(2)
        if symbol == arcade.key.RIGHT:
            self.player.center_x += 50
            if self.player.collides_with_list(self.walls) or self.player.right >= SCREEN_WIDTH:
                self.player.center_x -= 50
            self.player.index(1)
        if symbol == arcade.key.UP:
            self.player.center_y += 50
            if self.player.collides_with_list(self.walls) or self.player.top >= SCREEN_HEIGHT - 50:
                self.player.center_y -= 50
            self.player.index(3)
        if symbol == arcade.key.DOWN:
            self.player.center_y -= 50
            if self.player.collides_with_list(self.walls) or self.player.bottom <= 0:
                self.player.center_y += 50
            self.player.index(0)

    def play_song(self):
        self.current_player = self.music.play(MUSIC_VOLUME)
        sleep(0.03)

    def on_update(self, delta_time: float):
        global all_levels, count_coins, count_stars
        self.time_after_hit += delta_time
        self.coins.update()
        self.vertical_enemies.update()
        self.horizontal_enemies.update()
        self.player.update()
        if self.player.collides_with_sprite(self.exitt):
            if help_dict_for_stars[level] >= help_dict_for_stars[self.completed]:
                database.change_data("levels",
                                     f"completed = '{level}'",
                                     data_criterion=f"id = {self.id}")
                if len(self.get_coin) > self.level_coins.count("-"):
                    for i in self.get_coin:
                        self.level_coins[i - 1] = "-"
                    database.change_data("levels",
                                         f"all_coins = '{''.join(self.level_coins)}'",
                                         data_criterion=f"id = {self.id}")
            all_levels = database.get_data("levels")
            count_coins = think_coins(database.get_data("levels", "all_coins"))
            count_stars = think_stars(database.get_data("levels", "completed"))
            self.data_level = all_levels[int(self.id) - 1]
            self.off_music()
            self.win_sound.play()
            view = GameWinView(self, self.data_level)
            self.window.show_view(view)
        if self.player.collides_with_list(self.vertical_enemies) \
                or self.player.collides_with_list(self.horizontal_enemies):
            if self.time_after_hit >= 0.7:
                for i in range(self.count_hit):
                    if self.hearts:
                        self.hearts[-1].kill()
                self.hit_sound.play()
                self.time_after_hit = 0
                if not self.hearts:
                    self.off_music()
                    self.died_sound.play()
                    view = GameEndView(self, self.data_level)
                    self.window.show_view(view)
        for i, coin in enumerate(self.coins):
            if self.player.collides_with_sprite(coin):
                self.coin_sound.play()
                self.count_coin += 1
                self.get_coin.append(self.coins_list[i])
                del self.coins_list[i]
                coin.kill()
        for enemy in self.vertical_enemies:
            if enemy.collides_with_list(self.walls) \
                    or enemy.bottom < 0 \
                    or enemy.top > SCREEN_HEIGHT - 50 \
                    or enemy.collides_with_sprite(self.exitt):
                enemy.set_speed()
        for enemy in self.horizontal_enemies:
            if enemy.collides_with_list(self.walls) \
                    or enemy.left < 0 \
                    or enemy.right > SCREEN_HEIGHT \
                    or enemy.collides_with_sprite(self.exitt):
                mirrored, center_x, center_y, speed = enemy.data()
                enemy.kill()
                textures = [arcade.load_texture(f"{ENEMY_IMAGE}_walk{i}.png",
                                                mirrored=not mirrored) for i in range(8)]
                enemy = Enemy(textures, not mirrored, -speed)
                if mirrored:
                    center_x += 8
                else:
                    center_x -= 8
                enemy.center_x = center_x
                enemy.center_y = center_y
                enemy.scale = 0.45
                self.horizontal_enemies.append(enemy)
                self.all_sprites.append(enemy)
        position = self.music.get_stream_position(self.current_player)
        if position == 0.0:
            self.play_song()

    def off_music(self):
        self.current_player.pause()
        self.current_player.delete()

    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()
        arcade.draw_text(f"Монет собрано: {self.count_coin}",
                         start_x=25, start_y=SCREEN_HEIGHT - 40,
                         color=arcade.color.ORANGE, font_size=24)


class PauseView(arcade.View):
    def __init__(self, game_view, data_level):
        super().__init__()
        self.game_view = game_view
        self.data_level = data_level

    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        arcade.start_render()

        self.game_view.all_sprites.draw()
        arcade.draw_text(f"Монет собрано: {self.game_view.count_coin}",
                         start_x=25, start_y=SCREEN_HEIGHT - 40,
                         color=arcade.color.ORANGE, font_size=24)

        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0,
                                          arcade.color.BABY_BLUE + (175,))
        arcade.draw_text("PAUSED", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Нажмите Enter, чтобы вернуться в меню.\nВесь прогресс будет потерян!",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2,
                         arcade.color.BLACK,
                         font_size=24,
                         anchor_x="center")
        arcade.draw_text("Нажмите Esc, чтобы вернуться в игру.",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 80,
                         arcade.color.BLACK,
                         font_size=24,
                         anchor_x="center")
        arcade.draw_text("Нажмите R, чтобы перезапустить уровень.",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 160,
                         arcade.color.BLACK,
                         font_size=24,
                         anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.window.show_view(self.game_view)
        elif symbol == arcade.key.R:
            self.game_view.off_music()
            view = GameView(self.data_level)
            self.window.show_view(view)
        elif symbol == arcade.key.ENTER:
            self.game_view.off_music()
            view = LevelsMenuView(self.data_level[0] - 1)
            self.window.show_view(view)


class GameEndView(arcade.View):
    def __init__(self, game_view, data_level):
        super().__init__()
        self.game_view = game_view
        self.data_level = data_level

    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0,
                                          arcade.color.RED_DEVIL)
        arcade.draw_text("DEFEAT", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Нажмите Enter, чтобы вернуться в меню.",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2,
                         arcade.color.BLACK,
                         font_size=24,
                         anchor_x="center")
        arcade.draw_text("Нажмите R, чтобы перезапустить уровень.",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 80,
                         arcade.color.BLACK,
                         font_size=24,
                         anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            self.game_view.off_music()
            view = GameView(self.data_level)
            self.window.show_view(view)
        elif symbol == arcade.key.ENTER:
            self.game_view.off_music()
            view = LevelsMenuView(self.data_level[0] - 1)
            self.window.show_view(view)


class GameWinView(arcade.View):
    def __init__(self, game_view, data_level):
        super().__init__()
        self.game_view = game_view
        self.data_level = data_level

    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0,
                                          arcade.color.GREEN)
        arcade.draw_text("WIN", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text(f"Вы собрали {self.game_view.count_coin} монет!",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2,
                         arcade.color.BLACK,
                         font_size=24,
                         anchor_x="center")
        arcade.draw_text(f'Уровень пройден на уровне сложности - "{level}"',
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 80,
                         arcade.color.BLACK,
                         font_size=24,
                         anchor_x="center")
        arcade.draw_text("Нажмите Enter, чтобы вернуться в меню.",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 160,
                         arcade.color.BLACK,
                         font_size=24,
                         anchor_x="center")
        arcade.draw_text("Нажмите R, чтобы перезапустить уровень.",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 240,
                         arcade.color.BLACK,
                         font_size=24,
                         anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            self.game_view.off_music()
            view = GameView(self.data_level)
            self.window.show_view(view)
        elif symbol == arcade.key.ENTER:
            self.game_view.off_music()
            view = LevelsMenuView(self.data_level[0] - 1)
            self.window.show_view(view)


class InstructionView(arcade.View):
    def __init__(self):
        super(InstructionView, self).__init__()
        self.background = None
        self.coin = None
        self.star = None
        self.ui_manager = UIManager(self.window)
        self.setup()
        self.cursor = CURSOR
        self.btn_instruction = SETTINGS_SOUND

    def setup(self):
        self.ui_manager.purge_ui_elements()

        text = UILabel("Об игре",
                       center_x=SCREEN_WIDTH // 2,
                       center_y=SCREEN_HEIGHT - 100)
        text.set_style_attrs(font_color=arcade.color.BABY_BLUE, font_size=44)
        self.ui_manager.add_ui_element(text)

        btn_instruction = UIImageButton(center_x=50,
                                        center_y=45,
                                        normal_texture=arcade.load_texture(INSTRUCTION_IMAGE),
                                        press_texture=arcade.load_texture(INSTRUCTION_IMAGE_2))
        btn_instruction.set_handler("on_click", self.instruction)
        self.ui_manager.add_ui_element(btn_instruction)

    def instruction(self):
        self.btn_instruction.play()
        self.ui_manager.purge_ui_elements()
        view = MainMenuView()
        self.window.show_view(view)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cursor.center_x = x
        self.cursor.center_y = y

    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.background = BACKGROUND
        self.coin = COIN
        self.star = STAR

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.coin.draw()
        self.star.draw()
        arcade.draw_text(str(count_coins),
                         SCREEN_WIDTH - 80,
                         SCREEN_HEIGHT - 82,
                         anchor_x="right",
                         color=arcade.color.WHITE,
                         font_size=60,
                         bold=True)
        arcade.draw_text(str(count_stars),
                         SCREEN_WIDTH - 80,
                         SCREEN_HEIGHT - 165,
                         anchor_x="right",
                         color=arcade.color.WHITE,
                         font_size=60,
                         bold=True)
        arcade.draw_text(f"{SCREEN_TITLE} - игра с множеством"
                         f" уровней,\nдля прохождения"
                         f" которых нужно выйти из лабиринта.",
                         SCREEN_WIDTH // 2, 530,
                         color=arcade.color.BABY_BLUE,
                         font_size=24,
                         anchor_x="center")
        arcade.draw_text('На один уровень у вас есть 3 "сердчека" - жизни.'
                         "\nВ зависимости от уровня сложности"
                         "\nпротивники в лабиринте наносят разный урон.",
                         SCREEN_WIDTH // 2 + 80, 400,
                         color=arcade.color.BABY_BLUE,
                         font_size=24,
                         anchor_x="center")
        arcade.draw_text('Если "сердечки" закончатся - \n'
                         'вы потеряете весь прогрес на данном уровне.',
                         SCREEN_WIDTH // 2 - 50, 270,
                         color=arcade.color.BABY_BLUE,
                         font_size=24,
                         anchor_x="center")
        self.cursor.draw()
