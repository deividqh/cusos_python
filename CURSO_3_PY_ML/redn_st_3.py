import streamlit as st
import tensorflow as tf
import numpy as np
import plotly.graph_objects as go
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model

# Configuración de página en modo ancho estándar
st.set_page_config(layout="wide", page_title="Actividad - Red Neuronal MNIST")

# ■■■■■ 1. TÍTULO DE LA ACTIVIDAD ■■■■■
st.markdown("### Ejercicio: Entrenamiento de Redes Neuronales (Clasificación MNIST)")

# ■■■■■ Carga de datos global en Caché ■■■■■
@st.cache_data
def cargar_datos():
    """Descarga y normaliza el dataset MNIST una sola vez."""
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    x_train = x_train[..., tf.newaxis].astype("float32")
    x_test = x_test[..., tf.newaxis].astype("float32")
    return x_train, y_train, x_test, y_test

x_train, y_train, x_test, y_test = cargar_datos()

# ■■■■■ 2. ENUNCIADO EN COLLAPSE (CON DATOS DE MUESTRA) ■■■■■
ENUNCIADO = """En esta actividad vamos a entrenar una Red Neuronal Convolucional (CNN) sencilla para clasificar imágenes de dígitos escritos a mano (del 0 al 9) usando el famoso dataset MNIST.

A través del panel de control inferior, puedes modificar los hiperparámetros del algoritmo:
* **Épocas:** Cuántas veces verá la red neuronal el dataset completo.
* **Batch Size:** Cuántas imágenes procesa a la vez antes de actualizar sus pesos.
* **Shuffle Buffer:** El tamaño de la muestra que mezcla los datos para evitar sesgos durante el entrenamiento.
"""

with st.expander("📖 Ver el Enunciado y Exploración de los Datos", expanded=False):
    st.write(ENUNCIADO)
    st.markdown("---")
    st.markdown("#### 📂 Exploración del Dataset MNIST")
    
    col_info1, col_info2, col_img = st.columns([1.5, 1.5, 1])
    
    with col_info1:
        st.info(f"**Set de Entrenamiento:**\n\nImágenes: {x_train.shape}\nEtiquetas: {y_train.shape}")
    with col_info2:
        st.info(f"**Set de Prueba (Test):**\n\nImágenes: {x_test.shape}\nEtiquetas: {y_test.shape}")
    with col_img:
        st.markdown("**Muestra Visual (Ejemplo 0):**")
        st.image(x_train[0].numpy() if isinstance(x_train[0], tf.Tensor) else x_train[0], 
                 width=100, 
                 caption=f"Etiqueta real: {y_train[0]}")


# ■■■■■ 3. PANEL DE CONTROLES ■■■■■
st.markdown("### 🎛️ Panel de Simulación y Control de Hiperparámetros")
with st.container(border=True):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        EPOCHS = st.slider("Número de Épocas:", min_value=1, max_value=20, value=5)
    with c2:
        BATCH_SIZE = st.selectbox("Tamaño del Batch:", [16, 32, 64, 128, 256], index=1)
    with c3:
        SHUFFLE_SIZE = st.number_input("Tamaño de Mezcla (Shuffle):", min_value=1000, max_value=60000, value=10000, step=1000)
    with c4:
        st.write("") # Espaciador para alinear el botón verticalmente
        iniciar_entrenamiento = st.button("🚀 Iniciar Entrenamiento", type="primary", use_container_width=True)


