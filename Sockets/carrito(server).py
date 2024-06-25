from mailbox import NoSuchMailboxError
import socket
import threading

# Función para manejar la conexión con un cliente
def handle_client(client_socket):
    global productos
    while True:
        # Recibimos los datos del cliente
        data = client_socket.recv(1024)
        if not data:
            break
        
        lock.acquire()
        for p in productos:
           print(p.toString()) 
           client_socket.send(str(p.toString()).encode("utf-8"))

        # Liberamos el candado después de modificar el acumulador
        lock.release()
        # Convertimos los datos a un número entero
        try:
            numero = int(data.decode("utf-8"))
        except ValueError:
            print("Error: El dato recibido no es un número.")
            continue
        
        # Adquirimos el candado antes de modificar el acumulador
        lock.acquire()

        # Liberamos el candado después de modificar el acumulador
        lock.release()
        
        # Enviamos al cliente la suma acumulada
        client_socket.send(str(acumulador).encode("utf-8"))
    
    # Cerramos la conexión con el cliente
    client_socket.close()

def main():
    global acumulador
    # Creamos un socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Definimos la dirección y el puerto en el que escuchar
    server_address = ('localhost', 9999)
    
    # Ligamos el socket al puerto
    server_socket.bind(server_address)
    
    # Escuchamos conexiones entrantes (máximo 5 clientes en espera)
    server_socket.listen(5)
    
    print("Servidor escuchando en {} puerto {}".format(*server_address))
    
    # Inicializamos el acumulador
    productos = Producto[3]
    productos.push(Producto("Pepis", 20, 10.5))
    productos.push(Producto("Papitas Leis", 50, 50.5))
    productos.push(Producto("Juanma", 5, 1000.5))

    try:
        while True:
            # Aceptamos la conexión del cliente
            client_socket, client_address = server_socket.accept()
            print("Conexión aceptada desde:", client_address)
            
            # Creamos un hilo para manejar al cliente
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
    finally:
        # Cerramos el socket del servidor cuando terminamos
        server_socket.close()

if __name__ == "__main__":
    # Creamos un candado para garantizar la exclusión mutua
    lock = threading.Lock()
    main()

class Producto:

    nombre = str
    cantidad = int
    precio = float

    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def getPrecio(self):
        self.precio = self.precio * self.cantidad
    
    def toString(self):
        return ("Producto: ", self.nombre, ", cantidad: ", self.cantidad, ", precio: ", self.precio)