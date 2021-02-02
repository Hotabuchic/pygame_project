import arcade
from arcade.gui import UIManager, UILabel, UIFlatButton, UIImageButton

from constants import *
from databse import DataBase

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


class MainMenuView(arcade.View):
    def __init__(self):
        super(MainMenuView, self).__init__()
        self.background = None
        self.coin = None
        self.star = None
        self.ui_manager = UIManager(self.window)
        self.setup()
        self.cursor = CURSOR

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
        self.ui_manager.purge_ui_elements()
        view = NewGameView()
        self.window.show_view(view)

    def resume(self):
        self.ui_manager.purge_ui_elements()
        view = LevelsMenuView()
        self.window.show_view(view)

    def end(self):
        arcade.close_window()

    def settings(self):
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
        self.ui_manager.add_ui_element(level_easy)

        level_medium = UIFlatButton("Средний",
                                    center_x=400, center_y=SCREEN_HEIGHT - 325,
                                    width=180, height=100)
        level_medium.set_handler("on_click", self.medium)
        self.ui_manager.add_ui_element(level_medium)

        level_hard = UIFlatButton("Сложный",
                                  center_x=600, center_y=SCREEN_HEIGHT - 325,
                                  width=180, height=100)
        level_hard.set_handler("on_click", self.hard)
        self.ui_manager.add_ui_element(level_hard)

    def easy(self):
        global level
        database.change_data("player_info", "current_level = 'лёгкий'")
        level = database.get_data("player_info", "current_level")[0][0]

    def medium(self):
        global level
        database.change_data("player_info", "current_level = 'средний'")
        level = database.get_data("player_info", "current_level")[0][0]

    def hard(self):
        global level
        database.change_data("player_info", "current_level = 'сложный'")
        level = database.get_data("player_info", "current_level")[0][0]

    def settings(self):
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
        database.change_data("levels", "completed = 'False', all_coins = '+++'")
        database.change_data("player_info", "count_coins = 0")
        count_coins = database.get_data("player_info", "count_coins")[0][0]
        self.cancel()

    def cancel(self):
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
        self.ui_manager.purge_ui_elements()
        view = GameView(all_levels[self.num_level])
        self.window.show_view(view)

    def exit(self):
        self.ui_manager.purge_ui_elements()
        view = MainMenuView()
        self.window.show_view(view)

    def left(self):
        if self.num_level == 0:
            self.num_level = len(all_levels) - 1
        else:
            self.num_level -= 1
        self.set_star()

    def right(self):
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


class GameView(arcade.View):
    def __init__(self, data_level):
        super(GameView, self).__init__()
        self.data_level = data_level
        self.setup()

    def setup(self):
        pass

    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        arcade.start_render()
