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
    if 'Id' in df.columns: df = df.drop(columns=['Id'])
except:
    # Si falla la ruta de Kaggle, usamos la de Seaborn y renombramos para consistencia
    df = sns.load_dataset('iris')
    df.columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']

config_interactiva = {
    "SVM": {
        "C": {"tipo": "slider", "rango": (0.1, 10.0), "init": 1.0, "paso": 0.1},
        "kernel": {"tipo": "combo", "opciones": ["linear", "poly", "rbf", "sigmoid"], "init": "rbf"},
        "gamma": {"tipo": "combo", "opciones": ["scale", "auto"], "init": "scale"}
    },
    "Random Forest": {
        "n_estimators": {"tipo": "slider", "rango": (10, 200), "init": 100, "paso": 10},
        "max_depth": {"tipo": "slider", "rango": (1, 20), "init": 5, "paso": 1},
        "criterion": {"tipo": "combo", "opciones": ["gini", "entropy"], "init": "gini"}
    },
    "K-Means": {
        "n_clusters": {"tipo": "slider", "rango": (2, 10), "init": 3, "paso": 1},
        "init": {"tipo": "combo", "opciones": ["k-means++", "random"], "init": "k-means++"}
    },
    "Gaussian NB": {
        "var_smoothing": {"tipo": "slider", "rango": (0.000000001, 0.0000001), "init": 0.000000001, "paso": 0.000000001}
    }
}

widgets_activos = {}

def actualizar_interfaz_parametros(event=None):
    algoritmo = combo_algoritmos.get()
    for widget in frame_params_dinamico.winfo_children():
        widget.destroy()
    widgets_activos.clear()
    
    params = config_interactiva.get(algoritmo, {})
    for i, (nombre, config) in enumerate(params.items()):
        ttk.Label(frame_params_dinamico, text=f"{nombre}:", font=('Arial', 9, 'bold')).grid(row=i, column=0, sticky="w", pady=2)
        
        if config["tipo"] == "slider":
            var = tk.DoubleVar(value=config["init"])
            sc = tk.Scale(frame_params_dinamico, from_=config["rango"][0], to=config["rango"][1], 
                          resolution=config["paso"], variable=var, orient=tk.HORIZONTAL, 
                          length=150, font=('Arial', 8))
            sc.grid(row=i, column=1, sticky="ew", padx=5)
            widgets_activos[nombre] = var
        elif config["tipo"] == "combo":
            cb = ttk.Combobox(frame_params_dinamico, values=config["opciones"], state="readonly", width=15)
            cb.set(config["init"])
            cb.grid(row=i, column=1, sticky="ew", padx=5)
            widgets_activos[nombre] = cb

def actualizar_grafico():
    tipo_grafico = combo_graficos.get()
    estilo_visual = combo_estilos.get()
    algoritmo = combo_algoritmos.get()
    
    # Limpieza total de la figura
    fig.clf() 

    with plt.style.context(estilo_visual):
        fig.set_facecolor(plt.rcParams['figure.facecolor'])
        
        if tipo_grafico == "pairplot":
            cols = df.select_dtypes(include=[np.number]).columns
            n = len(cols)
            # El uso de subplots aquí es correcto tras fig.clf()
            axes = fig.subplots(n, n)
            for i, col_y in enumerate(cols):
                for j, col_x in enumerate(cols):
                    ax_curr = axes[i, j]
                    if i == j:
                        sns.histplot(data=df, x=col_x, hue='Species', ax=ax_curr, legend=False)
                    else:
                        sns.scatterplot(data=df, x=col_x, y=col_y, hue='Species', ax=ax_curr, legend=False, s=15)
                    ax_curr.tick_params(labelsize=7)
            fig.suptitle(f"Análisis Pairplot - Contexto: {algoritmo}", color=plt.rcParams['text.color'])

        else:
            ax = fig.add_subplot(111)
            ax.set_facecolor(plt.rcParams['axes.facecolor'])
            color_txt = plt.rcParams['text.color']
            
            if tipo_grafico == "heatmap":
                sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap="coolwarm", ax=ax)
            elif tipo_grafico == "boxplot":
                sns.boxplot(data=df.melt(id_vars='Species'), x='variable', y='value', hue='Species', ax=ax)
            elif tipo_grafico == "violinplot":
                sns.violinplot(data=df, x='Species', y='PetalWidthCm', ax=ax)
            
            ax.set_title(f"{tipo_grafico.capitalize()} - {algoritmo}", color=color_txt)

        # Usamos fig.tight_layout en lugar de plt para mayor precisión en Tkinter
        fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    canvas.draw()

# --- INTERFAZ ---
root = tk.Tk()
root.title("ML Simulator & EDA Dashboard Pro")
root.geometry("1200x850")

main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

sidebar = ttk.LabelFrame(main_frame, text=" Configuración ", padding="15")
sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

ttk.Label(sidebar, text="Algoritmo:").grid(row=0, column=0, sticky="w")
combo_algoritmos = ttk.Combobox(sidebar, values=list(config_interactiva.keys()), state="readonly")
combo_algoritmos.current(0)
combo_algoritmos.grid(row=1, column=0, sticky="ew", pady=(0, 10))
combo_algoritmos.bind("<<ComboboxSelected>>", actualizar_interfaz_parametros)

ttk.Label(sidebar, text="Gráfico:").grid(row=2, column=0, sticky="w")
combo_graficos = ttk.Combobox(sidebar, values=["pairplot", "heatmap", "boxplot", "violinplot"], state="readonly")
combo_graficos.current(0)
combo_graficos.grid(row=3, column=0, sticky="ew", pady=(0, 10))

ttk.Label(sidebar, text="Estilo:").grid(row=4, column=0, sticky="w")
combo_estilos = ttk.Combobox(sidebar, values=["dark_background", "ggplot", "bmh", "seaborn-v0_8-whitegrid"], state="readonly")
combo_estilos.current(0)
combo_estilos.grid(row=5, column=0, sticky="ew", pady=(0, 15))

frame_params_dinamico = ttk.Frame(sidebar)
frame_params_dinamico.grid(row=6, column=0, sticky="nsew", pady=10)

btn_update = ttk.Button(sidebar, text="🚀 Actualizar Vista", command=actualizar_grafico)
btn_update.grid(row=7, column=0, sticky="ew", pady=20)

plot_container = ttk.Frame(main_frame)
plot_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

fig = plt.figure(figsize=(8, 7), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=plot_container)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

toolbar = NavigationToolbar2Tk(canvas, plot_container)
toolbar.update()

actualizar_interfaz_parametros()
actualizar_grafico()

root.mainloop()