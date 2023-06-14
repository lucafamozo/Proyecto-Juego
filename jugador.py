import pygame
import colores

# TAMAÑO PANTALLA
ANCHO_SCREEN = 1200
ALTO_SCREEN = 800
ANCHO_PLAYER = 200
ALTO_PLAYER = 200

# VARIABLES DE DIRECCION
mover_izquierda = False
mover_derecha = False
mover_arriba = False
mover_abajo = False

class Jugador(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__
        self.image = pygame.surface((200,200))
        self.image.fill(colores.AQUA)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO_SCREEN//2,ALTO_SCREEN//2)

    def movimiento_jugador():
         if mover_izquierda == True:
             print("q")

    def saber_si_mover(evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                #personaje.update(player, -10)
                mover_izquierda = True
                mover_derecha = False
            if evento.key == pygame.K_d:
                #personaje.update(player, 10)
                mover_derecha = True
                mover_izquierda = False
            if evento.key == pygame.K_w:
                mover_arriba = True
                mover_abajo = False
        '''if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a or evento.key == pygame.K_d:
                vx = 0'''
        
    def update(self):
        self.rect.y += 10
        if self.rect.top > ALTO_SCREEN:
            self.rect.bottom = 0