import numpy as np

def mae(y_true, y_pred):
  """
  Calcula el me o error absoluto medio(Mean absolute Error)
  y_true ees la lista/array de valores reales
  y_pred es la lista/array de los valores de prediccion
  Retorno = es el valor promedio de las diferencias
  """
  y_true=np.array(y_true)
  y_pred=np.array(y_pred)
  return np.mean(np.abs(y_true - y_pred))


def mse(y_true, y_pred):
  """
  Calcula el error cuadratico medio(Mean Square Error) MSE
  y_true ees la lista/array de valores reales
  y_pred es la lista/array de los valores de prediccion
  Retorno = es el valor promedio de los cuadrados de las diferencias
  """
  y_true=np.array(y_true)
  y_pred=np.array(y_pred)
  return np.mean(np.mean(y_true - y_pred)**2)



