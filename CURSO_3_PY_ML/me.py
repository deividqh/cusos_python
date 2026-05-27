""" 
from sklearn.linear_model import LinearRegression   # Para crear modelos de regresión lineal
import statsmodels.api as sm                # Para obtener un resumen estadístico
    
    modelo_stats = sm.OLS(y, X).fit()           # 3. Ajuste del modelo por Mínimos Cuadrados Ordinarios (OLS) 
    print(modelo_stats.summary())               # 4. Resumen del modelo con estadísticas detalladas
from sklearn.preprocessing import PolynomialFeatures
from sklearn.datasets import make_blobs                 # Ideal para generar datos sintéticos agrupados 
from sklearn.cluster import KMeans          # Para aplicar el algoritmo de clustering K-Means
from sklearn.semi_supervised import LabelPropagation    # Para aplicar el algoritmo de Propagación de Etiquetas (Label Propagation)
from sklearn.metrics import classification_report, confusion_matrix  # Para evaluar el rendimiento del modelo de clasificación


"""