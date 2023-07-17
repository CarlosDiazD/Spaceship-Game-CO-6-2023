import pygame
import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import STINGRAY,LEFT,RIGHT,SCREEN_WIDTH,SCREEN_HEIGHT

class Stingray(Enemy):
    WIDTH = 40
    HEIGHT = 60

    def __init__(self):
        self.image = STINGRAY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
    
    def update(self):
       
        if self.rect.y >= 0:
            self.rect.y += self.SPEED_Y
        if self.index <= self.INTERVAL // 2:
            self.rect.y += self.SPEED_Y
        else :
            self.rect.y -= self.SPEED_Y
            
           
      
        
        super().update()