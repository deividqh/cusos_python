import socket

def start_client():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            except BrokenPipeError:
                print("Error: El servidor cerró la conexión.")
                break
            except socket.timeout:
                print("Error: Tiempo de espera agotado.")
            except socket.error as e:
                print(f"Error de socket: {e}")
                break

    except ConnectionRefusedError:
        print("Error: No se pudo conectar al servidor.")
    except socket.error as e:
        print(f"Error en la conexión: {e}")
    
    finally:
        client_socket.close()

start_client()
