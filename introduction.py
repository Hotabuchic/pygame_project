import arcade

from constants import *
from databse import DataBase
from menu import MainMenuView

database = DataBase()
language = database.get_data("player_info", "language")[0][0]


class IntroductionView(arcade.View):
    def __init__(self):
        super(IntroductionView, self).__init__()
        self.window.set_mouse_visible(False)
        self.background = None
        self.cursor = CURSOR
        self.start_load = START_LOAD_SOUND
        self.start_load.play(1.5)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cursor.center_x = x
        self.cursor.center_y = y

    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.background = LOGO

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        arcade.draw_text(database.get_data("dictionary",
                                           language,
                                           "russian = 'Нажмите любую кнопку чтобы продолжить'")[0][0],
                         SCREEN_WIDTH // 2,
                         100,
                         arcade.color.RED,
                         anchor_x="center",
                         font_size=20)
        self.cursor.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        view = MainMenuView()
        self.window.show_view(view)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        view = MainMenuView()
        self.window.show_view(view)
