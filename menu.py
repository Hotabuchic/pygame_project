from math import floor
from time import sleep

from arcade import View, color, \
    draw_text, key, set_viewport, \
    start_render, close_window, SpriteList, draw_lrtb_rectangle_filled
from arcade.experimental.lights import Light, LightLayer
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


database = DataBase()
count_coins = database.get_data("player_info", "count_coins")[0][0]
count_stars = think_stars(database.get_data("levels", "completed"))
level = database.get_data("player_info", "current_level")[0][0]
all_levels = database.get_data("levels")
player = database.get_data("player_info, persons",
                           "persons.path",
                           "player_info.person_id = persons.id")[0][0]
language = database.get_data("player_info", "language")[0][0]
all_person = database.get_data("persons")


class MainMenuView(View):
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

        text = UILabel(database.get_data("dictionary",
                                         language,
                                         "russian = 'Главное меню'")[0][0],
                       center_x=SCREEN_WIDTH // 2,
                       center_y=SCREEN_HEIGHT - 100)
        text.set_style_attrs(font_color=color.BABY_BLUE, font_size=44)
        self.ui_manager.add_ui_element(text)

        btn_new = UIFlatButton(database.get_data("dictionary",
                                                 language,
                                                 "russian = 'Новая игра'")[0][0],
                               center_x=SCREEN_WIDTH // 2,
                               center_y=550,
                               height=100, width=300)
        btn_new.set_style_attrs(
            font_color=color.WHITE,
            font_color_hover=color.WHITE,
            font_color_press=color.WHITE,
            bg_color=(255, 165, 10),
            bg_color_hover=(255, 165, 10),
            bg_color_press=(230, 145, 0),
            border_color=(255, 165, 10),
            border_color_hover=color.WHITE,
            border_color_press=color.WHITE,
            font_size=22
        )
        btn_new.set_handler("on_click", self.new_game)
        self.ui_manager.add_ui_element(btn_new)

        btn_resume = UIFlatButton(database.get_data("dictionary",
                                                    language,
                                                    "russian = 'Продолжить'")[0][0],
                                  center_x=SCREEN_WIDTH // 2,
                                  center_y=400,
                                  height=100, width=300)
        btn_resume.set_style_attrs(
            font_color=color.WHITE,
            font_color_hover=color.WHITE,
            font_color_press=color.WHITE,
            bg_color=(51, 139, 57),
            bg_color_hover=(51, 139, 57),
            bg_color_press=(28, 71, 32),
            border_color=(51, 139, 57),
            border_color_hover=color.WHITE,
            border_color_press=color.WHITE,
            font_size=22
        )
        btn_resume.set_handler("on_click", self.resume)
        self.ui_manager.add_ui_element(btn_resume)

        btn_end = UIFlatButton(database.get_data("dictionary",
                                                 language,
                                                 "russian = 'Выйти из игры'")[0][0],
                               center_x=SCREEN_WIDTH // 2,
                               center_y=250,
                               height=100, width=300)
        btn_end.set_style_attrs(
            font_color=color.WHITE,
            font_color_hover=color.WHITE,
            font_color_press=color.WHITE,
            bg_color=(135, 21, 25),
            bg_color_hover=(135, 21, 25),
            bg_color_press=(122, 21, 24),
            border_color=(135, 21, 25),
            border_color_hover=color.WHITE,
            border_color_press=color.WHITE,
            font_size=22
        )
        btn_end.set_handler("on_click", self.end)
        self.ui_manager.add_ui_element(btn_end)

        btn_settings = UIImageButton(center_x=35, center_y=SCREEN_HEIGHT - 35,
                                     normal_texture=load_texture(SETTINGS),
                                     press_texture=load_texture(SETTINGS2))
        btn_settings.set_handler("on_click", self.settings)
        self.ui_manager.add_ui_element(btn_settings)

        btn_instruction = UIImageButton(center_x=50,
                                        center_y=45,
                                        normal_texture=load_texture(INSTRUCTION_IMAGE),
                                        press_texture=load_texture(INSTRUCTION_IMAGE_2))
        btn_instruction.set_handler("on_click", self.instruction)
        self.ui_manager.add_ui_element(btn_instruction)

        btn_shop = UIImageButton(center_x=SCREEN_WIDTH - 50,
                                 center_y=45,
                                 normal_texture=load_texture(SHOP_IMAGE),
                                 press_texture=load_texture(SHOP_IMAGE_2))
        btn_shop.set_handler("on_click", self.shop)
        self.ui_manager.add_ui_element(btn_shop)

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
        close_window()

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

    def shop(self):
        self.btn.play()
        self.ui_manager.purge_ui_elements()
        view = ShopView()
        self.window.show_view(view)

    def on_show(self):
        set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.background = BACKGROUND
        self.coin = COIN
        self.star = STAR

    def on_draw(self):
        start_render()
        self.background.draw()
        self.coin.draw()
        self.star.draw()
        draw_text(str(count_coins), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 82, anchor_x="right",
                  color=color.WHITE, font_size=60, bold=True)
        draw_text(str(count_stars), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 165, anchor_x="right",
                  color=color.WHITE, font_size=60, bold=True)
        self.cursor.draw()


