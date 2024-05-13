import socket

def main():
    host = '127.0.0.1'  # Dirección IP del servidor
    port = 12345        # Puerto en el que el servidor estará escuchando

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))  # Enlazar el socket al host y al puerto
        server_socket.listen()             # Escuchar conexiones entrantes
        print("El servidor está esperando conexiones...")

        conn, addr = server_socket.accept()  # Aceptar la conexión entrante
        with conn:
            print("Conectado con", addr)

            while True:
                # El servidor espera el mensaje del cliente
                client_message = conn.recv(1024).decode()
                print("Mensaje del cliente:", client_message)

                # Si el mensaje del cliente es "bye", el servidor responde y cierra la conexión
                if client_message.lower() == "bye":
                    conn.sendall("Adiós, cliente.".encode())
                    break

                # El servidor envía un mensaje al cliente
                message_to_client = input("Mensaje para el cliente: ")
                conn.sendall(message_to_client.encode())

if __name__ == "__main__":
    main()

