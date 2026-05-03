# Configurar el archivo launch.json en Visual Studio Code (VSCode) para Python. 
# ----------------------------------------------------------------------------
""" 
    El archivo launch.json contiene configuraciones para depurar aplicaciones
    en diferentes lenguajes de programación.

1.	Abre tu proyecto Python en Visual Studio Code.
2.	Presiona Ctrl + Shift + P para abrir el panel de comandos.
3.	Escribe Debug: Open launch.json y selecciona la opción o simplemente selecciona el ícono de engranaje 
    en el panel lateral de depuración (o presiona Ctrl + Shift + D).
4.	Selecciona "Python" en la lista desplegable que aparece.
5.	VSCode mostrará un archivo launch.json predeterminado. 
    Aquí puedes crear diferentes configuraciones de depuración. 
    Aquí hay un ejemplo básico de archivo launch.json para Python:

 """
 # .... en launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Archivo actual",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}

# Explicación de la configuración predeterminada:
# -------------------------------------------------
# •	"name": Nombre descriptivo para la configuración.
# •	"type": Especifica el tipo de depuración. En este caso, establecémoslo en python.
# •	"request": Debe ser launch para iniciar una nueva sesión de depuración.
# •	"program":  Indica al programa que se está ejecutando. 
#                 Usa la variable predeterminada ${file}, lo que significa que se depurará el archivo actual.
# •	"console": Especifica donde desea ver la salida. Puede ser:
#                  integratedTerminal (consola integrada) 
#                  externalTerminal (consola externa).
# •	"justMyCode":   Al establecerlo en true, se omite el código de las bibliotecas y solo se centra 
#                     en el código en el archivo que se está depurando.

""" 
Puedes personalizar esta configuración según tus necesidades.
Una vez que hayas configurado el archivo launch.json, puedes iniciar la depuración presionando F5 
o seleccionando "Iniciar Depuración" desde el menú "Depurar".

 """
# Algunas opciones para type, request y console en el archivo launch.json de Visual Studio Code:
# -----------------------------------------------------------------------------------------------
# type:
""" El atributo "type" especifica el tipo de depuración que se usará. Algunos valores comunes para type incluyen:
    python: Depuración de scripts Python usando el módulo ptvsd.
    module: Depuración de módulos Python importados en un script.
    console: Inicie una sesión interactiva Python (REPL) en la terminal integrada.
    jupyter: Iniciar una sesión interactiva Jupyter Notebook.
    pyunit: Corra pruebas unitarias enmarcadas en Python (como unittest o pytest). """
# request:
""" El atributo "request" especifica el tipo de operación de depuración que se iniciará. Algunos valores comunes para request incluyen:
launch: Iniciar una nueva sesión de depuración.
attach: Adjuntar al depurador a un proceso ya en ejecución. """
# console:
""" El atributo "console" especifica dónde se mostrará la salida de la consola durante la depuración. Algunos valores comunes para console incluyen:
internalConsole: Muestra la salida en la consola integrada de VS Code.
integratedTerminal: Muestra la salida en la terminal integrada de VS Code.
externalTerminal: Abre una terminal externa para mostrar la salida.
 """
# Puedes encontrar más información sobre las diferentes opciones para estos atributos en la documentación
#  de depuración de Python de Visual Studio Code aquí: https://code.visualstudio.com/docs/python/debugging.