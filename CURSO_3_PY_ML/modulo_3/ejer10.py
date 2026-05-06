""" Ejercicio 10 - Pipeline Integral de Machine Learning
Objetivo: Crear una solución de extremo a extremo (End-to-End) robusta y profesional.
Enunciado del Reto: Como consultor experto, debes crear un "Pipeline" que automatice todo el flujo de
trabajo para nuevos datos de investigación floral: 1. Escale los datos, 2. Reduzca la dimensionalidad con LDA a
1 componente, y 3. Clasifique mediante SVM. Este pipeline debe ser capaz de entrenarse y predecir de forma
atómica. """

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn import datasets

# ■■■■■■■■■■■ Cargar datos
iris = datasets.load_iris()
X, y = iris.data, iris.target

# ■■■■■■■■■■■ Construcción del Pipeline Profesional
# ■■■■■■■■■■■ El Pipeline asegura que el escalado y la reducción se apliquen consistentemente
pipeline_floral = Pipeline([
('escalador', StandardScaler()),
('reductor_lda', LinearDiscriminantAnalysis(n_components=2)),
('clasificador_svm', SVC(kernel='poly', degree=3, C=1.0))
])

# ■■■■■■■■■■■ Entrenamiento completo del flujo
pipeline_floral.fit(X, y)

# ■■■■■■■■■■■ Simulación de llegada de nuevos datos
nuevos_datos = [[5.0, 3.6, 1.4, 0.2], [6.5, 3.0, 5.2, 2.0]]
predicciones = pipeline_floral.predict(nuevos_datos)
print("Predicciones del Pipeline para nuevas muestras:")

for i, pred in enumerate(predicciones):
    print(f" Muestra {i+1}: {iris.target_names[pred].upper()}")


""" Justificación: Demuestra la capacidad de creación al ensamblar múltiples componentes técnicos en una
solución arquitectónica coherente, escalable y reproducible. """

