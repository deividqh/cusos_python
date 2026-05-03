import socket

def start_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('127.0.0.1', 5000))
        server_socket.listen(1)
        print("Servidor escuchando...")
        # --------------------
        conn, addr = server_socket.accept()
        print(f"Conectado a {addr}")
        
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    print("Conexión cerrada por el cliente")
                    break
                print(f"Cliente: {data}")
                conn.send("Mensaje recibido".encode())
            except ConnectionResetError:
                print("El cliente cerró inesperadamente la conexión.")
                break
            except socket.error as e:
                print(f"Error de socket: {e}")
                break

    except socket.error as e:
        print(f"Error al crear el socket: {e}")
    
    finally:
        if conn:
            conn.close()
        server_socket.close()





start_server()

