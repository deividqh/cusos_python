import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np

root = tk.Tk()

# ■■■■ Cachamos las subclases figure y axes para crear el gráfico
# • 'figure' lo vamos a necesitar para crear el canvas 
# • 'axes' lo vamos a necesitar para manejar los datos del gráfico y dibujarlo.
fig , ax = plt.subplots()

# ■■■■ Creamos los datos para el gráfico
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y)


# ■■■■ Crea un 'canvas' para mostrar el gráfico en la ventana de 'Tkinter'
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# ■■■■ Muestra la ventana de 'Tkinter' con el gráfico cargado y dibujado.
root.mainloop()
