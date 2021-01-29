import arcade
from arcade.gui import UIManager, UILabel, UIFlatButton, UIImageButton

from constants import *


class MainMenuView(arcade.View):
    def __init__(self):
        super(MainMenuView, self).__init__()
        self.ui_manager = UIManager(self.window)
        self.setup()

    def setup(self):
        self.ui_manager.purge_ui_elements()

        text = UILabel("Главное меню",
                       center_x=SCREEN_WIDTH // 2,
                       center_y=SCREEN_HEIGHT - 100)
        text.set_style_attrs(font_color=arcade.color.BABY_BLUE)
        self.ui_manager.add_ui_element(text)

        btn_new = UIFlatButton("Новая игра", center_x=SCREEN_WIDTH // 2, center_y=SCREEN_HEIGHT // 1.5)
        btn_new.set_handler("on_click", self.new_game)
        self.ui_manager.add_ui_element(btn_new)

        btn_resume = UIFlatButton("Продолжить", center_x=SCREEN_WIDTH // 2, center_y=SCREEN_HEIGHT // 1.75)
        btn_resume.set_handler("on_click", self.resume)
        self.ui_manager.add_ui_element(btn_resume)

        btn_end = UIFlatButton("Выйти из игры", center_x=SCREEN_WIDTH // 2, center_y=SCREEN_HEIGHT // 2)
        btn_end.set_handler("on_click", self.end)
        self.ui_manager.add_ui_element(btn_end)

        btn_settings = UIFlatButton("Настройки", center_x=SCREEN_WIDTH // 2, center_y=SCREEN_HEIGHT // 2.25)
        btn_settings.set_style_attrs(
            bg_color=(51, 139, 57),
            bg_color_hover=(51, 139, 57),
            bg_color_press=(28, 71, 32),
            border_color=(51, 139, 57),
        )
        btn_settings.set_handler("on_click", self.settings)
        self.ui_manager.add_ui_element(btn_settings)
        print(help(arcade.load_texture))

        btn_settings2 = UIImageButton(center_x=SCREEN_WIDTH - 35, center_y=SCREEN_HEIGHT - 35,
                                      normal_texture=arcade.load_texture("images/settings2.png"))
        self.ui_manager.add_ui_element(btn_settings2)

    def new_game(self):
        pass

    def resume(self):
        pass

    def end(self):
        arcade.close_window()

    def settings(self):
        pass

    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.background = arcade.Sprite("images/background2.jpg", SCALING_BACKGROUND,
                                        center_x=SCREEN_WIDTH // 2, center_y=SCREEN_HEIGHT // 2)

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
