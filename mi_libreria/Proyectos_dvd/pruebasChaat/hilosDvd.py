import threading
import time
import os

# Función que será ejecutada por cada hilo
def imprimir_mensaje(mensaje, delay):
    for i in range(5):
        print(f"Hilo {threading.current_thread().name}: {mensaje}")
        time.sleep(delay)

# Función que será ejecutada por cada hilo
def imprimir_mensaje2(mensaje, delay):
    for i in range(5):
        print(f"Hilo {threading.current_thread().name}: {mensaje}")
        time.sleep(delay)


def ejecutar_hilos():
    # Crear hilos
    hilo1 = threading.Thread(target=imprimir_mensaje, args=("Hola desde el hilo 1", 1))
    hilo2 = threading.Thread(target=imprimir_mensaje2, args=("Hola desde el hilo 2", 2))

    # Iniciar hilos
    hilo1.start()
    hilo2.start()

    # Esperar a que los hilos terminen
    hilo1.join()
    hilo2.join()

    print("Todos los hilos han terminado.")

os.system('cls')
ejecutar_hilos()
