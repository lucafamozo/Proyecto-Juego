import sqlite3
import pygame

def crear_tabla_personajes():
    with sqlite3.connect("datos.db") as conexion:
        try:
            sentencia = '''CREATE TABLE IF NOT EXISTS personajes
                           (
                               nombre text,
                               score interger
                           )
                        '''
            conexion.execute(sentencia)
            print("Se creó la tabla personajes")
        except sqlite3.OperationalError:
            print("La tabla personajes ya existe")

def guardar_personaje(nombre, score):
    with sqlite3.connect("datos.db") as conexion:
        try:
            conexion.execute("INSERT INTO personajes (nombre, score) VALUES (?, ?)", (nombre, score))
            conexion.commit()
            print("Nombre y score guardados en la base de datos")
        except:
            print("Error al guardar los datos en la base de datos")

def mostrar_personajes(screen):
    with sqlite3.connect("datos.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM personajes ORDER BY score DESC LIMIT 3")
        filas = cursor.fetchall()
        
        if filas:
            # Posiciones iniciales para mostrar los nombres y puntajes
            x = 500
            y = 100

            # Tamaño y espaciado de la fuente
            font = pygame.font.Font(None, 30)
            espaciado = 40

            for fila in filas:
                nombre = fila[0]
                puntaje = str(fila[1])

                # Renderizar el nombre y puntaje como superficies de texto
                nombre_surface = font.render(nombre, True, (255, 255, 255))
                puntaje_surface = font.render(puntaje, True, (255, 255, 255))

                # Mostrar las superficies de texto en la pantalla
                screen.blit(nombre_surface, (x, y))
                screen.blit(puntaje_surface, (x + 200, y))

                # Aumentar la posición vertical para el siguiente nombre y puntaje
                y += espaciado
        else:
            print("No hay registros en la tabla personajes")
