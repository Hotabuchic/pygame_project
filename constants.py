from arcade import Sprite, Sound

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Baby Blue"
SCALING_BACKGROUND = 0.8
SCALING_BACKGROUND2 = 1.07
BACKGROUND = Sprite("images/background2.jpg", SCALING_BACKGROUND,
                    center_x=SCREEN_WIDTH // 2, center_y=SCREEN_HEIGHT // 2)
BACKGROUND2 = Sprite("images/background.jpg", SCALING_BACKGROUND2,
                     center_x=SCREEN_WIDTH // 2, center_y=SCREEN_HEIGHT // 2)
COIN_IMAGE = ":resources:images/items/gold_1.png"
COIN_IMAGE_2 = ":resources:images/items/gold_2.png"
COIN_IMAGE_3 = ":resources:images/items/gold_3.png"
COIN_IMAGE_4 = ":resources:images/items/gold_4.png"
COIN = Sprite(COIN_IMAGE,
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
CURSOR = Sprite("images/pointer.png", 0.5)
STAR2_IMAGE = "images/star.png"
SCALING_STAR = 1.3
TILE_SIZE = 50
BUTTON_SOUND = Sound("sound/button_press.wav")
SETTINGS_SOUND = Sound(":resources:sounds/rockHit2.wav")
BUTTON_SOUND_2 = Sound("sound/button_press_2.wav")
START_LOAD_SOUND = Sound("sound/start.mp3")
PLAY_SOUND = Sound("sound/play.wav")
EXIT_SOUND = Sound(":resources:sounds/lose5.wav")
GAMEOVER_SOUND = Sound(":resources:sounds/gameover1.wav")
BACKGROUND_SOUND = Sound(":resources:music/funkyrobot.mp3")
MUSIC_VOLUME = 0.5
HEART_IMAGE = "images/heart.png"
EXIT_IMAGE = ":resources:images/tiles/signExit.png"
ENEMY_IMAGE = ":resources:images/animated_characters/zombie/zombie"
COINS_SOUND = Sound(":resources:sounds/coin1.wav")
HIT_SOUND = Sound("sound/hit.wav")
DIED_SOUND = Sound("sound/died.mp3")
WIN_SOUND = Sound("sound/game-win-sound-effect.mp3")
INSTRUCTION_IMAGE = "images/instruction.png"
INSTRUCTION_IMAGE_2 = "images/instruction2.png"
RUSSIA_IMAGE = "images/russia.png"
RUSSIA_IMAGE_2 = "images/russia2.png"
ENGLISH_IMAGE = "images/english.png"
ENGLISH_IMAGE_2 = "images/english2.png"
SHOP_IMAGE = "images/shop.png"
SHOP_IMAGE_2 = "images/shop2.png"
PERSON_SOUND = Sound(":resources:sounds/upgrade1.wav")
SCALING_LOGO = 2.1
LOGO = Sprite("images/logo.png", SCALING_LOGO,
              center_x=SCREEN_WIDTH // 2, center_y=SCREEN_HEIGHT // 2)
