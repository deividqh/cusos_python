# Para las ventanas y formularios principales.
import tkinter as tk                

# ttk es un módulo dentro de Tkinter que proporciona un conjunto de widgets "temáticos" (estilizados) 
# que siguen los estándares del sistema operativo
from tkinter import ttk             

# Para enviar parametros al command y bind
from functools import partial       

# ******************* WIDGETS **********************
# 1. Label -> # Muestra texto o imágenes estáticas.
    # Ejemplo: label = tk.Label(root, text="Hola Mundo")

# 2. Button -> # Un botón que puede ejecutar una función cuando se hace clic en él.
    # Ejemplo: button = tk.Button(root, text="Click Me", command=my_function)

# 3. Entry -> # Caja de texto para entrada de una sola línea.
    # Ejemplo: entry = tk.Entry(root)
# 4. Text -> # Caja de texto para entrada de múltiples líneas.
    # Ejemplo: text = tk.Text(root, height=5, width=40)

# 5. Frame -> # Contenedor para agrupar otros widgets.
    # Ejemplo: frame = tk.Frame(root)

# 6. LabelFrame -> # Un contenedor con un borde y un título opcional para agrupar widgets relacionados.
    # Ejemplo: label_frame = tk.LabelFrame(root, text="Grupo de Widgets")

# 7. Checkbutton -> # Un botón de casilla de verificación que puede estar marcado o desmarcado.
    # Ejemplo: check = tk.Checkbutton(root, text="Opción")

# 8. Radiobutton -> # Botones de opción que permiten elegir una opción entre varias.
    # Ejemplo: radio = tk.Radiobutton(root, text="Opción 1", variable=var, value=1)

# 9. Listbox -> # Lista de elementos donde el usuario puede seleccionar uno o más elementos.
    # Ejemplo: listbox = tk.Listbox(root)

# 10. Spinbox -> # Campo de entrada con controles de aumento/disminución para seleccionar valores numéricos.
    # Ejemplo: spinbox = tk.Spinbox(root, from_=0, to=10)

# 11. Scale -> # Control deslizante para seleccionar un valor numérico dentro de un rango.
    # Ejemplo: scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)

# 12. Scrollbar -> # Barra de desplazamiento para widgets como Text, Listbox, etc.
    # Ejemplo: scrollbar = tk.Scrollbar(root)

# 13. Menu -> # Barra de menú desplegable que puede contener submenús y comandos.
    # Ejemplo: menu = tk.Menu(root)

# 14. Menubutton -> # Botón que abre un menú desplegable.
    # Ejemplo: menubutton = tk.Menubutton(root, text="Opciones")

# 15. Canvas -> # Un área para dibujar formas, gráficos, imágenes, etc.
    # Ejemplo: canvas = tk.Canvas(root, width=200, height=200)

# 16. Combobox (del módulo ttk) -> # Caja combinada de texto y lista desplegable.
    # Ejemplo: combobox = ttk.Combobox(root, values=["Opción 1", "Opción 2"])

# 17. Progressbar (del módulo ttk) -> # Barra de progreso visual que muestra el avance de una operación.
    # Ejemplo: progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate')

# 18. Notebook (del módulo ttk) -> # Pestañas para organizar múltiples páginas dentro de la ventana.
    # Ejemplo: notebook = ttk.Notebook(root)

# 19. Treeview (del módulo ttk) -> # Widget para mostrar datos en una estructura jerárquica similar a un árbol.
    # Ejemplo: tree = ttk.Treeview(root)

# 20. PanedWindow -> # Contenedor que organiza widgets en paneles redimensionables.
    # Ejemplo: paned = tk.PanedWindow(root)

# 21. Message -> # Similar a un Label, pero con soporte para mostrar textos más largos de forma automática.
    # Ejemplo: message = tk.Message(root, text="Este es un mensaje largo")

# 22. Toplevel -> # Crea una nueva ventana secundaria aparte de la ventana principal.
    # Ejemplo: top = tk.Toplevel(root)

