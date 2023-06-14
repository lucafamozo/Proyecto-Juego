import pygame
import random
import colores

class Enemigos(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__
        self.image = pygame.image.load("img\\auto_enemigo.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(415,725)
        self.rect.y = random.randrange(800)

'''def crear_enemigos(ancho,alto):
        dict_personaje = {}
        dict_personaje["surface"] = pygame.image.load("img\\auto_enemigo.png")
        dict_personaje["surface"] = pygame.transform.scale(dict_personaje["surface"],(70,70))
        dict_personaje["rect_pos"].x = random.randrange(415,725,70)
        dict_personaje["rect_pos"].y = random.randrange(0,800,70)
        dict_personaje["rect"].x = random.randrange(415,725,70)
        dict_personaje["rect"].y = random.randrange(0,800,70)
        return dict_personaje'''

'''def crear_enemigos(ancho, alto):
    dict_personaje = {}
    dict_personaje["surface"] = pygame.image.load("img\\auto_enemigo.png")
    dict_personaje["surface"] = pygame.transform.scale(dict_personaje["surface"], (70, 70))
    dict_personaje["rect_pos"] = pygame.Rect(0, 0, 150, 150)  # Crear un objeto Rect para rect_pos
    dict_personaje["rect"] = pygame.Rect(0, 0, 150, 150)  # Crear un objeto Rect para rect

    dict_personaje["rect_pos"].x = random.randrange(415, 725, 100)
    dict_personaje["rect_pos"].y = random.randrange(0, 800, 100)
    dict_personaje["rect"].x = random.randrange(415, 725, 100)
    dict_personaje["rect"].y = random.randrange(0, 800, 100)

    return dict_personaje'''


def crear_enemigos(ancho, alto):
    dict_personaje = {}
    dict_personaje["surface"] = pygame.image.load("img\\auto_enemigo.png")
    dict_personaje["surface"] = pygame.transform.scale(dict_personaje["surface"], (200, 200))  # Redimensionar la superficie
    dict_personaje["rect_pos"] = pygame.Rect(0, 0, 200, 200)  # Crear un objeto Rect con las nuevas dimensiones
    dict_personaje["rect"] = pygame.Rect(0, 0, 200, 200)  # Crear un objeto Rect con las nuevas dimensiones

    dict_personaje["rect_pos"].x = random.randrange(415, 725, 70)
    dict_personaje["rect_pos"].y = random.randrange(0, 800, 70)
    dict_personaje["rect"].x = random.randrange(415, 725, 70)
    dict_personaje["rect"].y = random.randrange(0, 800, 70)

    return dict_personaje