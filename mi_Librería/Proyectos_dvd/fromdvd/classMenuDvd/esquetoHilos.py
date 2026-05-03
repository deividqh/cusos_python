

# Funciones de ejemplo
def tarea_inmediata():
    print(f"Tarea ejecutándose en {threading.current_thread().name}...")

def formulario():
    print("Ejecutando formulario tkinter (simulado).")

# Ejemplo de uso
if __name__ == "__main__":
    # Instancia de la clase
    xindice = X_Men()

    # Agregar y ejecutar una tarea inmediata
    xindice.add(tarea_inmediata)
    xindice.start()  # Delay predeterminado de 0.3s

    # Pausa para observar la ejecución
    time.sleep(2)
    xindice.stop()

    # Configurar y ejecutar un formulario
    xindice.add(formulario)
    xindice.start(is_form=True, config_others=True)
