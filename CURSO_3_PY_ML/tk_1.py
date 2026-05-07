import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd
import seaborn as sns
import numpy as np

# --- CARGA DE DATOS ---
try:
    df = pd.read_csv('/kaggle/input/iris/Iris.csv')
    if 'Id' in df.columns:
        df = df.drop(columns=['Id'])
except FileNotFoundError:
    df = sns.load_dataset('iris')
    df.columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']

def actualizar_grafico():
    tipo_grafico = combo_graficos.get()
    estilo_visual = combo_estilos.get()
    
    # Limpiamos la figura por completo
    fig.clf() 

    with plt.style.context(estilo_visual):
        fig.set_facecolor(plt.rcParams['figure.facecolor'])
        
        if tipo_grafico == "pairplot":
            # --- CONSTRUCCIÓN MANUAL DE PAIRPLOT (Para evitar TypeError) ---
            cols = df.select_dtypes(include=[np.number]).columns
            n = len(cols)
            # Creamos una sub-cuadrícula de ejes dentro de la figura actual
            axes = fig.subplots(n, n)
            
            for i, col_y in enumerate(cols):
                for j, col_x in enumerate(cols):
                    ax_curr = axes[i, j]
                    if i == j:
                        # Diagonal: Histogramas
                        sns.histplot(data=df, x=col_x, hue='Species', ax=ax_curr, legend=False, element="step")
                    else:
                        # Fuera de diagonal: Scatter plots
                        sns.scatterplot(data=df, x=col_x, y=col_y, hue='Species', ax=ax_curr, legend=False, s=15)
                    
                    # Limpiamos etiquetas para que no se vea amontonado
                    if i < n - 1: ax_curr.set_xlabel('')
                    if j > 0: ax_curr.set_ylabel('')
                    ax_curr.tick_params(labelsize=7)

            fig.suptitle("Matriz Pairplot Personalizada", color=plt.rcParams['text.color'], y=0.98)

        else:
            # Gráficos estándar de un solo eje
            ax = fig.add_subplot(111)
            ax.set_facecolor(plt.rcParams['axes.facecolor'])
            color_t = plt.rcParams['text.color']

            if tipo_grafico == "heatmap":
                corr = df.select_dtypes(include=['number']).corr()
                sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
                ax.set_title("Correlación de Pearson", color=color_t)

            elif tipo_grafico == "boxplot":
                df_melt = df.melt(id_vars='Species', var_name='Métrica', value_name='Valor')
                sns.boxplot(data=df_melt, x='Métrica', y='Valor', hue='Species', ax=ax)
                ax.set_title("Boxplot por Especie", color=color_t)
                plt.xticks(rotation=15)

            elif tipo_grafico == "violinplot":
                sns.violinplot(data=df, x='Species', y='PetalLengthCm', ax=ax)
                ax.set_title("Violin Plot: Petal Length", color=color_t)

        plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajuste para el título
    
    canvas.draw()

# --- INTERFAZ TKINTER (Igual que antes) ---
root = tk.Tk()
root.title("Analizador EDA Iris - Estable")
root.geometry("1100x850")

main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

sidebar = ttk.LabelFrame(main_frame, text=" Configuración ", padding="15")
sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

ttk.Label(sidebar, text="Tipo de Análisis:").grid(row=0, column=0, sticky="w")
combo_graficos = ttk.Combobox(sidebar, values=["pairplot", "heatmap", "boxplot", "violinplot"], state="readonly")
combo_graficos.current(0)
combo_graficos.grid(row=1, column=0, sticky="ew", pady=(0, 15))

ttk.Label(sidebar, text="Tema:").grid(row=2, column=0, sticky="w")
combo_estilos = ttk.Combobox(sidebar, values=["dark_background", "ggplot", "bmh", "seaborn-v0_8-whitegrid"], state="readonly")
combo_estilos.current(0)
combo_estilos.grid(row=3, column=0, sticky="ew", pady=(0, 15))

ttk.Button(sidebar, text="Actualizar Vista", command=actualizar_grafico).grid(row=4, column=0, sticky="ew", pady=10)

plot_container = ttk.Frame(main_frame)
plot_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

fig = plt.figure(figsize=(8, 7), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=plot_container)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

toolbar = NavigationToolbar2Tk(canvas, plot_container)
toolbar.update()

actualizar_grafico()
root.mainloop()