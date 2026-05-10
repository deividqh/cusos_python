
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ INFORME DE CLASIFICACION
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
from sklearn.metrics import classification_report
print(classification_report(y_test, lda.predict( X_test ), target_names = iris.target_names))

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ MATRIZ DE CONFUSION
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Es el "mapa de errores" que te permite ver no solo cuántas veces falló el modelo, sino en qué se está confundiendo exactamente.
# Verdaderos Positivos (VP): El modelo dijo "Perro" y era un perro. ¡Acierto!
# Verdaderos Negativos (VN): El modelo dijo "No es perro" y realmente no era. ¡Acierto!
# Falsos Positivos (FP): El modelo dijo "Perro", pero era un gato. (También llamado Error Tipo I).
# Falsos Negativos (FN): El modelo dijo "No es perro", pero sí era. (También llamado Error Tipo II).

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
y_pred = modelo_entrenado.predict( X_test )
#  Generar la matriz de confusion
c_matrix = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix = c_matrix, display_labels = data.target_names)
disp.plot(cmap='Reds')
plt.title("Matriz de Confusión: Diagnóstico Oncológico")
plt.show()

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ score :  Rendimiento del modelo
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ Conveniencia (score): 
#   • Es un "atajo". No necesitas predecir nada primero; el modelo lo hace internamente, compara y te da la nota. 
#   • Es ideal para un chequeo rápido.
mod_fit   = SVC().fit(X_train_scaled, y_train)
mod_score = mod_fit.score(X_test_scaled, y_test)
print(f"Rendimiento: {mod_score:.4f}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ accuracy_score :  EXACTITUD
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#   • En el ejemplo de la diana serían cuantos centros
#   • Es más formal. Primero sacas las predicciones con y_pred = modelo.predict(X) 
#     y luego comparas las dos listas de etiquetas. 
#   • Cuándo se usa: Cuando te importa el éxito general del modelo.
from sklearn.metrics import accuracy_score
y_pred = mod_fit.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\n██•██ Precisión/accuracy_score en el diagnóstico médico: {acc*100:.2f}% \n")
# ■ NOTA:: Para usar accuracy_score, primero tienes que haber ejecutado predict() (no predict_proba), ya que esta función espera etiquetas (0, 1, 2...), no probabilidades (0.85, 0.15...).

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ Recall ■ 
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# El Recall (o Sensibilidad) mide la capacidad del modelo para encontrar todos los casos positivos reales.
# Mientras que la Precisión se enfoca en "no mentir" (no dar falsos positivos), el Recall se enfoca en "no olvidar" (no dejar pasar casos positivos).
# FORMULA: TP/TP+FN
# ¿Cuándo se usa? Debes priorizar el Recall cuando el coste de omitir un caso positivo es muy alto (es decir, cuando los Falsos Negativos son peligrosos o costosos).
from sklearn.metrics import recall_score
y_pred = modelo.predict(X_test)
recall = recall_score(y_test, y_pred)
print(f"Recall del modelo SVM: {recall:.2f}")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ Precisión (Precision) ■ 
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#   • Mide cuántos de los que el modelo marcó como "Positivos" eran realmente correctos.
#   • FORMULA: TP / TP + FP
#   • Es especialmente útil cuando el coste de un falso positivo es alto (por ejemplo, clasificar un correo legítimo como spam).
y_pred = modelo.predict(X_test)
# Esta métrica indica qué porcentaje de predicciones positivas fueron correctas.
precision = precision_score(y_test, y_pred)
print(f"Precisión del modelo SVM: {precision:.2f}")

""" La métrica precision_score responde a la pregunta: 
"De todos los casos que el modelo clasificó como positivos, ¿cuántas fueron correctas ?". """
