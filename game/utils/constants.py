import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SFX_DIR = os.path.join(os.path.dirname(__file__), "..", "assets",'Sounds')

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
CADENCE = pygame.image.load(os.path.join(IMG_DIR, 'Other/hevy.jpg'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG_1 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG_2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG_3 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG_4 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

SOUND_TRACK_1 = os.path.join(SFX_DIR,'Tracks/sound track.mp3')
SOUND_TRACK_2 = os.path.join(SFX_DIR,'Tracks/sound track 2.mp3')

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
CADENCE_TYPE = 'cadence'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
STINGRAY = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
BOSS = pygame.image.load(os.path.join(IMG_DIR, "Enemy/boss.png"))

FONT_STYLE = 'freesansbold.ttf'
LEFT = "left"
RIGHT = "right"
BULLET_ENEMY_TYPE='enemy'
BULLET_PLAYER_TYPE='player'
WHITE = (255, 255, 255)