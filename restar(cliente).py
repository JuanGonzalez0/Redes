import socket
import threading

def listen_for_updates(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            print(f"Valor restante del otro cliente: {data}")
            if data == "0":
                print("¡El otro cliente ha perdido!")
                break
        except:
            break

    client_socket.close()

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 9999))

    listen_thread = threading.Thread(target=listen_for_updates, args=(client_socket,))
    listen_thread.start()

    while True:
        try:
            value = input("Introduce un valor a restar: ")
            client_socket.send(value.encode())
        except:
            break

    client_socket.close()

if __name__ == "__main__":
    main()
