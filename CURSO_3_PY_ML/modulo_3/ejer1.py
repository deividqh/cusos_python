from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from  colorama import Fore, Style
# 1. Cargar el dataset

iris = datasets.load_iris()
print("type Iris:", type(iris) )
print("keys:", iris.keys())


X, y = iris.data, iris.target

print("type X:", type(X))
print("type y:", type(y))

# 2. Dividir en entrenamiento (70%) y prueba (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Crear y entrenar el modelo (Kernel Lineal)
modelo_svm = SVC(kernel='linear', verbose=True)
f = modelo_svm.fit(X_train, y_train)

# 4. Evaluación básica
precision = modelo_svm.score(X_test, y_test)
print(f"Precisión del modelo: {precision:.2f}")

# 5. Predicción de una nueva muestra desconocida
nueva_flor = np.array([[5.1, 3.5, 1.4, 0.2], [5.1, 4.5, 2.4, 0.2], [6.1, 3.5, 3.4, 0.2]])
prediccion = modelo_svm.predict(nueva_flor)

for i, flor in enumerate(prediccion):
    print(f"La flor pertenece a la especie: {Fore.CYAN}  {iris.target_names[prediccion][i]}  {Style.RESET_ALL})")