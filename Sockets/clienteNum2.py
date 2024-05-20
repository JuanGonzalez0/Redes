import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    client_socket.connect((host, port))
    print("Ingrese quit para salir")
    num = input("Ingrese un número: ")
    client_socket.sendall(num.encode())  
    num2 = input("Ingrese un número: ")
    client_socket.sendall(num2.encode())

    while True:
        data = client_socket.recv(1024)
        response = data.decode('utf-8')
        print(f"Respuesta del server: {response}")
        message = input("Escriba su mensaje: ")
        if(message=="quit"):
            client_socket.close()
            return
        client_socket.sendall(message.encode('utf-8'))  # Solo enviar el mensaje
       

if __name__ == "__main__":
    main()