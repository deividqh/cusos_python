import subprocess   
import sys 
from pathlib import Path


def st_ruta_completa(ejercicio:str):    
    try:
        print(f"Ejecutando Streamlit para el ejercicio 09...")
        result = subprocess.run([sys.executable, "-m", "streamlit", "run", str(ejercicio)], check=True)
        if result.returncode == 0:
            print("Streamlit se ejecutó correctamente.")
        else:
            print(f"Streamlit terminó con código de error: {result.returncode}")
    except Exception as e:
        print(f"Error al ejecutar Streamlit: {e}")

from pathlib import Path

def obtener_carpeta_proyecto(marcador: str = "requirements.txt") -> Path:
    """
    Devuelve exclusivamente la carpeta raíz del proyecto buscando un archivo marcador.
    """
    import pyrootutils

    # Encuentra la raíz buscando el archivo 'requirements.txt' desde donde esté este archivo
    raiz_proyecto = pyrootutils.find_root(search_from=__file__, indicator="requirements.txt")

    # Y ya puedes añadir tus paths relativos a mano de forma limpia:
    # ruta_app = raiz_proyecto / "app_completa.py"

    return raiz_proyecto

def ejercicios_regresion(ejercicio: str):
    # 1. Obtiene la carpeta raíz donde está este script principal (Ruta Absoluta)
    DIRECTORIO_ACTUAL = Path(__file__).resolve().parent
    
    # 2. Une la raíz con el parámetro recibido y lo convierte a STR absoluto
    # Usamos .as_posix() para que use barras '/' que Streamlit y Python entienden directo en cualquier OS
    # RUTA_ABSOLUTA_STR = (DIRECTORIO_ACTUAL / "/st_regresion/" / ejercicio).resolve().as_posix()
    RUTA_ABSOLUTA_STR = (DIRECTORIO_ACTUAL / f"st_regresion/{ejercicio}").resolve().as_posix()

    
    # 3. Lanzar Streamlit pasando el string
    print(f"Ejecutando Streamlit desde: {RUTA_ABSOLUTA_STR}")
    subprocess.run([sys.executable, "-m", "streamlit", "run", RUTA_ABSOLUTA_STR], check=True)

def ejercicio_01():
    ENUNCIADO = """ Actividad 1 - Rendimiento Académico: 
    Una academia desea predecir la nota final de un alumno basada únicamente en las horas de estudio semanales. 
    Genera un dataset sintético y aplica una Regresión Lineal Simple. Visualiza el resultado.
""" 
    # print(f"\n{Fore.BLUE}{ENUNCIADO}{Style.RESET_ALL}")

    ejercicios_regresion("st_reg_01.py")

def ejercicio_02():
    ENUNCIADO = """ Actividad 2 - Satisfacción Laboral (Inferencia): 
Utiliza Statsmodels para analizar si el número de días de teletrabajo al mes influye significativamente en 
el “Score de Felicidad” de los empleados. 
Interpreta el p-valor para una confianza del 95%.
"""  
    ejercicios_regresion("st_reg_02.py")

def ejercicio_03():
    ENUNCIADO = """ Actividad 3 - El Algoritmo desde Cero: 
Calcula manualmente los parámetros de una recta que relacione los “Minutos de uso de una App” con la “Batería consumida”. 
Valida tus cálculos comparándolos con el resultado de Scikit-Learn.
"""  
    ejercicios_regresion("st_reg_03.py")

def ejercicio_04():
    ENUNCIADO = """ Actividad 4 - Tasación de Vehículos: 
Crea un modelo de Regresión Múltiple para estimar el precio de venta de coches usados 
considerando: Años de antigüedad, Kilometraje y Caballos de fuerza (HP).
    """  
    ejercicios_regresion("st_reg_04.py")

def ejercicio_05():
    ENUNCIADO = """ Actividad 5 - Eficiencia Energética con Categorías: 
Predice el gasto en calefacción de una vivienda usando los metros cuadrados y la 
variable categórica “Tipo de Aislamiento” (Pobre, Medio, Excelente). No olvides usar One-Hot Encoding.
""" 
    ejercicios_regresion("st_reg_05.py")

def ejercicio_06():
    ENUNCIADO = """ Actividad 6 - Trayectoria de Mercado: Un producto nuevo presenta una curva de
ventas que aumenta rápido y luego se estabiliza. Aplica una Regresión Polinomial de
grado 2 y grado 3, y elige visualmente cuál captura mejor la tendencia.
"""  
    ejercicios_regresion("st_reg_06.py")

def ejercicio_07():
    ENUNCIADO = """Actividad 7 - Prevención del Overfitting: Genera un conjunto de datos con mucho
ruido que represente la temperatura horaria. Entrena modelos polinomiales de grado 1 al 15
y detecta en qué punto el modelo empieza a “memorizar” el ruido en lugar de la tendencia.
"""  
    ejercicios_regresion("st_reg_07.py")

def ejercicio_08():
    ENUNCIADO = """Actividad 8 - Diagnóstico Médico (Logística): Entrena un modelo de Regresión
Logística para predecir si un paciente tiene riesgo de hipertensión (1: Riesgo, 0: Normal)
basado en su nivel de estrés y edad.
"""  
    ejercicios_regresion("st_reg_08.py")

def ejercicio_09():
    ENUNCIADO = """Actividad 9 - Auditoría de Modelos de Fraude: Has entrenado un modelo para
detectar transacciones fraudulentas. Genera la Matriz de Confusión y el reporte de
clasificación. Explica por qué, en este caso, el “Recall” (Sensibilidad) es más importante
que la “Accuracy” (Exactitud).
"""     
    ejercicios_regresion("st_reg_09.py")

def ejercicio_10():
    ENUNCIADO = """Actividad 10 - Proyecto Final: Rendimiento Agrícola: Desarrolla un Pipeline completo
para predecir las toneladas de cosecha por hectárea. Debes incluir: carga de datos
(sintéticos), división Train/Test, entrenamiento de una regresión múltiple (usando agua,
fertilizante y horas de sol) y reporte de métricas MSE y R2. """
    ejercicios_regresion("st_reg_10.py")

def regresion_all():
    folder = obtener_carpeta_proyecto()
    # destino = folder / "ejercicios_modulo_3" / "st_regresion" / "st_reg_01.py"
    destino = folder / "app_completa.py"
    print(f"■█• Ejecutando Streamlit:  {destino}")
    st_ruta_completa(destino)
