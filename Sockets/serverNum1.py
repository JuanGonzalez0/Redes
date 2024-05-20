import socket
import threading # para poder manejar mas de un cliente a la vez

def handle_client(client_socket):
    numero = 27
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = int(data.decode())
        if(numero > message):
            response = (f"El número del server es mayor ({numero})")
        else:
            response = (f"El númmero del cliente es mayor ({message})")
        client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #establecer que tipo de ip se usa y el protocolo
    host = '127.0.0.1'
    port = 12345
    server_socket.bind((host, port)) #asocia la ip y el puerto
    server_socket.listen(5) #el server espera solicitudes
    print(f"Server Prendido {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexion desde: {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
