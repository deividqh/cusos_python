import tarea8_modulo as t8
import os


y_true = [10,20,30]
y_pred = (12,18,33)

os.system('cls' if os.name == 'nt' else 'clear')

print(f"SOLUCION EJERCICIO METRICAS\n{'■'*30}")
print("MAE:", t8.mae(y_true, y_pred))
print("MSE:", t8.mse(y_true, y_pred))

# verificar manualmente
expected_mae = (2 + 2 + 3) / 3
expected_mse = ((2**2) + (2**2) + (3**2)) / 3
print(f"\nVerificacion manual:")
print(f"MAE esperado: {expected_mae}")
print(f"MSE esperado: {expected_mse}")

assert abs(t8.mae(y_true, y_pred) - expected_mae) < 1e-5, "Error en MAE"
assert abs(t8.mse(y_true, y_pred) - expected_mse) < 1e-5, "Error en MSE"
print("\n¡Todas las pruebas pasaron correctamente!")

