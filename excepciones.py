try:
    int("Hola, mundo!")
except ValueError:
    print("Error. NO puede convertirse a un entero.")
finally:
    print("Aplicación finalizó su ejecución.")