from game.components.enemies.ship import Ship
from game.components.enemies.stingray import Stingray
import random
class EnemyHandler:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()

            if not enemy.is_visible:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 6:
            list_enemies=[Ship(),Stingray()]
            
            self.enemies.append(random.choice(list_enemies))

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)