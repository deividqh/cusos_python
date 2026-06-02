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
    """Descarga, normaliza y divide el dataset MNIST."""
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    
    # Normalización
    x_train, x_test = x_train / 255.0, x_test / 255.0
    x_train = x_train[..., tf.newaxis].astype("float32")
    x_test = x_test[..., tf.newaxis].astype("float32")
    
    # DIVISIÓN CLAVE:
    # De los 10,000 datos de test, dejamos 9000 para validar en cada época
    # y reservamos los últimos 1000 estrictamente para el motor de predicciones finales.
    x_val, y_val = x_test[:-1000], y_test[:-1000]
    x_pred, y_pred = x_test[-1000:], y_test[-1000:]
    
    return x_train, y_train, x_val, y_val, x_pred, y_pred

x_train, y_train, x_val, y_val, x_pred, y_pred = cargar_datos()

# Inicializamos la memoria de Streamlit para no perder el modelo entrenado
if 'modelo_entrenado' not in st.session_state:
    st.session_state.modelo_entrenado = None
    st.session_state.metricas_finales = None


# ■■■■■ 2. ENUNCIADO EN COLLAPSE (CON VISOR DINÁMICO) ■■■■■
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
        st.info(f"**Set de Entrenamiento (Train):**\n\nImágenes: {x_train.shape}\nEtiquetas: {y_train.shape}")
        st.info(f"**Set de Validación (Test interno):**\n\nImágenes: {x_val.shape}\nEtiquetas: {y_val.shape}")
    
    with col_info2:
        st.warning(f"**Set de Reserva (Para Predicciones):**\n\nImágenes: {x_pred.shape}\nEtiquetas: {y_pred.shape}\n\n*Estos 1000 datos están completamente aislados del entrenamiento.*")
    
    with col_img:
        st.markdown("**Visor del Set de Reserva:**")
        # Selector dinámico de muestra
        idx_visor = st.number_input("Selecciona un índice (0 - 999):", min_value=0, max_value=len(x_pred)-1, value=0)
        imagen_mostrar = x_pred[idx_visor].numpy() if hasattr(x_pred[idx_visor], 'numpy') else x_pred[idx_visor]
        st.image(imagen_mostrar, width=120, caption=f"Etiqueta real: {y_pred[idx_visor]}")


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
        st.write("") # Espaciador
        iniciar_entrenamiento = st.button("🚀 Iniciar Entrenamiento", type="primary", width='stretch')


# ■■■■■ 4. PROCESAMIENTO DE DATOS Y MODELADO ■■■■■
if iniciar_entrenamiento:
    
    train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(SHUFFLE_SIZE).batch(BATCH_SIZE)
    val_ds = tf.data.Dataset.from_tensor_slices((x_val, y_val)).batch(BATCH_SIZE)

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

    train_loss = tf.keras.metrics.Mean(name='train_loss')
    train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='train_accuracy')
    val_loss = tf.keras.metrics.Mean(name='test_loss')
    val_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='test_accuracy')

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
        val_loss(t_loss)
        val_accuracy(labels, predictions)

    st.markdown("---")
    st.markdown("### 📉 Entrenamiento Dinámico del Modelo")
    
    txt_estado = st.empty()
    barra_progreso = st.progress(0.0)
    
    col_grafico1, col_grafico2 = st.columns(2)
    grafico_perdida = col_grafico1.empty()
    grafico_precision = col_grafico2.empty()

    hist_epochs = []
    hist_train_loss, hist_val_loss = [], []
    hist_train_acc, hist_val_acc = [], []

    for epoch in range(EPOCHS):
        txt_estado.info(f"⏳ **Procesando Época {epoch + 1} de {EPOCHS}...** Por favor, espera.")
        
        train_loss.reset_state()
        train_accuracy.reset_state()
        val_loss.reset_state()
        val_accuracy.reset_state()

        for images, labels in train_ds:
            train_step(images, labels)

        for val_images, val_labels in val_ds:
            test_step(val_images, val_labels)

        hist_epochs.append(epoch + 1)
        hist_train_loss.append(train_loss.result().numpy())
        hist_val_loss.append(val_loss.result().numpy())
        hist_train_acc.append(train_accuracy.result().numpy() * 100)
        hist_val_acc.append(val_accuracy.result().numpy() * 100)

        fig_loss = go.Figure()
        fig_loss.add_trace(go.Scatter(x=hist_epochs, y=hist_train_loss, mode='lines+markers', name='Train Loss', line=dict(color='#1f77b4', width=3)))
        fig_loss.add_trace(go.Scatter(x=hist_epochs, y=hist_val_loss, mode='lines+markers', name='Val Loss', line=dict(color='#ff7f0e', width=3)))
        fig_loss.update_layout(title='Evolución de la Pérdida (Log Loss)', xaxis_title='Época', yaxis_title='Loss', template='plotly_white', margin=dict(t=40, b=0))
        grafico_perdida.plotly_chart(fig_loss, width='stretch')

        fig_acc = go.Figure()
        fig_acc.add_trace(go.Scatter(x=hist_epochs, y=hist_train_acc, mode='lines+markers', name='Train Accuracy', line=dict(color='#2ca02c', width=3)))
        fig_acc.add_trace(go.Scatter(x=hist_epochs, y=hist_val_acc, mode='lines+markers', name='Val Accuracy', line=dict(color='#d62728', width=3)))
        fig_acc.update_layout(title='Evolución de la Exactitud (Accuracy %)', xaxis_title='Época', yaxis_title='Precisión (%)', template='plotly_white', margin=dict(t=40, b=0))
        grafico_precision.plotly_chart(fig_acc, width='stretch')

        barra_progreso.progress((epoch + 1) / EPOCHS)

    txt_estado.success("✅ ¡Entrenamiento completado exitosamente!")
    
    # GUARDAR EL MODELO Y LAS MÉTRICAS EN MEMORIA
    st.session_state.modelo_entrenado = model
    st.session_state.metricas_finales = {
        'fin_train_acc': hist_train_acc[-1],
        'fin_val_acc': hist_val_acc[-1],
        'fin_train_loss': hist_train_loss[-1],
        'fin_val_loss': hist_val_loss[-1]
    }


