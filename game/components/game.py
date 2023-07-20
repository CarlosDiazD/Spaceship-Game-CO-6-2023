import pygame
import random
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE,WHITE,SOUND_TRACK_1,BG_2,BG_3,BG_4
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.power_ups.power_up_handler import PowerUpHandler
from game.utils import text_utils
from game.utils import sound_utils

class Game:
    BEST_SCORE = 0
    BACKGROUND = [BG,BG_2,BG_3,BG_4]
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler= BulletHandler()
        self.power_up_handler= PowerUpHandler()
        self.score = 0
        self.enemys_destroyed=0
        self.number_deaths = 0
        self.new_best_score =False
        self.track = SOUND_TRACK_1
        self.background = BG

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        sound_utils.load_mixer(self.track)
        sound_utils.play_tracks()
        while self.running:
            self.events()
            self.update()
            self.draw()
            
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                self.running = False
           elif event.type == pygame.KEYUP and not self.playing:
                self.reset()
                self.playing = True                

    def update(self):
       
        if self.playing:
            user_input= pygame.key.get_pressed()
            self.player.update(self.game_speed,user_input,self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler)
            self.bullet_handler.update(self.player,self.enemy_handler.enemies)
            self.power_up_handler.update(self.player)
            self.score = self.enemy_handler.match_score
            self.enemys_destroyed = self.enemy_handler.enemies_destroyed
            if not self.player.is_alive:
                pygame.time.delay(300)
                self.playing = False
                self.number_deaths += 1
                if self.score > self.BEST_SCORE:
                    self.BEST_SCORE = self.score
                    self.new_best_score = True
            if self.enemy_handler.match % 2:
                self.background = random.choice(self.BACKGROUND)
        

    def draw(self):
        self.draw_background(self.background)
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.power_up_handler.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()


    def draw_background(self,background):
        image = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
    
        

    def draw_menu(self):
        
        if self.number_deaths == 0:
            text, text_rect = text_utils.get_message('Press any Key to Start', 30, WHITE)
            self.screen.blit(text, text_rect)
        else:
           # sound_utils.change_track(SOUND_TRACK_1)
            text, text_rect = text_utils.get_message('Press any Key to Restart', 30, WHITE)
            if self.new_best_score:
                score, score_rect = text_utils.get_message(f'congratulations your new best score is: {self.BEST_SCORE}', 30, WHITE, height=SCREEN_HEIGHT//2 + 50)
            else:
                score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 30, WHITE, height=SCREEN_HEIGHT//2 + 50)
            deats , deaths_rect =  text_utils.get_message(f'Number of attemps: {self.number_deaths}', 25, WHITE, height=SCREEN_HEIGHT//2 + 100)     
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(deats, deaths_rect)
            self.background = random.choice(self.BACKGROUND)
        

            
    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 20, WHITE, 1000, 40)
        destroyed ,destroyed_rect = text_utils.get_message(f'Enemies destroyed: {self.enemys_destroyed}', 15, WHITE, 1000, 60)
        best_score, best_score_rect = text_utils.get_message(f'Best score: {self.BEST_SCORE}', 15, WHITE, 1000, 80)
        self.screen.blit(score, score_rect)
        self.screen.blit(destroyed ,destroyed_rect)
        self.screen.blit(best_score, best_score_rect)
        
    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.score = 0
        self.new_best_score = False
        self.background = random.choice(self.BACKGROUND)