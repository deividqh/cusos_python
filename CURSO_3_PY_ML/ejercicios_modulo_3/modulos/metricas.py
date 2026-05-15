
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
def get_matriz_confusion(X_test, y_test, target_names):
    from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
    
    y_predict = modelo_entrenado.predict( X_test )    
    #  Generar la matriz de confusion
    c_matrix = confusion_matrix(y_test, y_predict)
    matriz_UI = ConfusionMatrixDisplay(confusion_matrix = c_matrix, display_labels = target_names)
    
    # ■ Retorna el display, solo le falta el estilo y show
    return matriz_UI
    # matriz_UI.plot(cmap='Reds')
    # plt.title("Matriz de Confusión: Diagnóstico Oncológico")
    # plt.show()

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ score :  Rendimiento del modelo
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ Conveniencia (score): 
#   • Es un "atajo". No necesitas predecir nada primero; el modelo lo hace internamente, compara y te da la nota. 
#   • Es ideal para un chequeo rápido.
def get_score(X_train, y_train, X_test, y_test):

    modelo   = SVC().fit(X_train, y_train)
    mod_score = modelo.score(X_test, y_test)
    print(f"Score/Precisión: {mod_score:.4f}")
    return mod_score.round(4)
""" La métrica precision_score responde a la pregunta: 
"De todos los casos que el modelo clasificó como positivos, ¿cuántas fueron correctas ?". """

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ accuracy_score :  EXACTITUD
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#   • En el ejemplo de la diana serían cuantos centros
#   • Es más formal. Primero sacas las predicciones con y_pred = modelo.predict(X) 
#     y luego comparas las dos listas de etiquetas. 
#   • Cuándo se usa: Cuando te importa el éxito general del modelo.
def get_accuracy_score(modelo, X_test, y_test):
    from sklearn.metrics import accuracy_score

    y_predict = modelo.predict(X_test)
    exactitud = accuracy_score(y_true = y_test, y_pred = y_predict)
    print(f"\n██•██ Exactitud/accuracy_score en el diagnóstico médico: {exactitud*100:.2f}% \n")
    # ■ NOTA:: Para usar accuracy_score, primero tienes que haber ejecutado predict() (no predict_proba), ya que esta función espera etiquetas (0, 1, 2...), no probabilidades (0.85, 0.15...).
    return exactitud.round(4)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ Recall ■ 
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# El Recall (o Sensibilidad) mide la capacidad del modelo para encontrar todos los casos positivos reales.
# Mientras que la Precisión se enfoca en "no mentir" (no dar falsos positivos), el Recall se enfoca en "no olvidar" (no dejar pasar casos positivos).
# FORMULA: TP/TP+FN
# ¿Cuándo se usa? Debes priorizar el Recall cuando el coste de omitir un caso positivo es muy alto (es decir, cuando los Falsos Negativos son peligrosos o costosos).
def get_recall(modelo, X_test, y_test):
    from sklearn.metrics import recall_score
    
    y_predict = modelo.predict(X_test)
    recall = recall_score(y_test, y_predict)
    print(f"Recall del modelo SVM: {recall:.2f}")
    return recall.round(2)


