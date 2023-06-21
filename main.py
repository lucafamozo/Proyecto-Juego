import pygame
import personaje
import auto_rojos
import charcos_fuel
from base_datos import crear_tabla_personajes, guardar_personaje, mostrar_personajes
import botones
import musica
import operator

pygame.init()

# Crear la tabla "personajes" si no existe
crear_tabla_personajes()

# Configuración de la pantalla
ANCHO_SCREEN = 1200
ALTO_SCREEN = 800
screen = pygame.display.set_mode((ANCHO_SCREEN, ALTO_SCREEN))

# Configuración de eventos temporizados
timer_segundo = pygame.USEREVENT + 0
pygame.time.set_timer(timer_segundo, 100)

timer_cinco_segundos = pygame.USEREVENT + 1
pygame.time.set_timer(timer_cinco_segundos, 500)

score = 0
JUGANDO = 0
FPS = 30
nombre_jugador = ""
score_duracion = 0

# Creación del jugador
jugador = personaje.Player(screen.get_width(), 70, 110)

# Creación de autos enemigos y charcos de combustible
lista_autos_enemigos = auto_rojos.crear_lista_autos_enemigos(4)
lista_charcos = charcos_fuel.crear_lista_charcos(4)

# Inicialización del juego
flag_correr = True
clock = pygame.time.Clock()

# MÚSICA
#musica.reproducir_musica_fondo()

# CREADOR DE BOTONES
boton_jugar = botones.Button(screen, "img/boton_jugar.png", (500, 300, 200, 60))
boton_score = botones.Button(screen, "img/score.png", (500, 480, 200, 60))
boton_game_over = botones.Button(screen, "img/game_over.png", (500, 300, 300, 200))
boton_regresar = botones.Button(screen, "img/menu.png", (500, 300, 200, 60))

# CREADOR DE CUADRO DE INGRESO DEL NOMBRE
cuadro_texto = botones.CuadroTexto(screen, (500, 200, 200, 40))

def dibujar_fondo():
    # Imagen de fondo
    screen.fill((0, 0, 0))
    background = pygame.image.load("img/background-1_0.png")
    background = pygame.transform.scale(background, (ANCHO_SCREEN, ALTO_SCREEN))
    screen.blit(background, (0, 0))

def obtener_eventos():
    return pygame.event.get()

def mapear_coordenadas(evento):
    global JUGANDO, FPS, score  # Declarar las variables globales
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if JUGANDO == 0:
            if boton_jugar.rect.collidepoint(evento.pos):
                JUGANDO = 1
            elif boton_score.rect.collidepoint(evento.pos):
                JUGANDO = 3
        elif JUGANDO == 2:
            if boton_game_over.rect.collidepoint(evento.pos):
                JUGANDO = 0
        elif JUGANDO == 3:
            if boton_regresar.rect.collidepoint(evento.pos):
                JUGANDO = 0

    if evento.type == pygame.KEYDOWN:
        if JUGANDO == 0:
            if evento.key == pygame.K_BACKSPACE:
                cuadro_texto.eliminar_caracter()
            elif evento.key == pygame.K_RETURN:
                # Acción al presionar Enter (por ejemplo, iniciar el juego)
                # Puedes obtener el nombre ingresado utilizando cuadro_texto.texto
                JUGANDO = 1
            else:
                cuadro_texto.agregar_caracter(evento.unicode)

    if evento.type == pygame.USEREVENT:
        if evento.type == timer_segundo:
            FPS += 1
            auto_rojos.update(lista_autos_enemigos)
            charcos_fuel.update(lista_charcos)
            score += 1

def jugar():
    global JUGANDO, score, nombre_jugador, score_duracion
    # Mover personaje
    jugador.mover(pygame.key.get_pressed())
    jugador.mover_aleatorio()
    if jugador.salud <= 0:
        nombre_jugador = cuadro_texto.texto
        score_duracion = score
        # Guardar el nombre y score en la base de datos
        guardar_personaje(nombre_jugador, score_duracion)
        JUGANDO = 2
        # Reiniciar variables al regresar al estado inicial
        jugador.salud = 150  # Reiniciar la salud del jugador a su valor inicial
        score = 0  # Reiniciar el score a 0

    # Mostrar elementos en la pantalla
    jugador.actualizar_pantalla(screen)
    charcos_fuel.actualizar_movimiento_aleatorio(jugador)
    charcos_fuel.efecto_charco(lista_charcos, jugador, screen)
    auto_rojos.actualizar_pantalla(lista_autos_enemigos, jugador, screen, score)

def mostrar_interfaz_juego():
    cuadro_texto.mostrar()
    boton_jugar.mostrar()
    boton_score.mostrar()

def mostrar_game_over():
    boton_game_over.mostrar()

def mostrar_score():
    mostrar_personajes(screen)
    boton_regresar.mostrar()

while flag_correr:
    dibujar_fondo()

    # Obtener eventos
    lista_eventos = obtener_eventos()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False

        mapear_coordenadas(evento)

    # Juego en curso
    if JUGANDO == 1:
        jugar()

    # Mostrar botones en la pantalla si no se está jugando
    if JUGANDO == 0:
        mostrar_interfaz_juego()
    elif JUGANDO == 2:
        mostrar_game_over()
    elif JUGANDO == 3:
        mostrar_score()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()