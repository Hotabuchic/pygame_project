from time import sleep

import arcade
from arcade.gui import UIManager, UILabel, UIFlatButton, UIImageButton

from constants import *
from databse import DataBase
from sprites import Coin

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
        global count_coins
        self.btn_2.play(1.25)
        database.change_data("levels", "completed = 'False', all_coins = '+++'")
        database.change_data("player_info", "count_coins = 0")
        count_coins = database.get_data("player_info", "count_coins")[0][0]
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
    def __init__(self):
        super(LevelsMenuView, self).__init__()
        self.background = None
        self.coin = None
        self.star = None
        self.first_star, self.second_star, self.third_star = None, None, None
        self.num_level = 0
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
        arcade.draw_text(all_levels[self.num_level][1], start_x=SCREEN_WIDTH // 2, start_y=SCREEN_HEIGHT - 250,
                         anchor_x="center", color=arcade.color.ORANGE, font_size=44, font_name="")
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
        self.level = load_level(data_level[2])
        self.level_coins = data_level[4]
        self.wall_image = data_level[5]
        self.floor_image = data_level[6]
        self.all_sprites = arcade.SpriteList()
        self.hearts = arcade.SpriteList()
        self.coins = arcade.SpriteList()
        self.floors = arcade.SpriteList()
        self.walls = arcade.SpriteList()
        self.player = None
        self.music = BACKGROUND_SOUND
        self.count_coin = 0
        self.setup()

    def setup(self):
        self.play_song()

        for y, string in enumerate(self.level):
            for i in range(1, 4):
                heart = arcade.Sprite(HEART_IMAGE,
                                      center_x=SCREEN_WIDTH - i * 40,
                                      center_y=SCREEN_HEIGHT - 25)
                self.hearts.append(heart)
                self.all_sprites.append(heart)
            for x, column in enumerate(string):
                if column in ".@123OE":
                    floor = arcade.Sprite(f"images/{self.floor_image}",
                                          center_x=x * TILE_SIZE + TILE_SIZE // 2,
                                          center_y=(len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 2)
                    self.floors.append(floor)
                    self.all_sprites.append(floor)
                    if column == "E":
                        exitt = arcade.Sprite(EXIT_IMAGE,
                                              center_x=x * TILE_SIZE + TILE_SIZE // 2,
                                              center_y=(len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 3,
                                              scale=0.35)
                        self.all_sprites.append(exitt)
                    elif column in "123":
                        if self.level_coins[int(column) - 1] == "+":
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
                            self.coins.append(coin)
                            self.all_sprites.append(coin)
                elif column == "#":
                    wall = arcade.Sprite(f"images/{self.wall_image}",
                                         center_x=x * TILE_SIZE + TILE_SIZE // 2,
                                         center_y=(len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 2)
                    self.walls.append(wall)
                    self.all_sprites.append(wall)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            view = PauseView(self, self.data_level)
            self.window.show_view(view)

    def play_song(self):
        self.current_player = self.music.play(MUSIC_VOLUME)
        sleep(0.03)

    def on_update(self, delta_time: float):
        self.coins.update()
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
            view = LevelsMenuView()
            self.window.show_view(view)
