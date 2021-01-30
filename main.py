import arcade
from pygame import init, quit

from constants import *
from introduction import IntroductionView

init()
quit()


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = IntroductionView()
    window.show_view(view)
    arcade.run()


if __name__ == '__main__':
    main()
