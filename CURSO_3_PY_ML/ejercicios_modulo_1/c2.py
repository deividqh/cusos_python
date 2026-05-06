import os
import sys # Importante para saber qué Python estamos usando

archivo_entrada = "primer_archivo.ipynb"
archivo_salida = "primer_archivo.html"

# Usamos sys.executable para asegurar que use el Python de EAI_avanza
# Cambiamos 'jupyter nbconvert' por 'nbconvert' directamente
comando = f'"{sys.executable}" -m nbconvert --to html "{archivo_entrada}" --output "{archivo_salida}"'

print(f"Ejecutando: {comando}")

try: 
    # Usamos os.system pero ahora con la ruta absoluta del Python correcto
    resultado = os.system(comando)
    
    if resultado == 0:
        print(f"✅ Éxito: Archivo convertido a {archivo_salida}")
    else:
        print(f"❌ Error: El comando devolvió el código {resultado}")
        print("Asegúrate de que 'nbconvert' esté instalado en este entorno.")
    
except Exception as e:
    print(f"☢️ Error crítico: {e}")