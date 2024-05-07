package sockets.de.a.uno;

import java.io.*;
import java.net.*;

public class Servidor {
    public static void main(String[] args) throws IOException {
        ServerSocket servidorSocket = new ServerSocket(12345);
        System.out.println("Servidor esperando conexiones...");
        
        Socket clienteSocket = servidorSocket.accept();
        System.out.println("Cliente conectado: " + clienteSocket);
        
        BufferedReader entradaDesdeCliente = new BufferedReader(new InputStreamReader(clienteSocket.getInputStream()));
        PrintWriter salidaACliente = new PrintWriter(clienteSocket.getOutputStream(), true);
        
        BufferedReader entradaDesdeTeclado = new BufferedReader(new InputStreamReader(System.in));
        
        String mensajeDesdeCliente;
        String mensajeDesdeTeclado;
        
        while (true) {
            mensajeDesdeCliente = entradaDesdeCliente.readLine();
            if (mensajeDesdeCliente.equals("bye"))
                break;
            System.out.println("Cliente: " + mensajeDesdeCliente);
            
            System.out.print("Servidor: ");
            mensajeDesdeTeclado = entradaDesdeTeclado.readLine();
            salidaACliente.println(mensajeDesdeTeclado);
        }
        
        clienteSocket.close();
        servidorSocket.close();
    }
}

