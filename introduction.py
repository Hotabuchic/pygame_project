import arcade
from constants import *
from menu import MainMenuView


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
        self.background = BACKGROUND

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        arcade.draw_text(SCREEN_TITLE, SCREEN_WIDTH // 2,
                         SCREEN_HEIGHT // 2, arcade.color.WHITE_SMOKE, anchor_x="center", font_size=50)
        arcade.draw_text("Нажмите любую кнопку чтобы продолжить", SCREEN_WIDTH // 2,
                         SCREEN_HEIGHT // 2 - 80, arcade.color.RED, anchor_x="center", font_size=20)
        self.cursor.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        view = MainMenuView()
        self.window.show_view(view)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        view = MainMenuView()
        self.window.show_view(view)