# 23. Dialogbox (messagebox)  -> # Ventanas emergentes que muestran mensajes o piden confirmación al usuario.
    # Ejemplo: tk.messagebox.showinfo("Título", "Mensaje informativo")

# 24. Separator (del módulo ttk) -> # Línea separadora horizontal o vertical.
    # Ejemplo: separator = ttk.Separator(root, orient=tk.HORIZONTAL)

# ***********************************

""" Crear la ventana principal-Formulario """
root = tk.Tk()
root.title("Ejemplo de Tkinter")
root.geometry("300x250")


""" 
Metodo de ordenacion        pack() -> El wgt ocupa el primer sitio libre
"""
def on_label_pack_enter(event):
    label_pack["background"] = "#F5E5D3"

def on_label_pack_leave(event):
    label_pack["background"] = "#FDFE89"

# Crear una etiqueta con pack y poner evento de entrada y salida del raton
label_pack = tk.Label( root, text="Etiqueta con pack()", background="#FDFE89", foreground="#777777")
label_pack.bind("<Enter>", on_label_pack_enter)
label_pack.bind("<Leave>", on_label_pack_leave)
label_pack.pack()


""" 
Método ordenacion       grid()  -> En Grillas (filas x Columnas)
"""
# ********************************
# Crear un Frame dentro de root para utilizar el método grid()
frame_grid = tk.Frame(root, background="#F5E500")
frame_grid.pack()

# ---- Muestro diferentes maneras de Crear los widget
# *****************************************************
# A la etiqueta no le asigna variable pq no va a ser mas referenciada para hacer nada.
tk.Label(frame_grid, text="Etiqueta ", background="#F5E5D3", foreground="#777777").grid(row=0, column=0)

# ---- Primero creo el wgt y luego lo coloco.
entry1 = tk.Entry(frame_grid, background="#F5E5D3")
entry1.grid(row=0, column=1)    

# ---- Lo creo y lo coloco en una sola instruccion
tk.Label(frame_grid, text="Etiqueta", background="#AAAAAA", foreground="#777777").grid(row=1, column=0)

# ---- 
entry2 = tk.Entry(frame_grid, background="#F5E5D3").grid(row=1, column=1)    
# ------------------

"""
Metodo ordenacion        place()    -> Posicion fija
"""
# Una misma funcion para gestionar los diferentes eventos
# {partial} es una clase de {functools} que permite enviar parametros a un evento.
def on_button_click(button_name):
    print(f"El botón '{button_name}'  ha sido presionado")

# ----- Creo botones para usar la ordenacion place(personal x, y )
button = tk.Button(root, text="Botón1 con place()", command=partial(on_button_click, "btn01"))
button.place(x=120, y=120)

button2 = tk.Button(root, text="Botón2 con place()", command=partial(on_button_click, "btn02"))
button2.place(x=120, y= 150)


# ********************************
# Checkbutton y Radiobutton
# ********************************
def on_radiobutton_click():
    if opcion.get() == "Opt1":
        style.configure("Custom.TRadiobutton", background="#F5E5D3")
    else:
        style.configure("Custom.TRadiobutton", background="#FDFE89")

# Estilo personalizado para los Radiobuttons
# Los RadioButton no tienen propiedad background, asi que hay que crear un estilo y asignarlo
style = ttk.Style()
style.configure("Custom.TRadiobutton", background="#ABABAB")

# Establece la opcionByDef:
opcion = tk.StringVar(value="Opt1")

radiobutton1 = ttk.Radiobutton(root, text="Opción 1", value="Opt1", style="Custom.TRadiobutton" , 
                                variable=opcion,                                 
                                command=on_radiobutton_click)
radiobutton1.pack()

radiobutton2 = ttk.Radiobutton(root,text="Opción 2", value="Opt2",   style="Custom.TRadiobutton", 
                                variable=opcion, 
                                command=on_radiobutton_click)
radiobutton2.pack()


# ****************
root.mainloop()
# ****************