class SettingsView(View):
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

        text = UILabel(database.get_data("dictionary",
                                         language,
                                         "russian = 'Настройки'")[0][0],
                       center_x=SCREEN_WIDTH // 2,
                       center_y=SCREEN_HEIGHT - 100)
        text.set_style_attrs(font_color=color.BABY_BLUE, font_size=44)
        self.ui_manager.add_ui_element(text)

        btn_settings = UIImageButton(center_x=35, center_y=SCREEN_HEIGHT - 35,
                                     normal_texture=load_texture(SETTINGS),
                                     press_texture=load_texture(SETTINGS2))
        btn_settings.set_handler("on_click", self.settings)
        self.ui_manager.add_ui_element(btn_settings)

        text_level = UILabel(database.get_data("dictionary",
                                               language,
                                               "russian = 'Выбор уровня сложности:'")[0][0],
                             center_x=SCREEN_WIDTH // 2,
                             center_y=SCREEN_HEIGHT - 220)
        text_level.set_style_attrs(font_color=color.BABY_BLUE, font_size=30)
        self.ui_manager.add_ui_element(text_level)

        text_language = UILabel(database.get_data("dictionary",
                                                  language,
                                                  "russian = 'Выбор языка:'")[0][0],
                                center_x=SCREEN_WIDTH // 2,
                                center_y=SCREEN_HEIGHT - 600)
        text_language.set_style_attrs(font_color=color.BABY_BLUE, font_size=30)
        self.ui_manager.add_ui_element(text_language)

        level_easy = UIFlatButton(database.get_data("dictionary",
                                                    language,
                                                    "russian = 'Лёгкий'")[0][0],
                                  center_x=200, center_y=SCREEN_HEIGHT - 325,
                                  width=180, height=100)
        level_easy.set_handler("on_click", self.easy)
        level_easy.set_style_attrs(
            font_color=color.WHITE,
            font_color_hover=color.WHITE,
            font_color_press=color.WHITE,
            bg_color=(51, 139, 57),
            bg_color_hover=(51, 139, 57),
            bg_color_press=(28, 71, 32),
            border_color=(51, 139, 57),
            border_color_hover=color.WHITE,
            border_color_press=color.WHITE,
            font_size=22
        )
        self.ui_manager.add_ui_element(level_easy)

        level_medium = UIFlatButton(database.get_data("dictionary",
                                                      language,
                                                      "russian = 'Средний'")[0][0],
                                    center_x=400, center_y=SCREEN_HEIGHT - 325,
                                    width=180, height=100)
        level_medium.set_handler("on_click", self.medium)
        level_medium.set_style_attrs(
            font_color=color.WHITE,
            font_color_hover=color.WHITE,
            font_color_press=color.WHITE,
            bg_color=(255, 185, 10),
            bg_color_hover=(255, 185, 10),
            bg_color_press=(230, 160, 0),
            border_color=(255, 185, 10),
            border_color_hover=color.WHITE,
            border_color_press=color.WHITE,
            font_size=22
        )
        self.ui_manager.add_ui_element(level_medium)

        level_hard = UIFlatButton(database.get_data("dictionary",
                                                    language,
                                                    "russian = 'Сложный'")[0][0],
                                  center_x=600, center_y=SCREEN_HEIGHT - 325,
                                  width=180, height=100)
        level_hard.set_handler("on_click", self.hard)
        level_hard.set_style_attrs(
            font_color=color.WHITE,
            font_color_hover=color.WHITE,
            font_color_press=color.WHITE,
            bg_color=(155, 21, 25),
            bg_color_hover=(155, 21, 25),
            bg_color_press=(135, 21, 24),
            border_color=(155, 21, 25),
            border_color_hover=color.WHITE,
            border_color_press=color.WHITE,
            font_size=22
        )
        self.ui_manager.add_ui_element(level_hard)

        btn_russia = UIImageButton(center_x=300, center_y=100,
                                   normal_texture=load_texture(RUSSIA_IMAGE),
                                   press_texture=load_texture(RUSSIA_IMAGE_2))
        btn_russia.set_handler("on_click", self.russia)
        self.ui_manager.add_ui_element(btn_russia)

        btn_english = UIImageButton(center_x=500, center_y=100,
                                    normal_texture=load_texture(ENGLISH_IMAGE),
                                    press_texture=load_texture(ENGLISH_IMAGE_2))
        btn_english.set_handler("on_click", self.english)
        self.ui_manager.add_ui_element(btn_english)

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

    def russia(self):
        global language
        self.btn.play()
        database.change_data("player_info", "language = 'russian'")
        language = database.get_data("player_info", "language")[0][0]
        self.setup()

    def english(self):
        global language
        self.btn.play()
        database.change_data("player_info", "language = 'english'")
        language = database.get_data("player_info", "language")[0][0]
        self.setup()

    def on_show(self):
        set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.background = BACKGROUND
        self.coin = COIN
        self.star = STAR

    def on_draw(self):
        start_render()
        self.background.draw()
        self.coin.draw()
        self.star.draw()
        draw_text(str(count_coins), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 82, anchor_x="right",
                  color=color.WHITE, font_size=60, bold=True)
        draw_text(str(count_stars), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 165, anchor_x="right",
                  color=color.WHITE, font_size=60, bold=True)
        draw_text(database.get_data("dictionary",
                                    language,
                                    "russian = 'Сейчас выбран'")[0][0],
                  150,
                  300,
                  color=color.BABY_BLUE,
                  font_size=34)
        draw_text(database.get_data("dictionary",
                                    language,
                                    f"russian = '{level} уровень сложности'")[0][0],
                  150,
                  268,
                  color=color.BABY_BLUE,
                  font_size=34)
        self.cursor.draw()


