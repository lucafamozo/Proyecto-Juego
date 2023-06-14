import pygame
import sqlite3
import personaje
import enemigos
import colores

pygame.init()

ANCHO_SCREEN = 1200
ALTO_SCREEN = 800
POSICION_RUTA = [410,0,390,ALTO_SCREEN]# x, y, ancho y alto
POSICION_LINEA_RUTA = [595, 0, 10, ALTO_SCREEN]

FPS = 30

# CREACIÓN PERSONAJES
player = personaje.Player.crear_personaje()
autos_enemigos = enemigos.crear_enemigos(ANCHO_SCREEN,ALTO_SCREEN)
'''autos_enemigos = enemigos.Enemigos()
autos_enemigos.add'''

# COLORES: TIERRA/ARENA = (189, 183, 107) ///////  VERDE =  (34, 139, 34)   crear personaje220,310,220,310

#SETEO DE LA PANTALLA
screen = pygame.display.set_mode((ANCHO_SCREEN,ALTO_SCREEN))

# FONDO
background = pygame.image.load("img\\background-1_0.png")
background = pygame.transform.scale(background,(1200,800))
screen.blit(background,(0,0))

flag_correr = True
while flag_correr:
    lista_evento = pygame.event.get()
    for evento in lista_evento:
        if evento.type == pygame.QUIT:
            flag_correr = False

        #MAPEO DE COORDENADAS
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                personaje.update(player, -20)
                #mover_izquierda = True
                #mover_derecha = False
            if evento.key == pygame.K_d:
                personaje.update(player, 20)
        
    #COLOR DE FONDO (VERDE BOSQUE)
    #screen.fill(colores.FORESTGREEN)

    #DIBUJOS ESTRUCTURAS
    #pygame.draw.rect(screen, colores.DARKGRAY, POSICION_RUTA)
    #pygame.draw.rect(screen, colores.WHITESMOKE, POSICION_LINEA_RUTA)'''
    
    #DIBUJO DEL PERSONAJE DEL JUGADOR
    #pygame.draw.rect(screen, colores.RED2, player["rect_pos"])
    screen.blit(player["surface"], player["rect_pos"])
    screen.blit(autos_enemigos["surface"], autos_enemigos["rect_pos"])

    pygame.display.flip()