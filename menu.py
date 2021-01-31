import arcade
from arcade.gui import UIManager, UILabel, UIFlatButton, UIImageButton

from constants import *
from databse import DataBase

database = DataBase()
count_coins = database.get_data("player_info", "count_coins")[0][0]
level = database.get_data("player_info", "current_level")[0][0]


class MainMenuView(arcade.View):
    def __init__(self):
        super(MainMenuView, self).__init__()
        self.background = None
        self.coin = None
        self.ui_manager = UIManager(self.window)
        self.setup()

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
        pass

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

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.coin.draw()
        arcade.draw_text(str(count_coins), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 82, anchor_x="right",
                         color=arcade.color.WHITE, font_size=60, bold=True)


class SettingsView(arcade.View):
    def __init__(self):
        super(SettingsView, self).__init__()
        self.background = None
        self.coin = None
        self.ui_manager = UIManager(self.window)
        self.setup()

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

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.coin.draw()
        arcade.draw_text(str(count_coins), SCREEN_WIDTH - 80, SCREEN_HEIGHT - 82, anchor_x="right",
                         color=arcade.color.WHITE, font_size=60, bold=True)
        arcade.draw_text(f"Сейчас выбран\n{level} уровень сложности", 150, 300,
                         color=arcade.color.BABY_BLUE, font_size=34)


class NewGameView(arcade.View):
    def __init__(self):
        super(NewGameView, self).__init__()
        self.background = None
        self.ui_manager = UIManager(self.window)
        self.setup()

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
