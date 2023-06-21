import pygame

def reproducir_musica_fondo():
    pygame.mixer.music.load("music/NotIntoU.mp3")
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.5)