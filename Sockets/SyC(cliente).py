import socket

def main():
    host = '127.0.0.1'  # Dirección IP del servidor
    port = 12345        # Puerto al que se conectará el cliente

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))  # Conexión al servidor
        print("Conectado al servidor.")

        while True:
            # El cliente envía un mensaje al servidor
            message_to_server = input("Mensaje para el servidor: ")
            client_socket.sendall(message_to_server.encode())

            # El cliente espera la respuesta del servidor
            server_response = client_socket.recv(1024).decode()
            print("Respuesta del servidor:", server_response)

            # Salir del bucle si el cliente recibe la respuesta "bye" del servidor
            if server_response.lower() == "bye":
                break

if __name__ == "__main__":
    main()
