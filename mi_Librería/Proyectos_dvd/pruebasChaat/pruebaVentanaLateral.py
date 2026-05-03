import tkinter as tk

def mover_ventana():
    global start_x
    # Si la ventana aún no ha alcanzado la posición deseada, seguimos moviéndola
    if start_x > screen_width - window_width - 10:
        start_x -= 10  # Mover la ventana hacia la izquierda 10 píxeles en cada paso
        root.geometry(f'{window_width}x{window_height}+{start_x}+{start_y}')
        root.after(20, mover_ventana)  # Volver a llamar a esta función en 20 ms

def mostrar_completa(event=None):
    # Iniciar el movimiento gradual de la ventana
    mover_ventana()

# Inicializa la ventana de tkinter
root = tk.Tk()

# Tamaño de la ventana
window_width = 400
window_height = 300

# Obtiene el tamaño de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcula la posición inicial (fuera de la pantalla a la derecha)
start_x = screen_width  # Totalmente fuera de la pantalla
start_y = (screen_height // 2) - (window_height // 2)  # Centrando verticalmente

# Posición final (con un padx de 10 píxeles desde el borde derecho)
final_x = screen_width - window_width - 10

# Configura la geometría inicial de la ventana (fuera de la pantalla)
root.geometry(f'{window_width}x{window_height}+{start_x}+{start_y}')

# Detecta cuando la ventana gana el foco (como si se hiciera clic en la barra de título)
root.bind('<FocusIn>', mostrar_completa)

# Agrega un widget para mostrar dentro de la ventana (opcional)
label = tk.Label(root, text="La ventana se desliza al hacer clic en la barra de título")
label.pack(pady=100)

# Inicia el bucle principal
root.mainloop()
