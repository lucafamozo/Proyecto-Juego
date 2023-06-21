import pygame
import random

class Player:
    def __init__(self, pantalla, ancho, alto):
        self.salud = 150
        self.surface = pygame.image.load("img/player.png")
        self.surface = pygame.transform.scale(self.surface, (ancho, alto))
        self.rect = self.surface.get_rect()
        self.rect.y = 615
        self.rect.centerx = pantalla / 2
        self.movimiento_aleatorio = False
        self.tiempo_movimiento_aleatorio = 0

    def mover(self, lista_teclas):
        if lista_teclas[pygame.K_a]:
            self.update(-10)
        if lista_teclas[pygame.K_d]:
            self.update(10)

    def mover_aleatorio(self):
        if self.movimiento_aleatorio:
            self.rect.y = random.randrange(600, 655, 15)
            self.rect.x = self.rect.x + random.randrange(-10, 10, 5)

    def update(self, incremento):
        nueva_x = self.rect.x + incremento
        if (nueva_x > 195 and nueva_x < 940):
            self.rect.x += incremento

    def actualizar_pantalla(self, screen):
        screen.blit(self.surface, self.rect)