# https://www.kaggle.com/code/joeportilla/analisis-exploratorio-de-datos-dataset-iris
# https://rpubs.com/jigbadouin/EDAIRIS01
TEXTO = """ Ejercicio 1 - Clasificación Básica con SVM (Iris) 🌷🌷🌷🌷
Objetivo: Aplicar los conceptos fundamentales de Support Vector Machines para una clasificación multiclase.
Enunciado del Reto: Un equipo de botánicos necesita automatizar la identificación de la especie Iris
basándose en medidas físicas. Tu tarea es cargar el dataset Iris de Scikit-Learn, dividirlo en entrenamiento y
prueba, y entrenar un modelo SVM con kernel lineal para predecir la especie de una muestra desconocida. """

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from  colorama import Fore, Style
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os           #Para Limpiar la terminal con  os.system('cls') 
import  menuDvd     #Funcion que crea un menu y devuelve un int(opcion)

print (f"\n{Fore.BLUE}{TEXTO}{Style.RESET_ALL}")    

# █████████ 1. 🌷 Cargar el dataset ( Finsher - 1930 )
iris = datasets.load_iris()   
X, y = iris.data, iris.target
print("\n■■■■■■■■■ DATOS INICIALES")
# print(y)

# ■■■■■■■■■ 📉 Analisis de los datos ::: EDA
# ■ Crear el DataFrame con los nombres de las columnas
df = pd.DataFrame(data = X, columns = iris.feature_names)

# ■ Añadir la columna de especie (traducida de número a nombre)
df['species'] = [iris.target_names[i] for i in y]
print("■ Vista previa del DataFrame Iris:")
print(df.head())

# ■ MENU 
menu={  
    "Grafico pairplot": None, 
    "Grafico displot": None , 
}
sns.set_theme(style="ticks")

while (True):
    i = menuDvd.MenuDiccionario(menu, tituloMenu='Mod3 - Ejercicio 1 -  Graficas EDA', num_char=60)
    if i == 0: break  #PRIMERO LA DE SALIDA
    for index , opt in enumerate(menu):
        if i ==  1:
            # grafico = sns.pairplot(data=df, hue="species", palette="bright" )
            grafico = sns.pairplot(data=df, hue="species" )
            # grafico.fig.suptitle("Dispersión de Especies Iris", y=1.02)
            plt.show()
            break

        elif i == 2:
            sns.displot(df, x="petal width (cm)", hue="species", kind="kde", fill=True)
            plt.show()
            break
        
        pass
# ■■■■■■■■■ SALIDA MENU
# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
# ■ De aquí tenemos que salir con una idea de que 'Algoritmo' y 'Modelo'  queremos generar. 
# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 

# █████████ ✂️ Dividir en entrenamiento (70%) y prueba (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("•••••••••••• SPLIT train/test/ ✔️")

# █████████ 🧠 Crear el modelo sobre el algoritmo SVC con Kernel Lineal (byDef 'rbf')
#   • Elige modelo : [SVC, Gaussian]               .... depende de la naturaleza de los datos 
#   • Si SVC ... elige kernel : [linear, rbf, poly, sigmoid]  .... depende de la naturaleza de los datos
modelo_svm = SVC(kernel='linear', probability=True)
# modelo_svm = SVC(kernel='rbf', probability=True)
# modelo_svm = SVC(kernel='poly', probability=True)
# modelo_svm = SVC(kernel='sigmoid', probability=True)
print("•••••••••••• Modelo Cargado/ ✔️")

# █████████ 👟 Entrenar el Modelo SVC
fit = modelo_svm.fit(X_train, y_train)
print(f'PARAMETROS DEL MODELO: {modelo_svm.get_params(deep=True)}')

# ■ 🎲 Probabilidad (siempre despues de 'fit')
# Mientras que predict() te dice "esto es una Setosa", predict_proba() te dice "hay un 90% de probabilidad de que sea Setosa y un 10% de Versicolor"
# Devuelve un array de NumPy con una estructura de [n_samples, n_classes]
probabilidades = modelo_svm.predict_proba( X = X_test )
proba_view = probabilidades[:5]
print(f"\n■■■■■ Probabilidades del Test: "
f' \n[ % setosa(0), % versicolor(1) , % virginica ] ... hay que elegir el valor mayor(max)\n{proba_view.round(3)}' )

#  🎯 Precisión/score: El modelo se auto-analiza.
precision = modelo_svm.score(X_test, y_test)
print(f"\n■■■■■ Precisión/ Score del modelo sobre el Test(score) despues de ser entrenado: {precision:.2f}")

# █████████ 🔮 PREDICCION ... Con los elementos a 'predict', hago una consulta a la bolita magica
# ■ 🌷 Creo unos elementos (dentro del rango probable) con numpy
nueva_flor = np.array([[6.0, 5, 2, 1.2], [5.1, 4.5, 2.4, 0.2], [6.1, 3.5, 3.4, 0.2]])
print(f"\n■■■■■ Muestras: \n{nueva_flor.round(3)}")

# ■ 🔮 🔮 Predict ... hago una consulta a la bolita magica
predicciones_nuevas = modelo_svm.predict(X=nueva_flor)
print("•••••••••••• Prediccion Terminada ✔️")

# ■ 🎲 PROBABILIDAD Por cada nueva flor o array de flores, hay nuevas probabilidades
# ■ 🎲 Es un array de array np con la misma dimension que la nueva_flor
probabilidades_nuevas = modelo_svm.predict_proba(X=nueva_flor)
print(f'\n∟∟∟∟∟∟∟∟Predict Proba sobre Muestras:\n{probabilidades_nuevas.round(3)}\n')

l_percent = [ probabilidades_nuevas[i] for i, new_p in enumerate(probabilidades_nuevas) ]
np_l_percent = np.array(l_percent)*100
np_l_percent = np_l_percent.round(3)
new_percent = np.max(np_l_percent, axis=1)
print(f'Calculo de procentajes con lista compresion: \n{new_percent}')

# ■■■■■■■■■ 🖥️ Visualización por Consola.
for i, clase_idx in enumerate(predicciones_nuevas):
    nombre = iris.target_names[clase_idx]
    porcentaje = np.max(probabilidades_nuevas[i]) * 100
    
    print(f"► Flor {i+1}: {Fore.CYAN}{nombre}{Style.RESET_ALL} "
          f"(Confianza: {porcentaje:.2f} %)")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■          
print(f'\n {'■'*30}')
print("■ type Iris:", type(iris) )
print("■ keys:", iris.keys())
print("■ type X:", type(X))
print("■ type y:", type(y))
print(f'■ type x train: {type(X_train)} \n■ type y train: {type(y_train)}')
print("■ type fit:", type(fit))
print("■ type precision:", type(precision))
print("■ type modelo:", type(modelo_svm))
print(f'■ type Prediccion: {type(predicciones_nuevas)}')
print(f'■ type target_names: {type(iris.target_names)}')

print(""" Justificación: El alumno demuestra capacidad de aplicación al integrar el flujo básico de Scikit-Learn (Carga,
Split, Fit, Predict) en un problema de clasificación estándar. 
La elección de SVM con kernel lineal es adecuada para el dataset Iris, y la evaluación se realiza de forma
sencilla pero efectiva, mostrando comprensión de la precisión como métrica. La predicción de nuevas muestras añade un toque práctico al ejercicio. 
""")
