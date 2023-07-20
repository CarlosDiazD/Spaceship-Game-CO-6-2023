import pygame
from game.utils.constants  import SPACESHIP,SCREEN_WIDTH,SCREEN_HEIGHT,BULLET_PLAYER_TYPE,SPACESHIP_SHIELD
from game.components.power_ups.shield import Shield
from game.components.power_ups.cadence import Cadence

class Spaceship:
    WIDTH = 40
    HEIGHT = 60
    X_POS= (SCREEN_WIDTH//2)-WIDTH
    Y_POS= 500
    SHOOTING_TIME = 20
    def __init__(self) :
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.WIDTH,self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x= self.X_POS
        self.rect.y= self.Y_POS
        self.is_alive = True
        self.has_shield = False
        self.shooting_time=0
        self.time_up=0
        self.live = 3
    
    def update(self,game_speed,user_input,bullet_handler):
        if user_input[pygame.K_SPACE]: 
         self.shooting_time +=1
         if self.shooting_time % self.SHOOTING_TIME == 0:
          self.shoot(bullet_handler)
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
        if self.has_shield:
            time_to_show = round((self.time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show < 0:
                self.deactive_power_up()

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
    def shoot(self,bullet_handler):
        bullet_handler.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)
    
    def activate_power_up(self, power_up):
        self.time_up = power_up.time_up
        if type(power_up) == Shield:
            self.image = SPACESHIP_SHIELD
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT+5))
            self.has_shield = True
        elif type(power_up) == Cadence:
            self.SHOOTING_TIME = 10
    
    def deactive_power_up(self):
        self.has_shield = False
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.SHOOTING_TIME = 30
    
    def hit(self,damage):
        self.live -= damage
        if self.live == 0:
         self.is_alive = False
    
    def reset(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.has_shield = False   
        self.live = 3 
        
       
            