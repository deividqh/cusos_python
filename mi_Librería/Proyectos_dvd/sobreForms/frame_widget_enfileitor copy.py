import tkinter as tk

class CustomWidget:
    def __init__(self, master, widget_type, **kwargs):
        """
        Constructor para un widget genérico.
        
        :param master: El widget padre (contenedor).
        :param widget_type: El tipo de widget que se va a crear (por ejemplo, 'label', 'button').
        :param kwargs: Opciones adicionales para el widget.
        """
        self.master = master
        self.widget_type = widget_type
        self.kwargs = kwargs
        self.widget = None  # El widget real se crea en el bloque `with`
    
    def __enter__(self):
        """Crea y devuelve el widget."""
        widget_class = getattr(tk, self.widget_type.capitalize(), None)
        if widget_class is None:
            raise ValueError(f"Tipo de widget desconocido: {self.widget_type}")
        
        self.widget = widget_class(self.master, **self.kwargs)
        return self.widget

    def __exit__(self, exc_type, exc_value, traceback):
        """Maneja la salida del bloque 'with'."""
        pass


class CustomFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        """
        Constructor para un frame personalizado.
        
        :param master: El widget padre (contenedor).
        :param kwargs: Opciones adicionales para el frame.
        """
        kwargs.setdefault("padx", 10)
        kwargs.setdefault("pady", 10)
        super().__init__(master, **kwargs)
        
    def __enter__(self):
        """Devuelve el frame para su uso en el bloque `with`."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Maneja la salida del bloque 'with'."""
        pass


# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ejemplo de CustomWidget y CustomFrame")
    root.geometry("400x400")  # Tamaño inicial de la ventana

    # Configuración de la grilla principal
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Frame 1 con 4 botones en una fila
    with CustomFrame(root) as frame1:
        frame1.grid(row=0, column=0, sticky="nsew")  # Ubica el frame en la grilla
        for i, text in enumerate(["Add", "Supr", "Updt", "View"]):
            with CustomWidget(frame1, "button", text=text) as btn:
                btn.grid(row=0, column=i, sticky="nsew", padx=3, pady=3)
                frame1.grid_columnconfigure(i, weight=1)
        frame1.grid_rowconfigure(0, weight=1)

    # Frame 2 con 4 filas de Label - Entry
    with CustomFrame(root) as frame2:
        frame2.grid(row=1, column=0, sticky="nsew")  # Ubica el frame en la grilla
        labels = ["Name:", "Email:", "Phone:", "Address:"]
        for i, text in enumerate(labels):
            with CustomWidget(frame2, "label", text=text) as lbl:
                lbl.grid(row=i, column=0, sticky="nsew", padx=3, pady=3)
            with CustomWidget(frame2, "entry") as entry:
                entry.grid(row=i, column=1, sticky="nsew", padx=3, pady=3)
            frame2.grid_rowconfigure(i, weight=1)
        frame2.grid_columnconfigure(0, weight=1)
        frame2.grid_columnconfigure(1, weight=2)

    root.mainloop()



def create_dynamic_entries(frame, num_rows):
    for i in range(num_rows):
        label = tk.Label(frame, text=f"Label {i + 1}")
        entry = tk.Entry(frame)
        
        label.grid(row=i, column=0, padx=3, pady=10, sticky="nsew")
        entry.grid(row=i, column=1, padx=3, pady=10, sticky="nsew")

# Función para pedir el número de filas al usuario
def ask_for_rows():
    num_rows = int(input("¿Cuántas filas de label-entry deseas crear? "))
    return num_rows

# Obtener el número de filas y crear los widgets dinámicamente
num_rows = ask_for_rows()
create_dynamic_entries(parent_frame, num_rows)
