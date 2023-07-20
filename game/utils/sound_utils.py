import pygame 
def load_mixer(track):
    pygame.mixer.music.load(track)

def play_tracks():
    pygame.mixer.music.play(-1)

def change_track(track):
    pygame.mixer.music.fadeout(3)
    pygame.mixer.music.load(track)
    