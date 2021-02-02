from arcade import Sprite

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Бродилка"
SCALING_BACKGROUND = 0.8
SCALING_BACKGROUND2 = 1.07
BACKGROUND = Sprite("images/background2.jpg", SCALING_BACKGROUND,
                    center_x=SCREEN_WIDTH // 2, center_y=SCREEN_HEIGHT // 2)
BACKGROUND2 = Sprite("images/background.jpg", SCALING_BACKGROUND2,
                     center_x=SCREEN_WIDTH // 2, center_y=SCREEN_HEIGHT // 2)
COIN = Sprite(":resources:images/items/gold_1.png",
              center_x=SCREEN_WIDTH - 40, center_y=SCREEN_HEIGHT - 40)
SETTINGS = "images/settings.png"
SETTINGS2 = "images/settings2.png"
STAR_IMAGE = ":resources:images/items/star.png"
STAR = Sprite(STAR_IMAGE, scale=1.05, center_x=SCREEN_WIDTH - 40,
              center_y=SCREEN_HEIGHT - 120)
DOOR = "images/door.png"
DOOR2 = "images/door2.png"
ARROW = "images/arrow.png"
ARROW2 = "images/arrow2.png"
CURSOR = Sprite("images/cursor.png", 0.11)
STAR2_IMAGE = "images/star.png"
SCALING_STAR = 1.3
