import pygame
import random

class Charco:
    def __init__(self, x, y, ancho, alto):
        self.surface = pygame.image.load("img\\charco_fuel.png")
        self.surface = pygame.transform.scale(self.surface, (ancho, alto))
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randrange(30, 40, 10)
        self.posicion_inicial = (x, y)

def crear_lista_charcos(cantidad):
    lista_charcos = []
    for i in range(cantidad):
        y = random.randrange(-1000, 0, 100)
        lista_charcos.append(Charco((260 + i * 190), y, 50, 50))
    return lista_charcos

def update(lista_charcos):
    for charco in lista_charcos:
        charco.rect.y += charco.speed
        if charco.rect.y > 800:
            charco.rect.x, charco.rect.y = charco.posicion_inicial

def efecto_charco(lista_charcos, personaje, pantalla):
    for charco in lista_charcos:
        if personaje.rect.colliderect(charco.rect):
            personaje.movimiento_aleatorio = True
            personaje.tiempo_movimiento_aleatorio = 4 * 30  # 4 segundos x 30 FPS
        pantalla.blit(charco.surface, charco.rect)

def actualizar_movimiento_aleatorio(personaje):
    if personaje.movimiento_aleatorio:
        personaje.tiempo_movimiento_aleatorio -= 1
        if personaje.tiempo_movimiento_aleatorio <= 0:
            personaje.movimiento_aleatorio = False