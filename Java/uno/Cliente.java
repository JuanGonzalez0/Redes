package sockets.de.a.uno;

import java.io.*;
import java.net.*;

public class Cliente {
    public static void main(String[] args) throws IOException {
        Socket clienteSocket = new Socket("localhost", 12345);
        
        BufferedReader entradaDesdeServidor = new BufferedReader(new InputStreamReader(clienteSocket.getInputStream()));
        PrintWriter salidaAServidor = new PrintWriter(clienteSocket.getOutputStream(), true);
        
        BufferedReader entradaDesdeTeclado = new BufferedReader(new InputStreamReader(System.in));
        
        String mensajeDesdeServidor;
        String mensajeDesdeTeclado;
        
        while (true) {
            System.out.print("Cliente: ");
            mensajeDesdeTeclado = entradaDesdeTeclado.readLine();
            salidaAServidor.println(mensajeDesdeTeclado);
            if (mensajeDesdeTeclado.equals("bye"))
                break;
            
            mensajeDesdeServidor = entradaDesdeServidor.readLine();
            System.out.println("Servidor: " + mensajeDesdeServidor);
        }
        
        clienteSocket.close();
    }
}
