import socket

def main():
    # Creamos un socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Definimos la dirección y el puerto del servidor al que nos conectaremos
    server_address = ('localhost', 9999)
    
    try:
        # Nos conectamos al servidor
        client_socket.connect(server_address)
        
        while True:
            # Solicitamos al usuario ingresar un número
            numero = input("Ingrese un número (o 'q' para salir): ")
            
            # Si el usuario ingresa 'q', salimos del bucle
            if numero.lower() == 'q':
                break
            
            try:
                # Convertimos el número a un entero
                numero_entero = int(numero)
                
                # Enviamos el número al servidor
                client_socket.send(str(numero_entero).encode("utf-8"))
                
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
    finally:
        # Cerramos la conexión con el servidor
        client_socket.close()

if __name__ == "__main__":
    main()
