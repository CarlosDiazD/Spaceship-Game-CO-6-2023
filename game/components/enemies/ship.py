import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1,LEFT,RIGHT,SCREEN_WIDTH


class Ship(Enemy):
    WIDTH = 40
    HEIGHT = 60

    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
    def update(self):
        self.rect.y += self.SPEED_Y
        if self.move_x == LEFT:
            self.rect.x -= self.SPEED_X

            if self.rect.x <= 0 or self.index > self.INTERVAL:
                self.move_x = RIGHT
                self.index = 0
        else:
            self.rect.x += self.SPEED_X

            if (
                self.rect.x >= SCREEN_WIDTH - self.image.get_width()
                or self.index > self.INTERVAL
            ):
                self.move_x = LEFT
                self.index = 0
        super().update()