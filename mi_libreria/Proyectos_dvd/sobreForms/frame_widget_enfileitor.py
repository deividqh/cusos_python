import tkinter as tk
from tkinter import ttk

""" 

# Ejemplo: Cambiar sticky Dinámicamente

# Supongamos que tienes un botón creado con el contexto CustomWidget:
with CustomWidget(parent_frame, "button", text="Click Me") as btn:
    btn.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)

# Si más adelante decides cambiar el comportamiento de su posición (por ejemplo, el sticky):
btn.grid_configure(sticky="e")  # Cambia a que se alinee a la derecha

# ¿Cómo Funciona?
# 1. Configuración Inicial:
# En el bloque with, defines una configuración inicial para el widget al llamarlo con grid() o pack().
# 2. Métodos Dinámicos de grid y pack:
# grid_configure: Permite modificar los parámetros iniciales de grid (como sticky, padx, pady) sin necesidad de volver a declarar la posición del widget.
# grid_remove: Te permite ocultar el widget sin destruirlo, manteniendo sus propiedades.
# pack_configure: Similar a grid_configure, pero para el gestor de geometría pack.
# 3. Flexibilidad Total:
# Como el widget mismo (btn, label, etc.) está separado del contexto y el layout, puedes ajustar dinámicamente cualquier aspecto después de haberlo creado.

 """


class CustomFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        """
        Clase personalizada para un Frame con padding predeterminado.
        """
        options = {"padx": kwargs.pop("padx", 10), "pady": kwargs.pop("pady", 10)}
        super().__init__(master, **options)
        self.grid_propagate(False)  # Permite control explícito de tamaño.
    
    def __enter__(self):
        """Empaqueta automáticamente el Frame en el contexto."""
        self.grid(sticky="nsew")  # Se expande en todas las direcciones.
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Maneja la salida del bloque `with`."""
        pass


class CustomWidget(tk.Widget):
    def __init__(self, master, widget_type, **kwargs):
        """
        Clase genérica para widgets basada en tk.Widget.
        """
        kwargs.setdefault("padx", 3)
        kwargs.setdefault("pady", 3)
        self._type = widget_type
        super().__init__(master, widget_type, kwargs)

    def __enter__(self):
        """Empaqueta automáticamente el widget en el contexto."""
        self.grid(sticky="nsew")  # Se expande completamente.
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Maneja la salida del bloque `with`."""
        pass


# Aplicación principal
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ejemplo con CustomFrame y CustomWidget")
    root.geometry("600x400")
    
    # Configuración del grid principal
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)
    root.rowconfigure(0, weight=1)
    
    # Frame izquierdo (Botones)
    with CustomFrame(root) as frame_left:
        frame_left.grid(row=0, column=0)
        for i, text in enumerate(["Add", "Supr", "Updt", "View"]):
            button = tk.Button(frame_left, text=text)
            button.grid(row=i, column=0, sticky="nsew", pady=3, padx=3)
            frame_left.rowconfigure(i, weight=1)  # Configurar filas dinámicas
        frame_left.columnconfigure(0, weight=1)

    # Frame derecho (Label-Entry)
    with CustomFrame(root) as frame_right:
        frame_right.grid(row=0, column=1)
        for i, text in enumerate(["Label 1", "Label 2", "Label 3", "Label 4"]):
            label = tk.Label(frame_right, text=text)
            entry = tk.Entry(frame_right)
            label.grid(row=i, column=0, sticky="w", padx=3, pady=3)
            entry.grid(row=i, column=1, sticky="ew", padx=3, pady=3)
            frame_right.rowconfigure(i, weight=1)  # Configurar filas dinámicas
        frame_right.columnconfigure(0, weight=1)
        frame_right.columnconfigure(1, weight=2)  # Más espacio para entradas

    # Loop principal
    root.mainloop()
