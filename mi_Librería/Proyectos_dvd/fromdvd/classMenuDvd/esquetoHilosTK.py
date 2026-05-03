import threading
import time
import tkinter as tk

class XindiceX:
    def __init__(self, thread=None):
        self.thread = thread
        self.func = None
        self.running = False
        self.form = None  # Controlador del formulario, si aplica

    def add(self, func):
        """Asigna una función al hilo."""
        self.func = func

    def start(self, delay=0.3, is_form=False, config_others=True):
        """Inicia el hilo con la configuración especificada."""
        if self.func is None:
            raise ValueError("No se ha asignado una función al hilo.")

        if self.thread and self.thread.is_alive():
            print("El hilo ya está activo.")
            return

        self.thread = threading.Thread(
            target=self._run_task, args=(delay, is_form, config_others)
        )
        self.running = True
        self.thread.start()

    def _run_task(self, delay, is_form, config_others):
        """Lógica para ejecutar la tarea."""
        if is_form:
            if config_others:
                print("Configurando otros formularios...")
            print("Iniciando formulario...")
            self.form = self.func()  # Asigna el formulario devuelto por la función
            self.form.mainloop()  # Ejecuta el bucle del formulario
        else:
            while self.running:
                self.func()
                time.sleep(delay)

    def stop(self):
        """Detiene el hilo o cierra el formulario si es un formulario."""
        self.running = False
        if self.form:  # Si es un formulario, destrúyelo
            print("Cerrando formulario...")
            self.form.destroy()
            self.form = None
        if self.thread and self.thread.is_alive():
            self.thread.join()

    def is_running(self):
        """Verifica si el hilo está activo."""
        return self.thread.is_alive() if self.thread else False

# Funciones de ejemplo
def tarea_inmediata():
    print(f"Tarea ejecutándose en {threading.current_thread().name}...")

def formulario():
    print("Creando formulario...")
    root = tk.Tk()
    root.title("Formulario")
    tk.Label(root, text="Formulario Tkinter").pack()
    tk.Button(root, text="Cerrar", command=root.destroy).pack()
    return root

# Menú de ejemplo
if __name__ == "__main__":
    xindice = XindiceX()

    while True:
        print("\nMenú:")
        print("1. Ejecutar tarea inmediata")
        print("2. Iniciar formulario")
        print("3. Detener formulario o tarea")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            xindice.add(tarea_inmediata)
            xindice.start()
        elif opcion == "2":
            xindice.add(formulario)
            xindice.start(is_form=True)
        elif opcion == "3":
            xindice.stop()
        elif opcion == "4":
            xindice.stop()
            break
        else:
            print("Opción inválida.")