class NewGameView(View):
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

        text = UILabel(database.get_data("dictionary",
                                         language,
                                         "russian = 'Вы точно хотите начать новую игру?'")[0][0],
                       center_x=SCREEN_WIDTH // 2,
                       center_y=SCREEN_HEIGHT - 100)
        text.set_style_attrs(font_color=color.BABY_BLUE, font_size=30)
        self.ui_manager.add_ui_element(text)

        btn_ok = UIFlatButton(database.get_data("dictionary",
                                                language,
                                                "russian = 'Да'")[0][0],
                              center_x=225, center_y=SCREEN_HEIGHT // 2 - 75,
                              width=225, height=100)
        btn_ok.set_handler("on_click", self.ok)
        btn_ok.set_style_attrs(
            font_color=color.WHITE,
            font_color_hover=color.WHITE,
            font_color_press=color.WHITE,
            bg_color=(51, 139, 57),
            bg_color_hover=(51, 139, 57),
            bg_color_press=(28, 71, 32),
            border_color=(51, 139, 57),
            border_color_hover=color.WHITE,
            border_color_press=color.WHITE,
            font_size=22
        )
        self.ui_manager.add_ui_element(btn_ok)

        btn_cancel = UIFlatButton(database.get_data("dictionary",
                                                    language,
                                                    "russian = 'Отмена'")[0][0],
                                  center_x=575, center_y=SCREEN_HEIGHT // 2 - 75,
                                  width=225, height=100)
        btn_cancel.set_handler("on_click", self.cancel)
        btn_cancel.set_style_attrs(
            font_color=color.WHITE,
            font_color_hover=color.WHITE,
            font_color_press=color.WHITE,
            bg_color=(135, 21, 25),
            bg_color_hover=(135, 21, 25),
            bg_color_press=(122, 21, 24),
            border_color=(135, 21, 25),
            border_color_hover=color.WHITE,
            border_color_press=color.WHITE,
            font_size=22
        )
        self.ui_manager.add_ui_element(btn_cancel)

    def ok(self):
        global count_coins, count_stars, all_levels, all_person, player
        self.btn_2.play(1.25)
        database.change_data("levels", "completed = 'False', all_coins = '+++', time = 'False'")
        database.change_data("persons", "received = 'False'", "id > 1")
        database.change_data("player_info", "person_id = 1, current_level = 'лёгкий', count_coins = 0")
        count_coins = database.get_data("player_info", "count_coins")[0][0]
        count_stars = think_stars(database.get_data("levels", "completed"))
        all_levels = database.get_data("levels")
        player = database.get_data("player_info, persons",
                                   "persons.path",
                                   "player_info.person_id = persons.id")[0][0]
        all_person = database.get_data("persons")
        self.cancel()

    def cancel(self):
        self.btn.play()
        self.ui_manager.purge_ui_elements()
        view = MainMenuView()
        self.window.show_view(view)

    def on_show(self):
        set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.background = BACKGROUND

    def on_draw(self):
        start_render()
        self.background.draw()
        draw_text(database.get_data("dictionary",
                                    language,
                                    "russian = 'Если вы начнёте новую игру,'")[0][0],
                  start_x=125, start_y=520, color=color.RED, font_size=30)
        draw_text(database.get_data("dictionary",
                                    language,
                                    "russian = 'то потеряете весь текущий прогресс!'")[0][0],
                  start_x=125, start_y=487, color=color.RED, font_size=30)
        self.cursor.draw()


