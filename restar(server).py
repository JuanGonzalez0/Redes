import socket
import threading

clients = []
values = [100, 100]

def handle_client(client_socket, client_id):
    global values
    while True:
        try:
            # Recibir datos del cliente
            data = client_socket.recv(1024).decode()
            if not data:
                break
            
            value = int(data)
            # Restar el valor de la variable del otro cliente
            other_client_id = 1 - client_id
            values[other_client_id] -= value

            # Verificar si la variable del otro cliente ha llegado a 0
            if values[other_client_id] <= 0:
                clients[other_client_id].send("0".encode())
                clients[other_client_id].close()
                break

            # Enviar la actualización al otro cliente
            clients[other_client_id].send(f"{values[other_client_id]}".encode())
        except:
            break

    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(2)
    print("Servidor escuchando en el puerto 9999...")

    for i in range(2):
        client_socket, addr = server.accept()
        print(f"Cliente {i+1} conectado desde {addr}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, i))
        client_thread.start()

if __name__ == "__main__":
    main()
