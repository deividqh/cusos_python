import socket
import time

MAX_RECONNECTIONS = 5       # Máximo número de intentos de reconexión
RETRY_DELAY = 3             # Tiempo de espera entre intentos de reconexión (segundos)
TIMEOUT = 5                 # Tiempo de espera para recibir datos (segundos)

def start_client():
    reconnections = 0

    while reconnections < MAX_RECONNECTIONS:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(TIMEOUT)
            client_socket.connect(('127.0.0.1', 5000))
            print("Conectado al servidor")
            
            while True:
                message = input("Cliente: ")
                if not message:
                    print("No se puede enviar un mensaje vacío.")
                    continue
                
                try:
                    client_socket.send(message.encode())
                    response = client_socket.recv(1024).decode()
                    print(f"Servidor: {response}")
                except socket.timeout:
                    print("Tiempo de espera agotado. No se recibió respuesta a tiempo.")
                except BrokenPipeError:
                    print("Error: El servidor cerró la conexión.")
                    break

        except ConnectionRefusedError:
            reconnections += 1
            print(f"Conexión rechazada. Intentando reconectar... ({reconnections}/{MAX_RECONNECTIONS})")
            time.sleep(RETRY_DELAY)  # Espera antes de intentar reconectar
        except socket.error as e:
            print(f"Error de socket: {e}")
            break
        else:
            # Si la conexión se logra, salimos del bucle
            break
        finally:
            client_socket.close()

    if reconnections == MAX_RECONNECTIONS:
        print("No se pudo conectar después de varios intentos. Verifica que el servidor esté en línea.")


start_client()

