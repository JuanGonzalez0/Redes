import socket
import os

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    client_socket.connect((host, port))

    edad = input("Ingrese su edad: ")
    client_socket.sendall(edad.encode())

    respServ = client_socket.recv(1024).decode() #recibe el nombre del cliente
    print(f"{respServ}") 


if __name__ == "__main__":
    main()

os.system("pause")