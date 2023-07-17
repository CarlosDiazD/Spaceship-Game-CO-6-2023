import pygame
from game.utils.constants  import SPACESHIP,SCREEN_WIDTH,SCREEN_HEIGHT

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
    
    def update(self,game_speed,user_input):
        if user_input[pygame.K_UP] and user_input[pygame.K_LEFT] :
         self.mov_up_left(game_speed)
        elif user_input[pygame.K_UP] and user_input[pygame.K_RIGHT] :
         self.mov_up_rigth(game_speed)
        elif user_input[pygame.K_DOWN] and user_input[pygame.K_LEFT] :
         self.mov_down_left(game_speed)
        elif user_input[pygame.K_DOWN] and user_input[pygame.K_RIGHT] :
         self.mov_down_rigth(game_speed)
        elif user_input[pygame.K_LEFT]:
         self.mov_lef(game_speed)
        elif user_input[pygame.K_RIGHT]:
         self.mov_rigth(game_speed)
        elif user_input[pygame.K_UP]:
         self.mov_up(game_speed)
        elif user_input[pygame.K_DOWN]:
         self.mov_down(game_speed)
        
    
    def draw(self,screen):
        screen.blit(self.image,self.rect )
    
    def mov_lef(self,game_speed):
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH - self.WIDTH
        self.rect.x -= game_speed
    
    def mov_rigth(self,game_speed):
        if self.rect.right > SCREEN_WIDTH:
            self.rect.x = 1
        self.rect.x += game_speed
   
    def mov_up(self,game_speed):
        if self.rect.top > SCREEN_HEIGHT // 2:
            self.rect.y -= game_speed
   
    def mov_down(self,game_speed):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += game_speed
    
    def mov_up_left(self,game_speed):
        self.mov_up(game_speed/1.5)
        self.mov_lef(game_speed/1.5)
       
    def mov_up_rigth(self,game_speed):
        self.mov_up(game_speed/1.5)
        self.mov_rigth(game_speed/1.5)
      
    def mov_down_left(self,game_speed):
        self.mov_down(game_speed/1.5)
        self.mov_lef(game_speed/1.5)
        
    def mov_down_rigth(self,game_speed):
        self.mov_down(game_speed/1.5)
        self.mov_rigth(game_speed/1.5)
       
            