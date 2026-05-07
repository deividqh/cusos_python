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

# --- DICCIONARIO DE APRENDIZAJE: PARÁMETROS POR ALGORITMO ---
info_parametros = {
    "SVM": [
        ("C", "Regularización: Controla el error."),
        ("Kernel", "Función: Transforma los datos (RBF, Lineal)."),
        ("Gamma", "Influencia: Qué tan lejos llega un ejemplo.")
    ],
    "Gaussian NB": [
        ("Priors", "Probabilidades previas de las clases."),
        ("Var Smoothing", "Estabilidad: Porción de la varianza mayor.")
    ],
    "Random Forest": [
        ("n_estimators", "Árboles: Cuántos bosques crear."),
        ("max_depth", "Profundidad: Límite de crecimiento."),
        ("min_samples_split", "División: Mínimo para separar nodo.")
    ],
    "K-Means": [
        ("n_clusters", "K: Número de grupos a encontrar."),
        ("init", "Método de inicialización (k-means++)."),
        ("max_iter", "Iteraciones máximas del algoritmo.")
    ]
}

def actualizar_parametros_ui(algoritmo):
    """Limpia y dibuja los parámetros del algoritmo seleccionado."""
    # Eliminamos los labels anteriores del frame de parámetros
    for widget in frame_params_dinamico.winfo_children():
        widget.destroy()
    
    params = info_parametros.get(algoritmo, [])
    
    for i, (nombre, desc) in enumerate(params):
        # Nombre del parámetro en negrita
        lbl_nom = ttk.Label(frame_params_dinamico, text=f"• {nombre}:", font=('Arial', 9, 'bold'))
        lbl_nom.grid(row=i, column=0, sticky="w", pady=(2, 0))
        
        # Descripción debajo o al lado
        lbl_desc = ttk.Label(frame_params_dinamico, text=desc, font=('Arial', 8), foreground="gray")
        lbl_desc.grid(row=i, column=1, sticky="w", padx=5, pady=(2, 0))

def actualizar_grafico():
    tipo_grafico = combo_graficos.get()
    estilo_visual = combo_estilos.get()
    algoritmo_actual = combo_algoritmos.get()
    
    # Actualizar la lista de parámetros en la UI
    actualizar_parametros_ui(algoritmo_actual)
    
    fig.clf() 

    with plt.style.context(estilo_visual):
        fig.set_facecolor(plt.rcParams['figure.facecolor'])
        
        if tipo_grafico == "pairplot":
            cols = df.select_dtypes(include=[np.number]).columns
            n = len(cols)
            axes = fig.subplots(n, n)
            for i, col_y in enumerate(cols):
                for j, col_x in enumerate(cols):
                    ax_curr = axes[i, j]
                    if i == j:
                        sns.histplot(data=df, x=col_x, hue='Species', ax=ax_curr, legend=False, element="step")
                    else:
                        sns.scatterplot(data=df, x=col_x, y=col_y, hue='Species', ax=ax_curr, legend=False, s=15)
                    if i < n - 1: ax_curr.set_xlabel('')
                    if j > 0: ax_curr.set_ylabel('')
                    ax_curr.tick_params(labelsize=7)
            fig.suptitle(f"EDA - Enfoque: {algoritmo_actual}", color=plt.rcParams['text.color'])

        else:
            ax = fig.add_subplot(111)
            ax.set_facecolor(plt.rcParams['axes.facecolor'])
            color_t = plt.rcParams['text.color']

            if tipo_grafico == "heatmap":
                corr = df.select_dtypes(include=['number']).corr()
                sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
                ax.set_title(f"Matriz de Correlación ({algoritmo_actual})", color=color_t)

            elif tipo_grafico == "boxplot":
                df_melt = df.melt(id_vars='Species', var_name='Métrica', value_name='Valor')
                sns.boxplot(data=df_melt, x='Métrica', y='Valor', hue='Species', ax=ax)
                ax.set_title(f"Boxplot - Preparación para {algoritmo_actual}", color=color_t)
                plt.xticks(rotation=15)

            elif tipo_grafico == "violinplot":
                sns.violinplot(data=df, x='Species', y='PetalLengthCm', ax=ax)
                ax.set_title(f"Análisis de Densidad ({algoritmo_actual})", color=color_t)

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    canvas.draw()

# --- INTERFAZ TKINTER ---
root = tk.Tk()
root.title("Dashboard Educativo: EDA & Algoritmos")
root.geometry("1200x850")

main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# Sidebar
sidebar = ttk.LabelFrame(main_frame, text=" Configuración ", padding="15")
sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

# Selectores
ttk.Label(sidebar, text="1. Algoritmo a Estudiar:").grid(row=0, column=0, sticky="w")
combo_algoritmos = ttk.Combobox(sidebar, values=list(info_parametros.keys()), state="readonly")
combo_algoritmos.current(0)
combo_algoritmos.grid(row=1, column=0, sticky="ew", pady=(0, 15))

ttk.Label(sidebar, text="2. Tipo de Gráfico:").grid(row=2, column=0, sticky="w")
combo_graficos = ttk.Combobox(sidebar, values=["pairplot", "heatmap", "boxplot", "violinplot"], state="readonly")
combo_graficos.current(0)
combo_graficos.grid(row=3, column=0, sticky="ew", pady=(0, 15))

ttk.Label(sidebar, text="3. Tema:").grid(row=4, column=0, sticky="w")
combo_estilos = ttk.Combobox(sidebar, values=["dark_background", "ggplot", "bmh", "seaborn-v0_8-whitegrid"], state="readonly")
combo_estilos.current(0)
combo_estilos.grid(row=5, column=0, sticky="ew", pady=(0, 15))

btn_update = ttk.Button(sidebar, text="📊 Actualizar Vista", command=actualizar_grafico)
btn_update.grid(row=6, column=0, sticky="ew", pady=20)

# --- SECCIÓN DE APRENDIZAJE DE PARÁMETROS ---
lbl_frame_params = ttk.LabelFrame(sidebar, text=" Parámetros del Modelo ", padding="10")
lbl_frame_params.grid(row=7, column=0, sticky="nsew", pady=10)

# Frame interno que limpiaremos y llenaremos
frame_params_dinamico = ttk.Frame(lbl_frame_params)
frame_params_dinamico.pack(fill=tk.BOTH, expand=True)

# Área de Gráficos
plot_container = ttk.Frame(main_frame)
plot_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

fig = plt.figure(figsize=(8, 7), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=plot_container)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

toolbar = NavigationToolbar2Tk(canvas, plot_container)
toolbar.update()

# Ejecución inicial
actualizar_grafico()
root.mainloop()