import pygame
import colores

class Player:
    def __init__(self) -> None:
        ''', surface, rect_pos, rect
        self.surface = surface
        self.rect_pos = rect_pos
        self.rect = rect'''
        
        pass

    def crear_personaje():
        dict_personaje = {}
        dict_personaje["surface"] = pygame.image.load("img/player.png")
        dict_personaje["surface"] = pygame.transform.scale(dict_personaje["surface"],(70,70))
        dict_personaje["rect_pos"] = pygame.Rect(565,615,70,70)
        dict_personaje["rect"] = pygame.Rect(565,615,70,70)
        return dict_personaje

def update(personaje, incremento_x):
    coordenadas = personaje["rect_pos"].x #= personaje["rect_pos"].x + incremento_x
    if (coordenadas > 195 and coordenadas < 725):
        personaje["rect_pos"].x = personaje["rect_pos"].x + incremento_x
        personaje["rect"].x = personaje["rect"].x + incremento_x
    if coordenadas > 195:
        coordenadas = 185
    if coordenadas < 725:
        coordenadas = 725
    
    print(coordenadas)

def actualizar_pantalla(personaje, screen):
    pygame.draw.rect(screen, colores.RED1, personaje["rect"])
    screen.blit(personaje["surface"], personaje["rect"]) 






    #415
    #725