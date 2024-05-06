package sockets;

import java.io.*; 
import java.text.*; 
import java.util.*; 
import java.net.*; 
import java.util.Scanner;


public class Cliente extends Conexion
{
    public Cliente() throws IOException{super("cliente");} //Se usa el constructor para cliente de Conexion

    public void startClient() //Método para iniciar el cliente
    {
        try
        {
            //Flujo de datos hacia el servidor
            salidaServidor = new DataOutputStream(cs.getOutputStream());

            //Se escribe en el servidor usando su flujo de datos
            while(true){
                Scanner myObj = new Scanner(System.in);
                System.out.println("Escriba su mensaje");
            
                String mensaje = myObj.nextLine();  // Read user input
                salidaServidor.writeUTF(mensaje);
                if(mensaje.equals("quit")){
                    cs.close();//Fin de la conexión
                    return;
                }
            }
        }
    catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
