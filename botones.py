import pygame

class Button:
    def __init__(self, master_surface, imagen, rect):
        self.master_surface = master_surface
        self.slave_surface = pygame.surface.Surface((10, 10))
        self.imagen =imagen
        self.rect = pygame.Rect(rect)

    def mostrar(self):
        boton_imagen = pygame.image.load(self.imagen)
        boton_imagen = pygame.transform.scale(boton_imagen, (self.rect[2], self.rect[3]))
        self.master_surface.blit(boton_imagen, (self.rect[0], self.rect[1])) 

class CuadroTexto:
    def __init__(self, master_surface, rect):
        self.master_surface = master_surface
        self.rect = pygame.Rect(rect)
        self.texto = ""
        self.font = pygame.font.Font(None, 32)

    def agregar_caracter(self, caracter):
        self.texto += caracter

    def eliminar_caracter(self):
        self.texto = self.texto[:-1]

    def mostrar(self):
        pygame.draw.rect(self.master_surface, (255, 255, 255), self.rect, 2)
        texto_superficie = self.font.render(self.texto, True, (255, 255, 255))
        self.master_surface.blit(texto_superficie, (self.rect.x + 5, self.rect.y + 5))