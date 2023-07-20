import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import BOSS


class Boss(Enemy):
    WIDTH = 80
    HEIGHT = 120
    SPEED_Y = 0
    SPEED_X = 4
    LIVE = 50
    POINTS = 50
    SHOOTING_TIME = 50
    def __init__(self):
        self.image = BOSS
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
    def update(self, bullet_handler):
        self.rect.y += self.SPEED_Y
        super().update(bullet_handler)
    