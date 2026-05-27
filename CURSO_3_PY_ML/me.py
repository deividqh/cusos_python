from sklearn.linear_model import LinearRegression
import statsmodels.api as sm 
    # 3. Ajuste del modelo por Mínimos Cuadrados Ordinarios (OLS) 
    modelo_stats = sm.OLS(y, X).fit()
    print(modelo_stats.summary())

from sklearn.preprocessing import PolynomialFeatures