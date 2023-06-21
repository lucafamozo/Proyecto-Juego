import pygame
import random

class Enemigos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img\\auto_enemigo.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(415, 725)
        self.rect.y = random.randrange(800)

def crear_enemigos(x, y, ancho, alto):
    auto_enemigo = Enemigos()
    auto_enemigo.image = pygame.transform.scale(auto_enemigo.image, (ancho, alto))
    auto_enemigo.rect.x = x
    auto_enemigo.rect.y = y
    auto_enemigo.speed = random.randrange(20, 50, 10)
    auto_enemigo.posicion_inicial = (x, y)
    return auto_enemigo

def crear_lista_autos_enemigos(cantidad):
    lista_autos_enemigos = []
    for i in range(cantidad):
        y = random.randrange(-1000, 0, 50)
        lista_autos_enemigos.append(crear_enemigos((260 + i * 190), y, 120, 210))
    return lista_autos_enemigos

def update(lista_autos):
    for auto in lista_autos:
        auto.rect.y += auto.speed
        if auto.rect.y > 800:
            auto.rect.x, auto.rect.y = auto.posicion_inicial

def actualizar_pantalla(lista_autos, personaje, pantalla, tiempo):
    for auto in lista_autos:
        if personaje.rect.colliderect(auto.rect):
            personaje.salud -= 1
            if personaje.salud < 0:
                personaje.salud = 0
        pantalla.blit(auto.image, auto.rect)

    font = pygame.font.SysFont("Arial Narrow", 50)
    salud_texto = font.render("SALUD: {0}".format(personaje.salud), True, (255, 0, 0))
    tiempo_texto = font.render("SCORE: {0}".format(tiempo), True, (255, 0, 0))
    pantalla.blit(salud_texto, (0, 0))
    pantalla.blit(tiempo_texto, (0, 50))