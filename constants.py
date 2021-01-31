from arcade import Sprite

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Бродилка"
SCALING = 0.5
SCALING_BACKGROUND = 0.8
BACKGROUND = Sprite("images/background2.jpg", SCALING_BACKGROUND,
                    center_x=SCREEN_WIDTH // 2, center_y=SCREEN_HEIGHT // 2)
COIN = Sprite(":resources:images/items/gold_1.png",
              center_x=SCREEN_WIDTH - 40, center_y=SCREEN_HEIGHT - 40)
SETTINGS = "images/settings.png"
SETTINGS2 = "images/settings2.png"
