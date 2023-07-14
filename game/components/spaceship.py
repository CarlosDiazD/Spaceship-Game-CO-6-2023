import pygame
from game.utils.constants  import SPACESHIP,SCREEN_WIDTH

class Spaceship:
    WIDTH = 40
    HEIGTH = 60
    X_POS= (SCREEN_WIDTH//2)-WIDTH
    Y_POS= 500
    def __init__(self) :
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.WIDTH,self.HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x= self.X_POS
        self.rect.y= self.Y_POS
    
    def update(self):
        pass
    
    def draw(self,screen):
        screen.blit(self.image,self.rect )
    
    def mov_lef():
        pass