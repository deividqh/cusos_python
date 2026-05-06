import os
import sys # Importante para saber qué Python estamos usando
archivo_entrada = "primer_archivo.ipynb"
archivo_salida = "primer_archivo.html"

# comando = f"python -m jupyter nbconvert --to html {archivo_entrada} --output {archivo_salida}"
comando = f'"{sys.executable} " -m nbconvert --to html "{archivo_entrada}" --output "{archivo_salida}"'

print (f"{comando}")
try: 
    # resultado = os.system(comando)
    resultado = sys.executable(comando)
    if(resultado == 0):
        print(f"Archivo convertido {archivo_salida}")
    else:
        print(f"Error al convertir el archivo: {archivo_entrada}")
    
except Exception as e:
    print(f"Error al convertir el archivo: {e}")