# ■■■■■ 4. PROCESAMIENTO DE DATOS Y MODELADO ■■■■■
# A diferencia de una regresión rápida, el entrenamiento de una Red Neuronal 
# bloquea el flujo. Por eso lo ejecutamos solo si se pulsa el botón.
if iniciar_entrenamiento:
    
    # 1. Preparar Datasets con los controles seleccionados
    train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(SHUFFLE_SIZE).batch(BATCH_SIZE)
    test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(BATCH_SIZE)

    # 2. Definición del Modelo
    class MyModel(Model):
        def __init__(self):
            super().__init__()
            self.conv1 = Conv2D(32, 3, activation='relu')
            self.flatten = Flatten()
            self.d1 = Dense(128, activation='relu')
            self.d2 = Dense(10)

        def call(self, x):
            x = self.conv1(x)
            x = self.flatten(x)
            x = self.d1(x)
            return self.d2(x)

    model = MyModel()
    loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    optimizer = tf.keras.optimizers.Adam()

    # Métricas
    train_loss = tf.keras.metrics.Mean(name='train_loss')
    train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='train_accuracy')
    test_loss = tf.keras.metrics.Mean(name='test_loss')
    test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='test_accuracy')

    @tf.function
    def train_step(images, labels):
        with tf.GradientTape() as tape:
            predictions = model(images, training=True)
            loss = loss_object(labels, predictions)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))
        train_loss(loss)
        train_accuracy(labels, predictions)

    @tf.function
    def test_step(images, labels):
        predictions = model(images, training=False)
        t_loss = loss_object(labels, predictions)
        test_loss(t_loss)
        test_accuracy(labels, predictions)

    st.markdown("---")
    st.markdown("### 📉 Entrenamiento Dinámico del Modelo")
    
    # Contenedores para UI en tiempo real
    txt_estado = st.empty()
    barra_progreso = st.progress(0.0)
    
    # Dos columnas para los gráficos interactivos
    col_grafico1, col_grafico2 = st.columns(2)
    grafico_perdida = col_grafico1.empty()
    grafico_precision = col_grafico2.empty()

    hist_epochs = []
    hist_train_loss, hist_test_loss = [], []
    hist_train_acc, hist_test_acc = [], []

    # Bucle de Entrenamiento
    for epoch in range(EPOCHS):
        # UI actualizando estado
        txt_estado.info(f"⏳ **Procesando Época {epoch + 1} de {EPOCHS}...** Por favor, espera.")
        
        # Resetear métricas
        train_loss.reset_state()
        train_accuracy.reset_state()
        test_loss.reset_state()
        test_accuracy.reset_state()

        # Entrenamiento
        for images, labels in train_ds:
            train_step(images, labels)

        # Validación
        for test_images, test_labels in test_ds:
            test_step(test_images, test_labels)

        # Recoger datos
        hist_epochs.append(epoch + 1)
        hist_train_loss.append(train_loss.result().numpy())
        hist_test_loss.append(test_loss.result().numpy())
        hist_train_acc.append(train_accuracy.result().numpy() * 100)
        hist_test_acc.append(test_accuracy.result().numpy() * 100)

        # Gráfico Plotly: Pérdida
        fig_loss = go.Figure()
        fig_loss.add_trace(go.Scatter(x=hist_epochs, y=hist_train_loss, mode='lines+markers', name='Train Loss', line=dict(color='#1f77b4', width=3)))
        fig_loss.add_trace(go.Scatter(x=hist_epochs, y=hist_test_loss, mode='lines+markers', name='Test Loss', line=dict(color='#ff7f0e', width=3)))
        fig_loss.update_layout(title='Evolución de la Pérdida (Log Loss)', xaxis_title='Época', yaxis_title='Loss', template='plotly_white', margin=dict(t=40, b=0))
        grafico_perdida.plotly_chart(fig_loss, use_container_width=True)

        # Gráfico Plotly: Precisión
        fig_acc = go.Figure()
        fig_acc.add_trace(go.Scatter(x=hist_epochs, y=hist_train_acc, mode='lines+markers', name='Train Accuracy', line=dict(color='#2ca02c', width=3)))
        fig_acc.add_trace(go.Scatter(x=hist_epochs, y=hist_test_acc, mode='lines+markers', name='Test Accuracy', line=dict(color='#d62728', width=3)))
        fig_acc.update_layout(title='Evolución de la Exactitud (Accuracy %)', xaxis_title='Época', yaxis_title='Precisión (%)', template='plotly_white', margin=dict(t=40, b=0))
        grafico_precision.plotly_chart(fig_acc, use_container_width=True)

        # Actualizar progreso
        barra_progreso.progress((epoch + 1) / EPOCHS)

    # Limpiar el mensaje de estado al terminar
    txt_estado.success("✅ ¡Entrenamiento completado exitosamente!")


    # ■■■■■ 5. PANEL INFERIOR (MÉTRICAS Y CONCLUSIONES) ■■■■■
    st.markdown("---")
    st.markdown("### 📊 Métricas Finales de Rendimiento")

    # Extraer los últimos valores conseguidos
    fin_train_acc = hist_train_acc[-1]
    fin_test_acc = hist_test_acc[-1]
    fin_train_loss = hist_train_loss[-1]
    fin_test_loss = hist_test_loss[-1]

    # Mostramos 4 métricas usando columnas
    m1, m2, m3, m4 = st.columns(4)

    m1.metric(label="Precisión Final (Training)", 
              value=f"{fin_train_acc:.2f} %", 
              delta="Datos que el modelo ha visto")
    
    m2.metric(label="Precisión Final (Testing)", 
              value=f"{fin_test_acc:.2f} %", 
              delta="Datos invisibles para el modelo")
    
    m3.metric(label="Pérdida Final (Train Loss)", 
              value=f"{fin_train_loss:.4f}", 
              delta="Menor entropía es mejor", delta_color="inverse")
    
    m4.metric(label="Pérdida Final (Test Loss)", 
              value=f"{fin_test_loss:.4f}", 
              delta="Menor entropía es mejor", delta_color="inverse")

    # Calculamos la diferencia para ver si hay Overfitting evidente
    diferencia_acc = fin_train_acc - fin_test_acc
    if diferencia_acc > 5.0:
        st.warning(f"⚠️ **Atención:** Existe una diferencia de {diferencia_acc:.2f}% entre la precisión de Train y Test. Esto puede ser un indicador de **Overfitting** (El modelo está memorizando en lugar de aprendiendo). Prueba a aumentar el tamaño de mezcla (Shuffle) o reducir las épocas.")
    elif fin_test_acc > 95.0:
        st.balloons()
        st.info(f"💡 **Excelente Rendimiento:** El modelo generaliza de forma sobresaliente. Has superado el 95% de acierto en los datos de prueba.")