import tkinter as tk

# Variable de estado para rastrear si la ventana está expandida o contraída
expanded = False

def mover_ventana(mostrar_completa=True):
    global coorX, expanded
    if mostrar_completa:
        # Expande la ventana hacia el centro de la pantalla
        if coorX > screenWidth - formWidth - 10:
            coorX -= 10
            root.geometry(f'{formWidth}x{formHeight}+{coorX}+{coorY}')
            root.after(20, mover_ventana)
        else:
            expanded = True  # Indica que la ventana está completamente expandida
    else:
        # Contrae la ventana de nuevo hacia los 40 píxeles visibles
        if coorX < screenWidth - 40:
            coorX += 10
            root.geometry(f'{formWidth}x{formHeight}+{coorX}+{coorY}')
            root.after(20, mover_ventana, False)
        else:
            expanded = False  # Indica que la ventana está contraída
# ___________________
# Al hacer doble clic, expandir o contraer la ventana
def toggle_ventana(event):
    if expanded:
        mover_ventana(mostrar_completa=False)
    else:
        mover_ventana(mostrar_completa=True)


# Inicializa la ventana de tkinter
root = tk.Tk()

# Tamaño de la ventana
formWidth = 200
formHeight = 150

# Obtiene el tamaño de la pantalla Xa calcular la posicion (coorX, coorY) 
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# Calcula la posición inicial (40 píxeles visibles)
coorX = screenWidth - 40                             # 40 píxeles visibles al inicio
coorY = screenHeight - formHeight - 100              # 100 de la barra inferior. 

# Configura la geometría inicial de la ventana (40 píxeles visibles)
root.geometry(f'{formWidth}x{formHeight}+{coorX}+{coorY}')

# Detecta el doble clic en la ventana para expandir o contraer
root.bind('<Double-1>', toggle_ventana)

# Agrega un widget para mostrar dentro de la ventana (opcional)
# label = tk.Label(root, text="Haz doble clic para expandir/contraer la ventana")
# label.pack(pady=100)

# Inicia el bucle principal
root.mainloop()
