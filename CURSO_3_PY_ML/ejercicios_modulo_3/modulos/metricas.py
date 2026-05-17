""" 
DEFINO LAS FUNCIONES DE LAS METRICAS PARA TENERLAS TODAS JUNTAS Y CLASIFICADAS Y
VALIDAS PARA CUALQUIER MODELO. 
PUEDO VER LOS PARAMETROS BASE QUE SE NECESITAN PARA FORMAR LA METRICA.
ES REDUNDANTE A LA HORA DE HACER predict EN CASO DE MAS DE 2 METRICAS QUE LO USEN PERO PARA EL ESTUDIO VALE.
"""
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay, recall_score, f1_score
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ INFORME DE CLASIFICACION
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
from sklearn.metrics import classification_report

def get_reporte_completo(modelo, X_test, y_test, target_names):    
    y_predict = modelo.predict(X_test)
    reporte = classification_report(y_test, y_predict, target_names=target_names)
    print("\n📈 📈  INFORME DE CLASIFICACIÓN  📈 📈 ")
    print(reporte)
    return reporte

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ MATRIZ DE CONFUSION
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Es el "mapa de errores" que te permite ver no solo cuántas veces falló el modelo, sino en qué se está confundiendo exactamente.
# Verdaderos Positivos (VP): El modelo dijo "Perro" y era un perro. ¡Acierto!
# Verdaderos Negativos (VN): El modelo dijo "No es perro" y realmente no era. ¡Acierto!
# Falsos Positivos (FP): El modelo dijo "Perro", pero era un gato. (También llamado Error Tipo I).
# Falsos Negativos (FN): El modelo dijo "No es perro", pero sí era. (También llamado Error Tipo II).
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def get_matriz_confusion(modelo, X_test, y_test, target_names):
    y_predict = modelo.predict(X_test)    
    c_matrix = confusion_matrix(y_test, y_predict)
    matriz_UI = ConfusionMatrixDisplay(confusion_matrix=c_matrix, display_labels=target_names)
    return matriz_UI
    # matriz_UI.plot(cmap='Reds')
    # plt.title("Matriz de Confusión: Diagnóstico Oncológico")
    # plt.show()

# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ MÉTRICAS INDIVIDUALES ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■

""" La métrica score responde a la pregunta: 
"De todos los casos que el modelo clasificó como positivos, ¿cuántas fueron correctas ?". 
• Es un "atajo". No necesitas predecir nada primero; el modelo lo hace internamente, compara y te da la nota. 
"""
# ■■■■■■ PRECISIÓN (SCORE) ■■■■■■
# Usamos el método .score() del modelo, que por defecto es el Accuracy
def get_accuracy(modelo, X_test, y_test):
    exactitud = modelo.score(X_test, y_test)
    print(f"📈 PRECISION (Accuracy): {exactitud*100:.2f}%")
    return round(exactitud.round , 4)

# ■■■■■■ EXACTITUD ( ACCURACY_SCORE ) ■■■■■■
#   • En el ejemplo de la diana serían cuantos centros
#   • Es más formal. Primero sacas las predicciones con y_pred = modelo.predict(X) 
#     y luego comparas las dos listas de etiquetas. 
#   • Cuándo se usa: Cuando te importa el éxito general del modelo.
def get_accuracy_score(modelo, X_test, y_test):
    from sklearn.metrics import accuracy_score
    
    """ Calcula la exactitud total: (TP+TN) / Total 
    # ■ NOTA:: Para usar accuracy_score, primero tienes que haber ejecutado predict() (no predict_proba), ya que esta función espera etiquetas (0, 1, 2...), no probabilidades (0.85, 0.15...)."""
    y_predict = modelo.predict(X_test)
    exactitud = accuracy_score(y_true=y_test, y_pred=y_predict)
    
    print(f"📈 EXACTITUD (accuracy_score): {exactitud*100:.2f}%")
    return round(exactitud, 4)


# ■■■■■■ SENSIBILIDAD ( RECALL ) ■■■■■■
# El Recall (o Sensibilidad) mide la capacidad del modelo para encontrar todos los casos positivos reales.
# Mientras que la Precisión se enfoca en "no mentir" (no dar falsos positivos), el Recall se enfoca en "no olvidar" (no dejar pasar casos positivos).
# FORMULA: TP/TP+FN
# ¿Cuándo se usa? Debes priorizar el Recall cuando el coste de omitir un caso positivo es muy alto (es decir, cuando los Falsos Negativos son peligrosos o costosos).
def get_recall(modelo, X_test, y_test):
    from sklearn.metrics import recall_score
    
    y_predict = modelo.predict(X_test)
    recall = recall_score(y_test, y_predict)
    print(f"📈 RECALL: {recall:.2f}")
    return round(recall ,4)


# ■■■■■■ ( F1-SCORE ) ■■■■■■
""" El F1-Score es tu mejor amigo cuando la Exactitud (Accuracy) te miente. 
En el mundo real, los datos rara vez están equilibrados, y ahí es donde el F1-Score brilla. 
■■■ 3 situaciones clave para usarlo:
    1. Cuando tienes Datasets Desequilibrados (El caso más común)
        Imagina que tienes un sistema de detección de fraudes donde el 99% de las transacciones son legales y solo el 1% son fraude.
        Si tu modelo es "vago" y dice siempre que "No es fraude", tendrá un 99% de Exactitud.
        Sin embargo, ese modelo es inútil porque no detecta ni un solo robo.
        El F1-Score en este caso sería cercano a 0, delatando que el modelo es en realidad un desastre.
    2. Cuando tanto los Falsos Positivos como los Falsos Negativos duelen
        El F1-Score es la "media armónica" entre la Precisión y el Recall. Lo usas cuando no puedes permitirte ignorar ninguno de los dos errores:
        Si priorizas la Precisión: Te preocupa mucho no dar falsas alarmas (Falsos Positivos).
        Si priorizas el Recall: Te preocupa mucho que no se te escape ningún caso real (Falsos Negativos).
        Si usas F1-Score: Quieres un modelo equilibrado que sea bueno en ambas cosas a la vez.
    3. En problemas de Clasificación Binaria Crítica
        Se usa por estándar en:
        Diagnósticos médicos: No quieres decirle a alguien sano que está enfermo, pero mucho menos quieres que alguien enfermo se vaya a casa pensando que está sano.
        Seguridad informática (tu ejercicio de intrusos): Quieres detectar al hacker (Recall), pero no quieres bloquear a tus empleados legítimos cada 5 minutos (Precision).
"""
def get_f1(modelo, X_test, y_test):
    from sklearn.metrics import  f1_score

    y_predict = modelo.predict(X_test)
    f1 = f1_score(y_test, y_predict)
    print(f"📈 F1-Score: {f1:.2f}")
    return round(f1 , 4)





