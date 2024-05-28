import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    client_socket.connect((host, port))

    name = input("Ingrese su nombre: ")
    client_socket.sendall(name.encode('utf-8'))  # Enviar el nombre al servidor

    while True:
        message = input("Escriba su mensaje: ")
        client_socket.sendall(message.encode('utf-8'))  # Solo enviar el mensaje
        data = client_socket.recv(1024)
        response = data.decode('utf-8')
        print(f"Respuesta del server: {response}")

if __name__ == "__main__":
    main()
