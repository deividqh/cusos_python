import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg , NavigationToolbar2Tk
import tkinter as tk
from tkinter import ttk
import numpy as np

def actualizar_grafico():

    # Nuevo tipo de gráfico seleccionado
    nuevo_grafico = combo_graficos.get()

    # Obtenemos el estilo seleccionado
    new_estilo = combo_estilos.get()

    # Actualizamos los datos del gráfico
    x = np.random.randint(low=0, high=10, size=10)  
    y = np.random.randint(low=0, high=10, size=10)  
    
    with plt.style.context(new_estilo):

        ax.clear()  # Limpiamos el gráfico anterior

        # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ACTUALIZACIÓN CLAVE: Sincronizar colores de fondo con el estilo seleccionado
        # • El problema es que al usar 'style.context' dentro de la función, Matplotlib cambia los colores
        #   de los elementos nuevos (líneas, puntos), pero no actualiza automáticamente el color de fondo 
        #   del objeto 'figure' que ya fue creado al inicio.
        # • Para solucionarlo, hay que forzar la actualización del color de fondo de la figura (facecolor) 
        #   dentro del contexto del estilo.
        fig.set_facecolor( color = plt.rcParams['figure.facecolor'] )
        ax.set_facecolor( plt.rcParams['axes.facecolor'] )
        # ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
        # Criterio de selección del tipo de gráfico a dibujar
        if nuevo_grafico == "plot":
            ax.plot(x, y)                      # Dibujamos el nuevo gráfico
        elif nuevo_grafico == "scatter":
            ax.scatter(x, y, color='red')      # distribución de variable x e y.
        elif nuevo_grafico == "histogram":     # distribución de una sola variable.
            ax.hist(x, bins='auto')            # Dibujamos el nuevo gráfico
        elif nuevo_grafico == "bar":     # distribución de una sola variable.
            ax.bar(np.arange(len(y)), y)
        elif nuevo_grafico == "stem":     # distribución de una sola variable.
            ax.stem(x, y)            # Dibujamos el nuevo gráfico
        elif nuevo_grafico == "step":     # distribución de una sola variable.
            ax.step(x, y)            # Dibujamos el nuevo gráfico
        elif nuevo_grafico == "boxplot":     # distribución de una sola variable.
            ax.boxplot([x, y])            # Dibujamos el nuevo gráfico
        elif nuevo_grafico == "violin":
            ax.violinplot([x, y])
        elif nuevo_grafico == "pie":
            ax.pie(x, labels=y)
        elif nuevo_grafico == "area":
            ax.fill_between(x, y)

        ax.legend()
        ax.set_title(f"Estilo: {new_estilo}", color=plt.rcParams['text.color'])
    
    # ■ Redibuja el canvas para mostrar el nuevo gráfico
    canvas.draw()  

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
# Inicializamos la ventana de Tkinter
root = tk.Tk()

# ■■■■ Cachamos las subclases figure y axes para crear el gráfico
# • 'figure' lo vamos a necesitar para crear el canvas 
# • 'axes' lo vamos a necesitar para manejar los datos del gráfico y dibujarlo.
fig , ax = plt.subplots()

frame = tk.Frame(root)
frame.pack()
label = tk.Label(frame, text="matplotlib en Tkinter!!")
label.pack()

# ■■■■ Crea un 'canvas' para mostrar el gráfico en la ventana de 'Tkinter'
canvas = FigureCanvasTkAgg(figure = fig, master=frame)
canvas.get_tk_widget().pack()

# ■■■ Agrega la barra de herramientas de navegación
# toolbar = NavigationToolbar2Tk(canvas, frame) 
# toolbar.update()
# toolbar.pack() # Empaquetamos la barra de herramientas para mostrarla en la ventana 

frame.pack() # Empaquetamos el frame para mostrarlo en la ventana

tk.Button(master = frame, text="Actualizar Gráfico", command=actualizar_grafico).pack(pady=15) # Botón para actualizar el gráfico

# ■ ■ ■ ■ ■ ■ ■ Lista de estilos solicitados
estilos = [
    "dark_background", "bmh", "ggplot", "fivethirtyeight", 
    "seaborn-v0_8-darkgrid", "seaborn-v0_8-whitegrid", 
    "seaborn-v0_8-poster", "seaborn-v0_8-talk", "seaborn-v0_8-ticks"
]
# Combobox para seleccionar estilo
tk.Label(frame, text="Selecciona un estilo:").pack()
combo_estilos = ttk.Combobox(master = frame, values=estilos, state="readonly")
combo_estilos.current(0) # Por defecto el primero
combo_estilos.pack(pady=5)
# ■ ■ ■ ■ ■ ■ 

# ■ ■ ■ ■ ■ ■ ■ Lista de graficos 
graficos = ["plot", "scatter", "histogram", "bar", "stem", "step", "boxplot", "violin", "pie", "area"]
# Combobox para seleccionar tipo de gráfico
tk.Label(frame, text="Selecciona un tipo de gráfico:").pack()
combo_graficos = ttk.Combobox(master = frame, values=graficos, state="readonly")
combo_graficos.current(0) # Por defecto el primero
combo_graficos.pack(pady=5)

# ■■■■ Muestra la ventana de 'Tkinter' con el gráfico cargado y dibujado.
root.mainloop()
