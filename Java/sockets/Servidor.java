package sockets;


import java.io.*; 
import java.text.*; 
import java.util.*; 
import java.net.*; 


public class Servidor extends Conexion {
    public Servidor() throws IOException {
        super("servidor");
    }

    public void startServer() {
        try {
            System.out.println("Esperando..."); 

            cs = ss.accept(); 
            System.out.println("Cliente en línea");

            salidaCliente = new DataOutputStream(cs.getOutputStream());
            salidaCliente.writeUTF("Petición recibida y aceptada");

            DataInputStream entrada = new DataInputStream(cs.getInputStream());

            while (true) {
                // Se lee el mensaje del cliente
                String mensajeServidor = entrada.readUTF();
                // Se muestra por pantalla el mensaje recibido
                System.out.println("Cliente: " + mensajeServidor);
            }

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}

