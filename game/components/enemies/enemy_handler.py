from game.components.enemies.ship import Ship
from game.components.enemies.stingray import Stingray
from game.components.enemies.boss import Boss
import random
class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.enemies_destroyed = 0
        self.match_destroyed = 0
        self.match_score = 0
        self.enemies_alive = 6
        self.match=4

    def update(self,bullet_handler):
        
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_visible:
                enemy.rect.y = 0
                enemy.is_visible = True
            if not enemy.is_alive:
                self.remove_enemy(enemy)
            if not enemy.is_alive:
                self.enemies_destroyed += 1
                
                self.match_score += enemy.points
            if self.enemies_destroyed % 5 == 0  and self.enemies_destroyed != 0:
               self.match +=1
            
                  

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < self.enemies_alive:
            if Boss() in self.enemies:
                list_enemies=[Ship(),Stingray()]
                self.enemies.append(random.choice(list_enemies))
            else:
                 if self.enemies_destroyed % 5 == 0  and self.enemies_destroyed != 0:
                    self.enemies.append(Boss())
                 else: 
                    list_enemies=[Ship(),Stingray()]
                    self.enemies.append(random.choice(list_enemies))

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
    def reset(self):
        self.enemies = []
        self.enemies_destroyed = 0
        self.match_destroyed = 0
        self.match_score = 0
        self.enemies_alive = 6
        self.match=1