import tkinter as tk
import tkinter as tk
from tkinter import ttk

class CustomFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        """
        Constructor de la clase personalizada.

        :param master: El contenedor padre.
        :param kwargs: Opciones adicionales para el widget.
        """
        # Configuraciones predeterminadas
        options = {
            "padx": kwargs.pop("padx", 3),
            "pady": kwargs.pop("pady", 3),
        }
        super().__init__(master, **options)  # Inicializa el widget base con opciones.
    
    def __enter__(self):
        """Activa el widget en el contexto del administrador `with`."""
        self.pack(expand=True, fill=tk.BOTH)  # Expande y llena el espacio disponible.
        return self  # Devuelve el objeto para usarlo dentro del bloque `with`.

    def __exit__(self, exc_type, exc_value, traceback):
        """Maneja la salida del bloque `with`."""
        # No necesitamos hacer nada aquí, pero puedes agregar lógica si es necesario.
        pass



class CustomWidget(tk.Widget):
    def __init__(self, master, widget_type, **kwargs):
        """
        Constructor para un widget genérico basado en tk.Widget.
        
        :param master: El widget padre (contenedor).
        :param widget_type: El tipo de widget que se va a crear (por ejemplo, 'label', 'button').
        :param kwargs: Opciones adicionales para el widget.
        """
        # Configuración predeterminada de padding
        kwargs.setdefault("padx", 3)
        kwargs.setdefault("pady", 3)
        self._type = widget_type
        
        # Llama al constructor base
        super().__init__(master, widget_type, kwargs)
    
    def __enter__(self):
        """
        Al entrar en el contexto 'with', empaqueta el widget automáticamente.
        """
        self.pack(expand=True, fill=tk.BOTH)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Maneja la salida del contexto 'with' (si es necesario).
        """
        pass




# ==================================================================
# ==================================================================
# Ejemplo de uso Frame

root = tk.Tk()
root.title("Ejemplo de CustomFrame con Contexto")

with CustomFrame(root, padx=10, pady=10) as frame:
    """ OBJETIVO A CUMPLIR CON LOS WIDGETS EN ENFILEITOR.
        >>> widget_01=.add_widget(nombre, posicionEstructura)    
        widget.configure(fg="blue", bg="lightgray")
    """    

with CustomWidget(frame, "label", text="Loren Ipsun!") as widget:
    widget.configure(fg="blue", bg="lightblue")


root.mainloop()





