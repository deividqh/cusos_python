import threading
import os
import tkinter as tk
# import socket

# -----------------------
from sobreSockets.clienteChat import ClienteChat as Ccli              # El cliente para enviar msg/File/emoji
from sobreSockets.infoSocket import infoSocket as InfoSck 
# -----------------------
from sobreForms.formServerAvz import FormularioServerAvanza       as FSer_A
from sobreForms.formClienteAvz import FormularioClienteChatAvanza as FCli_A

# =====================================================
# ---- Configuración de IP y Puertos
# ---- Tengo que cachar mi ip y el puerto es cte y elegido por mi.
# ---- Tengo que cachar la red local (192.168.0.[0-255]) y mostrar los equipos
# ---- De momento esto son constantes

# IP_ServidorPC1 = '192.168.1.10'
# IP_ServidorLocal = '127.0.0.1'
IP_ServidorLocal = 'localhost'
PORT_ServerLocal = 5000

# # IP_ServidorPC2 = '192.168.1.20'
# # IP_ServidorPC2 = '127.0.0.1'
# IP_ServidorPC2 = 'localhost'
PORT_ClientePC1 = 5001


def main():

    # ============= raiz para el SERVIDOR
    rootS = tk.Tk()
    rootS.title("Formulario Servidor de Chat")

    FServidor=FSer_A(root=rootS, title="Formulario Servidor", ancho=350, alto=300)
    # FServidor.OpenVentanaDownRight("Servidor Creado pero no mainloop aun")    
    
    # ========= raiz para el FormCLIENTE
    rootC = tk.Tk()
    rootC.title("Formulario Cliente de Chat")    
    FCliente=FCli_A(rootC, title="Formulario Cliente", ancho=250, alto=350, posY=100)

    # =================================    
    # Muestra el Formulario Cliente y servidor en hilos separados para que se ejecuten al mismo tiempo. 
    # Esto lo hago pq el Formulario Toma el Control al hacer mainloop y no puedo tener los dos a la vez.
    hiloServidor = threading.Thread(target=rootS.mainloop())
    hiloCliente  = threading.Thread(target=rootC.mainloop())

    # Esto puede no ponerse???
    hiloServidor.start()
    hiloCliente.start()

    # Esto puede no ponerse???
    hiloServidor.join()
    hiloCliente.join()

    # ____________________
    # Hasta que no se cierra el formulario no se ejecuta este código.
    # Y Cada ventana Toma el Control (Luego se ejecuta una después de la otra)
    # app.OpenVentanaUpRight("Que Pacha!!")
    # app.OpenVentanaDownRight("Que Que Pacha!!")
    print("The End Chat")
# ====================================================================



# Uso obtener ip
# ip_local, nombreHost = obtener_ip_local()
# print(f"Nombre host: {nombreHost} \nIP local :{ip_local}")
# ******************************

if __name__ == "__main__":
    # ---- Limpio la terminal 
    os.system('cls')    
    # ---- Empezamos!!
    main()
    