# ■■■■■ 5. PANEL INFERIOR (MÉTRICAS Y PREDICCIÓN INTERACTIVA) ■■■■■
# Solo se muestra si el modelo está guardado en la memoria (session_state)
if st.session_state.modelo_entrenado is not None:
    
    st.markdown("---")
    st.markdown("### 📊 Métricas Finales de Rendimiento")

    mf = st.session_state.metricas_finales
    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Precisión Final (Training)", f"{mf['fin_train_acc']:.2f} %", delta="Datos conocidos")
    m2.metric("Precisión Final (Validación)", f"{mf['fin_val_acc']:.2f} %", delta="Datos invisibles")
    m3.metric("Pérdida Final (Train Loss)", f"{mf['fin_train_loss']:.4f}", delta="Menor entropía es mejor", delta_color="inverse")
    m4.metric("Pérdida Final (Val Loss)", f"{mf['fin_val_loss']:.4f}", delta="Menor entropía es mejor", delta_color="inverse")

    st.markdown("---")
    
    # ■■■■■ MOTOR DE PREDICCIÓN ■■■■■
    st.markdown("### 🔮 Motor de Predicción Interactivo")
    st.write("Usa el modelo ya entrenado para clasificar imágenes del **set de reserva** (1000 datos que la red no ha tocado ni para entrenar ni para validar).")
    
    # Widget numérico para seleccionar qué imagen predecir
    idx_pred = st.slider("Selecciona el índice de la imagen de reserva a predecir:", 0, len(x_pred)-1, 0)
    
    col_img_pred, col_resultados, col_graf_prob = st.columns([1, 1.5, 2])
    
    # Obtener el tensor y la etiqueta
    img_tensor = x_pred[idx_pred]
    label_real = y_pred[idx_pred]
    
    with col_img_pred:
        imagen_mostrar_pred = img_tensor.numpy() if hasattr(img_tensor, 'numpy') else img_tensor
        st.image(imagen_mostrar_pred, width=150, caption=f"Imagen Real (Dígito: {label_real})")
        
    with col_resultados:
        # Preparamos la imagen para la red (añadimos la dimensión de "lote/batch")
        img_batch = tf.expand_dims(img_tensor, 0) 
        
        # Inferencia con el modelo guardado
        logits_pred = st.session_state.modelo_entrenado(img_batch, training=False)
        
        # Convertimos los logits brutos a probabilidades (Porcentajes)
        probabilidades = tf.nn.softmax(logits_pred).numpy()[0]
        clase_predicha = np.argmax(probabilidades)
        confianza = probabilidades[clase_predicha] * 100
        
        # Resultados visuales
        if clase_predicha == label_real:
            st.success(f"### ✅ Predicción: {clase_predicha}")
            st.write("¡El modelo ha acertado!")
        else:
            st.error(f"### ❌ Predicción: {clase_predicha}")
            st.write(f"El modelo ha fallado. El número real era **{label_real}**.")
            
        st.metric("Confianza del modelo", f"{confianza:.2f}%")
        
    with col_graf_prob:
        # Gráfico de barras interactivo con la confianza para los 10 dígitos
        clases_x = [str(i) for i in range(10)]
        fig_probs = go.Figure(data=[go.Bar(
            x=clases_x, 
            y=probabilidades,
            marker_color=['#2ca02c' if i == clase_predicha else '#1f77b4' for i in range(10)]
        )])
        fig_probs.update_layout(
            title="Distribución de Probabilidades (Softmax)", 
            xaxis_title="Dígitos Posibles", 
            yaxis_title="Probabilidad", 
            template="plotly_white", 
            margin=dict(t=40, b=0, l=0, r=0)
        )
        st.plotly_chart(fig_probs, width='stretch')