class LevelsMenuView(View):
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
        self.text = database.get_data("dictionary",
                                      language,
                                      "russian = 'Время прохождения -'")[0][0]

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cursor.center_x = x
        self.cursor.center_y = y

    def setup(self):
        self.ui_manager.purge_ui_elements()

        btn_exit = UIImageButton(center_x=40, center_y=SCREEN_HEIGHT - 50,
                                 normal_texture=load_texture(DOOR),
                                 press_texture=load_texture(DOOR2))
        btn_exit.set_handler("on_click", self.exit)
        self.ui_manager.add_ui_element(btn_exit)

        btn_left = UIImageButton(center_x=50, center_y=SCREEN_HEIGHT // 2,
                                 normal_texture=load_texture(ARROW, flipped_horizontally=True),
                                 press_texture=load_texture(ARROW2, flipped_horizontally=True))
        btn_left.set_handler("on_click", self.left)
        self.ui_manager.add_ui_element(btn_left)

        btn_right = UIImageButton(center_x=SCREEN_WIDTH - 50, center_y=SCREEN_HEIGHT // 2,
                                  normal_texture=load_texture(ARROW),
                                  press_texture=load_texture(ARROW2))
        btn_right.set_handler("on_click", self.right)
        self.ui_manager.add_ui_element(btn_right)

        btn_play = UIFlatButton(database.get_data("dictionary",
                                                  language,
                                                  "russian = 'Играть'")[0][0],
                                center_x=SCREEN_WIDTH // 2,
                                center_y=SCREEN_HEIGHT // 2,
                                height=120, width=280)
        btn_play.set_handler("on_click", self.play)
        btn_play.set_style_attrs(
            font_color=color.WHITE,
            font_color_hover=color.WHITE,
            font_color_press=color.WHITE,
            bg_color=(51, 139, 57),
            bg_color_hover=(51, 139, 57),
            bg_color_press=(28, 71, 32),
            border_color=(51, 139, 57),
            border_color_hover=color.WHITE,
            border_color_press=color.WHITE,
            font_size=34
        )
        self.ui_manager.add_ui_element(btn_play)

    def set_star(self):
        self.time = all_levels[self.num_level][7]
        completed = all_levels[self.num_level][3]
        self.first_star = Sprite(STAR2_IMAGE, center_x=300, center_y=230)
        self.second_star = Sprite(STAR2_IMAGE, center_x=400, center_y=230)
        self.third_star = Sprite(STAR2_IMAGE, center_x=500, center_y=230)
        if completed == "лёгкий":
            self.first_star = Sprite(STAR_IMAGE, SCALING_STAR,
                                     center_x=300, center_y=230)
        elif completed == "средний":
            self.first_star = Sprite(STAR_IMAGE, SCALING_STAR,
                                     center_x=300, center_y=230)
            self.second_star = Sprite(STAR_IMAGE, SCALING_STAR,
                                      center_x=400, center_y=230)
        elif completed == "сложный":
            self.first_star = Sprite(STAR_IMAGE, SCALING_STAR,
                                     center_x=300, center_y=230)
            self.second_star = Sprite(STAR_IMAGE, SCALING_STAR,
                                      center_x=400, center_y=230)
            self.third_star = Sprite(STAR_IMAGE, SCALING_STAR,
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

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.LEFT:
            self.left()
        elif symbol == key.RIGHT:
            self.right()

    def on_show(self):
        set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.background = BACKGROUND2
        self.coin = COIN
        self.star = STAR

    def on_draw(self):
        start_render()
        self.background.draw()
        self.coin.draw()
        self.star.draw()
        self.first_star.draw()
        self.second_star.draw()
        self.third_star.draw()
        draw_text(str(count_coins), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 82, anchor_x="right",
                  color=color.WHITE, font_size=60, bold=True)
        draw_text(str(count_stars), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 165, anchor_x="right",
                  color=color.WHITE, font_size=60, bold=True)
        draw_text(all_levels[self.num_level][1], start_x=SCREEN_WIDTH // 2, start_y=SCREEN_HEIGHT - 200,
                  anchor_x="center", color=color.ORANGE, font_size=44, font_name="")
        count = all_levels[self.num_level][4].count("-")
        textt = database.get_data("dictionary",
                                  language,
                                  "russian = 'Собрано монет на уровне:'")[0][0]
        text = f"{textt} {count}"
        if count == 3:
            text = database.get_data("dictionary",
                                     language,
                                     "russian = 'На уровне уже собраны все монеты'")[0][0]
        draw_text(text=text,
                  start_x=SCREEN_WIDTH // 2,
                  start_y=SCREEN_HEIGHT - 260,
                  anchor_x="center", color=color.YELLOW_ORANGE,
                  font_size=24, font_name="")
        if self.time != "False":
            draw_text(f"{self.text} {self.time}",
                      SCREEN_WIDTH / 2,
                      100,
                      color.BABY_BLUE,
                      font_size=32,
                      anchor_x="center")

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


class GameView(View):
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
        self.all_sprites = SpriteList()
        self.hearts = SpriteList()
        self.coins = SpriteList()
        self.coins_list = []
        self.get_coin = []
        self.floors = SpriteList()
        self.walls = SpriteList()
        self.horizontal_enemies = SpriteList()
        self.vertical_enemies = SpriteList()
        self.player = None
        self.exitt = None
        self.music = BACKGROUND_SOUND
        self.coin_sound = COINS_SOUND
        self.hit_sound = HIT_SOUND
        self.died_sound = DIED_SOUND
        self.win_sound = WIN_SOUND
        self.count_coin = 0
        self.time_after_hit = 0.7
        self.time_level = 0
        self.text = database.get_data("dictionary",
                                      language,
                                      "russian = 'Монет собрано:'")[0][0]
        self.light_layer = LightLayer(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.light = None
        self.setup()

    def setup(self):
        self.play_song()

        for i in range(1, 4):
            heart = Sprite(HEART_IMAGE,
                           center_x=SCREEN_WIDTH - i * 40,
                           center_y=SCREEN_HEIGHT - 25)
            self.hearts.append(heart)
            self.all_sprites.append(heart)

        for y, string in enumerate(self.level):
            for x, column in enumerate(string):
                if column in ".@123OEV":
                    floor = Sprite(f"images/{self.floor_image}",
                                   center_x=x * TILE_SIZE + TILE_SIZE // 2,
                                   center_y=(len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 2)
                    self.floors.append(floor)
                    self.all_sprites.append(floor)
                elif column == "#":
                    wall = Sprite(f"images/{self.wall_image}",
                                  center_x=x * TILE_SIZE + TILE_SIZE // 2,
                                  center_y=(len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 2)
                    self.walls.append(wall)
                    self.all_sprites.append(wall)

        for y, string in enumerate(self.level):
            for x, column in enumerate(string):
                if column == "E":
                    self.exitt = Sprite(EXIT_IMAGE,
                                        center_x=x * TILE_SIZE + TILE_SIZE // 2,
                                        center_y=(len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 2.2,
                                        scale=0.35)
                    self.all_sprites.append(self.exitt)
                elif column in "123":
                    textures = [load_texture(COIN_IMAGE),
                                load_texture(COIN_IMAGE_2),
                                load_texture(COIN_IMAGE_3),
                                load_texture(COIN_IMAGE_4),
                                load_texture(COIN_IMAGE_3, mirrored=True),
                                load_texture(COIN_IMAGE_2, mirrored=True)]
                    coin = Coin(textures)
                    coin.center_x = x * TILE_SIZE + TILE_SIZE // 2
                    coin.center_y = (len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 2
                    coin.scale = 0.7
                    self.coins_list.append(int(column))
                    self.coins.append(coin)
                    self.all_sprites.append(coin)
                elif column == "O":
                    textures = [load_texture(f"{ENEMY_IMAGE}_walk{i}.png",
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
                    self.light = Light(x * TILE_SIZE + TILE_SIZE // 2,
                                       (len(self.level) - y - 1) * TILE_SIZE + TILE_SIZE // 2,
                                       150, color.WHITE, 'soft')
                    self.light_layer.add(self.light)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.ESCAPE:
            view = PauseView(self, self.data_level)
            self.window.show_view(view)
        elif symbol == key.LEFT:
            self.player.center_x -= 50
            if self.player.collides_with_list(self.walls) or self.player.left <= 0:
                self.player.center_x += 50
            self.player.index(2)
        elif symbol == key.RIGHT:
            self.player.center_x += 50
            if self.player.collides_with_list(self.walls) or self.player.right >= SCREEN_WIDTH:
                self.player.center_x -= 50
            self.player.index(1)
        elif symbol == key.UP:
            self.player.center_y += 50
            if self.player.collides_with_list(self.walls) or self.player.top >= SCREEN_HEIGHT - 50:
                self.player.center_y -= 50
            self.player.index(3)
        elif symbol == key.DOWN:
            self.player.center_y -= 50
            if self.player.collides_with_list(self.walls) or self.player.bottom <= 0:
                self.player.center_y += 50
            self.player.index(0)

    def play_song(self):
        self.current_player = self.music.play(MUSIC_VOLUME)
        sleep(0.03)

    def to_sec(self, time):
        time = list(map(int, time.split(":")))
        new_time = time[0] * 60 + time[1] + time[2] / 100
        return new_time

    def on_update(self, delta_time: float):
        global all_levels, count_coins, count_stars
        self.time_level += delta_time
        self.time_after_hit += delta_time
        self.coins.update()
        self.vertical_enemies.update()
        self.horizontal_enemies.update()
        self.player.update()
        self.light.position = self.player.position
        if self.player.collides_with_sprite(self.exitt):
            if help_dict_for_stars[level] >= help_dict_for_stars[self.completed]:
                database.change_data("levels",
                                     f"completed = '{level}'",
                                     data_criterion=f"id = {self.id}")
                if len(self.get_coin) > self.level_coins.count("-"):
                    x = len(self.get_coin) - self.level_coins.count("-")
                    for i in self.get_coin:
                        self.level_coins[i - 1] = "-"
                    database.change_data("levels",
                                         f"all_coins = '{''.join(self.level_coins)}'",
                                         data_criterion=f"id = {self.id}")
                    count_coins += x
                    database.change_data("player_info", f"count_coins = {count_coins}")
            time_old = database.get_data("levels", "time", data_criterion=f"id = {self.id}")[0][0]
            millis = str(round(self.time_level % 1, 2))[2:]
            if time_old == "False" \
                    or self.to_sec(f"{int(self.time_level // 60)}:{floor(self.time_level % 60)}:{millis}") \
                    < self.to_sec(time_old):
                database.change_data("levels",
                                     f"time = '{int(self.time_level // 60)}:{floor(self.time_level % 60)}:{millis}'",
                                     data_criterion=f"id = {self.id}")
            all_levels = database.get_data("levels")
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
                textures = [load_texture(f"{ENEMY_IMAGE}_walk{i}.png",
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
        set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        start_render()
        with self.light_layer:
            self.all_sprites.draw()
        self.light_layer.draw(ambient_color=(5, 5, 5))
        draw_text(f"{self.text} {self.count_coin}",
                  start_x=25, start_y=SCREEN_HEIGHT - 40,
                  color=color.ORANGE, font_size=24)
        millis = str(round(self.time_level % 1, 2))[2:]
        draw_text(f"{int(self.time_level // 60)}:{floor(self.time_level % 60)}:{millis}",
                  SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 45, color=color.WHITE, font_size=30)
        self.hearts.draw()


class PauseView(View):
    def __init__(self, game_view, data_level):
        super().__init__()
        self.game_view = game_view
        self.data_level = data_level
        self.text_1 = database.get_data("dictionary",
                                        language,
                                        "russian = 'ПАУЗА'")[0][0]
        self.text_2 = database.get_data("dictionary",
                                        language,
                                        "russian = 'Нажмите Enter, чтобы вернуться в меню.'")[0][0]
        self.text_3 = database.get_data("dictionary",
                                        language,
                                        "russian = 'Весь прогресс будет потерян!'")[0][0]
        self.text_4 = database.get_data("dictionary",
                                        language,
                                        "russian = 'Нажмите Esc, чтобы вернуться в игру.'")[0][0]
        self.text_5 = database.get_data("dictionary",
                                        language,
                                        "russian = 'Нажмите R, чтобы перезапустить уровень.'")[0][0]

    def on_show(self):
        set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        start_render()

        self.game_view.all_sprites.draw()
        draw_text(f"{self.game_view.text} {self.game_view.count_coin}",
                  start_x=25, start_y=SCREEN_HEIGHT - 40,
                  color=color.ORANGE, font_size=24)
        millis = str(round(self.game_view.time_level % 1, 2))[2:]
        draw_text(f"{int(self.game_view.time_level // 60)}:{floor(self.game_view.time_level % 60)}:{millis}",
                  SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 45, color=color.WHITE, font_size=30)

        draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0,
                                   color.BABY_BLUE + (175,))
        draw_text(self.text_1,
                  SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 2 + 150,
                  color.BLACK, font_size=50, anchor_x="center")
        draw_text(self.text_2,
                  SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 2,
                  color.BLACK,
                  font_size=24,
                  anchor_x="center")
        draw_text(self.text_3,
                  SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 2 - 30,
                  color.BLACK,
                  font_size=24,
                  anchor_x="center")
        draw_text(self.text_4,
                  SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 2 - 80,
                  color.BLACK,
                  font_size=24,
                  anchor_x="center")
        draw_text(self.text_5,
                  SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 2 - 160,
                  color.BLACK,
                  font_size=24,
                  anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.ESCAPE:
            self.window.show_view(self.game_view)
        elif symbol == key.R:
            self.game_view.off_music()
            view = GameView(self.data_level)
            self.window.show_view(view)
        elif symbol == key.ENTER:
            self.game_view.off_music()
            view = LevelsMenuView(self.data_level[0] - 1)
            self.window.show_view(view)


class GameEndView(View):
    def __init__(self, game_view, data_level):
        super().__init__()
        self.game_view = game_view
        self.data_level = data_level
        self.text_1 = database.get_data("dictionary",
                                        language,
                                        "russian = 'ПРОИГРЫШ'")[0][0]
        self.text_2 = database.get_data("dictionary",
                                        language,
                                        "russian = 'Нажмите Enter, чтобы вернуться в меню.'")[0][0]
        self.text_3 = database.get_data("dictionary",
                                        language,
                                        "russian = 'Нажмите R, чтобы перезапустить уровень.'")[0][0]

    def on_show(self):
        set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        start_render()

        draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0,
                                   color.RED_DEVIL)
        draw_text(self.text_1,
                  SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 2 + 150,
                  color.BLACK, font_size=50, anchor_x="center")
        draw_text(self.text_2,
                  SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 2,
                  color.BLACK,
                  font_size=24,
                  anchor_x="center")
        draw_text(self.text_3,
                  SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 2 - 80,
                  color.BLACK,
                  font_size=24,
                  anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.R:
            self.game_view.off_music()
            view = GameView(self.data_level)
            self.window.show_view(view)
        elif symbol == key.ENTER:
            self.game_view.off_music()
            view = LevelsMenuView(self.data_level[0] - 1)
            self.window.show_view(view)


class GameWinView(View):
    def __init__(self, game_view, data_level):
        super().__init__()
        self.game_view = game_view
        self.data_level = data_level
        self.text_1 = database.get_data("dictionary",
                                        language,
                                        "russian = 'Вы собрали'")[0][0]
        self.text_2 = database.get_data("dictionary",
                                        language,
                                        "russian = 'монет'")[0][0]
        self.text_3 = database.get_data("dictionary",
                                        language,
                                        "russian = 'ПОБЕДА'")[0][0]
        self.text_4 = database.get_data("dictionary",
                                        language,
                                        "russian = 'Нажмите Enter, чтобы вернуться в меню.'")[0][0]
        self.text_5 = database.get_data("dictionary",
                                        language,
                                        "russian = 'Нажмите R, чтобы перезапустить уровень.'")[0][0]
        self.text_6 = database.get_data("dictionary",
                                        language,
                                        "russian = 'Уровень пройден на уровне сложности -'")[0][0]
        self.text_7 = database.get_data("dictionary",
                                        language,
                                        f"russian = '{level.capitalize()}'")[0][0]
        self.text_8 = database.get_data("dictionary",
                                        language,
                                        "russian = 'Время прохождения -'")[0][0]
        self.millis = str(round(self.game_view.time_level % 1, 2))[2:]

    def on_show(self):
        set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        start_render()

        draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0,
                                   color.GREEN)
        draw_text(self.text_3,
                  SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 2 + 150,
                  color.BLACK, font_size=50, anchor_x="center")
        draw_text(f"{self.text_1} {self.game_view.count_coin} {self.text_2}!",
                  SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 2,
                  color.BLACK,
                  font_size=24,
                  anchor_x="center")
        draw_text(f'{self.text_6} "{self.text_7.lower()}"',
                  SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 2 - 80,
                  color.BLACK,
                  font_size=24,
                  anchor_x="center")
        draw_text(f"{self.text_8} {int(self.game_view.time_level // 60)}:"
                  f"{floor(self.game_view.time_level % 60)}:{self.millis}",
                  SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 2 - 160,
                  color.BLACK,
                  font_size=24,
                  anchor_x="center")
        draw_text(self.text_4,
                  SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 2 - 240,
                  color.BLACK,
                  font_size=24,
                  anchor_x="center")
        draw_text(self.text_5,
                  SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 2 - 320,
                  color.BLACK,
                  font_size=24,
                  anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.R:
            self.game_view.off_music()
            view = GameView(self.data_level)
            self.window.show_view(view)
        elif symbol == key.ENTER:
            self.game_view.off_music()
            view = LevelsMenuView(self.data_level[0] - 1)
            self.window.show_view(view)


class InstructionView(View):
    def __init__(self):
        super(InstructionView, self).__init__()
        self.background = None
        self.coin = None
        self.star = None
        self.ui_manager = UIManager(self.window)
        self.setup()
        self.cursor = CURSOR
        self.btn_instruction = SETTINGS_SOUND
        self.text_1 = database.get_data("dictionary",
                                        language,
                                        "russian = '- игра с множеством уровней,'")[0][0]
        self.text_2 = database.get_data("dictionary",
                                        language,
                                        "russian = 'для прохождения которых нужно выйти из лабиринта.'")[0][0]
        text = 'На один уровень у вас есть 3 "сердчека" - жизни.'
        self.text_3 = database.get_data("dictionary",
                                        language,
                                        f"russian = '{text}'")[0][0]
        self.text_4 = database.get_data("dictionary",
                                        language,
                                        "russian = 'В зависимости от уровня сложности'")[0][0]
        self.text_5 = database.get_data("dictionary",
                                        language,
                                        "russian = 'противники в лабиринте наносят разный урон.'")[0][0]
        text_2 = 'Если "сердечки" закончатся -'
        self.text_6 = database.get_data("dictionary",
                                        language,
                                        f"russian = '{text_2}'")[0][0]
        self.text_7 = database.get_data("dictionary",
                                        language,
                                        "russian = 'вы потеряете весь прогресс на данном уровне.'")[0][0]

    def setup(self):
        self.ui_manager.purge_ui_elements()

        text = UILabel(database.get_data("dictionary",
                                         language,
                                         "russian = 'Об игре'")[0][0],
                       center_x=SCREEN_WIDTH // 2,
                       center_y=SCREEN_HEIGHT - 100)
        text.set_style_attrs(font_color=color.BABY_BLUE, font_size=44)
        self.ui_manager.add_ui_element(text)

        btn_instruction = UIImageButton(center_x=50,
                                        center_y=45,
                                        normal_texture=load_texture(INSTRUCTION_IMAGE),
                                        press_texture=load_texture(INSTRUCTION_IMAGE_2))
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
        set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.background = BACKGROUND
        self.coin = COIN
        self.star = STAR

    def on_draw(self):
        start_render()
        self.background.draw()
        self.coin.draw()
        self.star.draw()
        draw_text(str(count_coins),
                  SCREEN_WIDTH - 80,
                  SCREEN_HEIGHT - 82,
                  anchor_x="right",
                  color=color.WHITE,
                  font_size=60,
                  bold=True)
        draw_text(str(count_stars),
                  SCREEN_WIDTH - 80,
                  SCREEN_HEIGHT - 165,
                  anchor_x="right",
                  color=color.WHITE,
                  font_size=60,
                  bold=True)
        draw_text(f"{SCREEN_TITLE} {self.text_1}",
                  SCREEN_WIDTH // 2, 530,
                  color=color.BABY_BLUE,
                  font_size=24,
                  anchor_x="center")
        draw_text(self.text_2,
                  SCREEN_WIDTH // 2, 500,
                  color=color.BABY_BLUE,
                  font_size=24,
                  anchor_x="center")
        draw_text(self.text_3,
                  SCREEN_WIDTH // 2 + 80, 400,
                  color=color.BABY_BLUE,
                  font_size=24,
                  anchor_x="center")
        draw_text(self.text_4,
                  SCREEN_WIDTH // 2 + 80, 370,
                  color=color.BABY_BLUE,
                  font_size=24,
                  anchor_x="center")
        draw_text(self.text_5,
                  SCREEN_WIDTH // 2 + 80, 340,
                  color=color.BABY_BLUE,
                  font_size=24,
                  anchor_x="center")
        draw_text(self.text_6,
                  SCREEN_WIDTH // 2 - 50, 270,
                  color=color.BABY_BLUE,
                  font_size=24,
                  anchor_x="center")
        draw_text(self.text_7,
                  SCREEN_WIDTH // 2 - 50, 240,
                  color=color.BABY_BLUE,
                  font_size=24,
                  anchor_x="center")
        self.cursor.draw()


class ShopView(View):
    def __init__(self):
        super(ShopView, self).__init__()
        self.background = None
        self.coin = None
        self.star = None
        self.time_buy = 3
        self.ui_manager = UIManager(self.window)
        self.cursor = CURSOR
        self.btn_shop = BUTTON_SOUND
        self.btn = BUTTON_SOUND_2
        self.person = PERSON_SOUND
        self.num_person = 0
        self.path = ":resources:images/animated_characters/"
        self.person_image = Sprite(self.path + all_person[self.num_person][2]
                                   + "_idle.png",
                                   center_x=SCREEN_WIDTH // 2,
                                   center_y=SCREEN_HEIGHT // 2 + 50, scale=3)
        self.setup()

    def update(self, delta_time: float):
        self.time_buy += delta_time

    def setup(self):
        self.ui_manager.purge_ui_elements()

        btn_left = UIImageButton(center_x=50, center_y=SCREEN_HEIGHT // 2,
                                 normal_texture=load_texture(ARROW, flipped_horizontally=True),
                                 press_texture=load_texture(ARROW2, flipped_horizontally=True))
        btn_left.set_handler("on_click", self.left)
        self.ui_manager.add_ui_element(btn_left)

        btn_right = UIImageButton(center_x=SCREEN_WIDTH - 50, center_y=SCREEN_HEIGHT // 2,
                                  normal_texture=load_texture(ARROW),
                                  press_texture=load_texture(ARROW2))
        btn_right.set_handler("on_click", self.right)
        self.ui_manager.add_ui_element(btn_right)

        btn_shop = UIImageButton(center_x=SCREEN_WIDTH - 50,
                                 center_y=45,
                                 normal_texture=load_texture(SHOP_IMAGE),
                                 press_texture=load_texture(SHOP_IMAGE_2))
        btn_shop.set_handler("on_click", self.shop)
        self.ui_manager.add_ui_element(btn_shop)

        text = UILabel(database.get_data("dictionary",
                                         language,
                                         f"russian = '{all_person[self.num_person][1]}'")[0][0],
                       center_x=SCREEN_WIDTH // 2,
                       center_y=SCREEN_HEIGHT - 120)
        text.set_style_attrs(font_color=color.BABY_BLUE, font_size=54)
        self.ui_manager.add_ui_element(text)

        if player == all_person[self.num_person][2]:
            text = UILabel(database.get_data("dictionary",
                                             language,
                                             "russian = 'Выбрано'")[0][0],
                           center_x=SCREEN_WIDTH // 2,
                           center_y=SCREEN_HEIGHT // 2 - 270)
            text.set_style_attrs(font_color=color.WHITE, font_size=34)
            self.ui_manager.add_ui_element(text)
        else:
            if all_person[self.num_person][4] == "True":
                btn_select = UIFlatButton(database.get_data("dictionary",
                                                            language,
                                                            "russian = 'Выбрать'")[0][0],
                                          center_x=SCREEN_WIDTH // 2,
                                          center_y=SCREEN_HEIGHT // 2 - 270,
                                          height=120, width=250)
                btn_select.set_handler("on_click", self.select)
                btn_select.set_style_attrs(
                    font_color=color.WHITE,
                    font_color_hover=color.WHITE,
                    font_color_press=color.WHITE,
                    bg_color=(51, 139, 57),
                    bg_color_hover=(51, 139, 57),
                    bg_color_press=(28, 71, 32),
                    border_color=(51, 139, 57),
                    border_color_hover=color.WHITE,
                    border_color_press=color.WHITE,
                    font_size=34
                )
                self.ui_manager.add_ui_element(btn_select)
            elif all_person[self.num_person][4] == "False":
                textt = database.get_data("dictionary",
                                          language,
                                          "russian = 'Этот персонаж "
                                          "стоит'")[0][0] \
                        + " " + str(all_person[self.num_person][3]) + " " \
                        + database.get_data("dictionary",
                                            language,
                                            "russian = 'монет'")[0][0]
                text = UILabel(textt,
                               center_x=SCREEN_WIDTH // 2,
                               center_y=SCREEN_HEIGHT // 2 - 165)
                text.set_style_attrs(font_color=color.WHITE, font_size=34)
                self.ui_manager.add_ui_element(text)

                btn_buy = UIFlatButton(database.get_data("dictionary",
                                                         language,
                                                         "russian = 'Купить'")[0][0],
                                       center_x=SCREEN_WIDTH // 2,
                                       center_y=SCREEN_HEIGHT // 2 - 270,
                                       height=120, width=250)
                btn_buy.set_handler("on_click", self.buy)
                btn_buy.set_style_attrs(
                    font_color=color.WHITE,
                    font_color_hover=color.WHITE,
                    font_color_press=color.WHITE,
                    bg_color=(135, 21, 25),
                    bg_color_hover=(135, 21, 25),
                    bg_color_press=(122, 21, 24),
                    border_color=(135, 21, 25),
                    border_color_hover=color.WHITE,
                    border_color_press=color.WHITE,
                    font_size=34
                )
                self.ui_manager.add_ui_element(btn_buy)

    def select(self):
        global player
        self.person.play()
        database.change_data("player_info", f"person_id = {all_person[self.num_person][0]}")
        player = database.get_data("player_info, persons",
                                   "persons.path",
                                   "player_info.person_id = persons.id")[0][0]
        self.setup()

    def buy(self):
        global count_coins, player, all_person
        if count_coins >= all_person[self.num_person][3]:
            self.person.play()
            count_coins -= all_person[self.num_person][3]
            database.change_data("player_info", f"count_coins = {count_coins}")
            database.change_data("persons", "received = 'True'",
                                 f"id = {all_person[self.num_person][0]}")
            database.change_data("player_info",
                                 f"person_id = {all_person[self.num_person][0]}")
            all_person = database.get_data("persons")
            player = database.get_data("player_info, persons",
                                       "persons.path",
                                       "player_info.person_id = persons.id")[0][0]
            self.setup()
        else:
            self.time_buy = 0

    def shop(self):
        self.btn_shop.play()
        self.ui_manager.purge_ui_elements()
        view = MainMenuView()
        self.window.show_view(view)

    def left(self):
        self.btn.play()
        if self.num_person == 0:
            self.num_person = len(all_person) - 1
        else:
            self.num_person -= 1
        self.setup()
        self.person_image = Sprite(self.path + all_person[self.num_person][2]
                                   + "_idle.png",
                                   center_x=SCREEN_WIDTH // 2,
                                   center_y=SCREEN_HEIGHT // 2 + 50, scale=3)

    def right(self):
        self.btn.play()
        if self.num_person == len(all_person) - 1:
            self.num_person = 0
        else:
            self.num_person += 1
        self.setup()
        self.person_image = Sprite(self.path + all_person[self.num_person][2]
                                   + "_idle.png",
                                   center_x=SCREEN_WIDTH // 2,
                                   center_y=SCREEN_HEIGHT // 2 + 50, scale=3)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.LEFT:
            self.left()
        elif symbol == key.RIGHT:
            self.right()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cursor.center_x = x
        self.cursor.center_y = y

    def on_show(self):
        set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.background = BACKGROUND2
        self.coin = COIN
        self.star = STAR

    def on_draw(self):
        start_render()
        self.background.draw()
        self.coin.draw()
        self.star.draw()
        draw_text(str(count_coins), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 82, anchor_x="right",
                  color=color.WHITE, font_size=60, bold=True)
        draw_text(str(count_stars), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 165, anchor_x="right",
                  color=color.WHITE, font_size=60, bold=True)
        if self.time_buy < 3:
            draw_text(database.get_data("dictionary",
                                        language,
                                        "russian = 'Недостаточно монет!'")[0][0],
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80,
                      anchor_x="center",
                      color=color.RED, font_size=40, bold=True)
        self.person_image.draw()
        self.cursor.draw()
