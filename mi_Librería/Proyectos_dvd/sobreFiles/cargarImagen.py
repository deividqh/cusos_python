""" Librería para visualizar imagenes facilmente """
# pip install pillow

"""  """
from PIL import Image
import io

# Abrir el archivo de imagen en modo binario
with open("imagen.jpg", "rb") as archivo_binario:
    datos_binarios = archivo_binario.read()

# Convertir los datos binarios en un objeto BytesIO para Pillow
imagen_bytes = io.BytesIO(datos_binarios)

# Cargar la imagen con PIL
imagen = Image.open(imagen_bytes)

# Mostrar la imagen
imagen.show()
""" 
Leer el Archivo Binario: 
    Abrimos el archivo .jpg en modo binario ("rb") y leemos todos los datos en datos_binarios.

Convertir a BytesIO: 
    Usamos io.BytesIO() para crear un flujo de bytes desde datos_binarios. 
    Esto permite que Pillow lo trate como una imagen, aunque no provenga directamente de un archivo.

Cargar y Mostrar la Imagen: 
    Image.open(imagen_bytes) convierte los bytes en un objeto de imagen y permite usar imagen.show() 
    para abrir la imagen en la aplicación predeterminada de visualización de imágenes de tu sistema operativo.
 """