package Multihilos.ArchivosJava__3;

import java.time.Instant;
import java.time.Duration;

public class Ejemplo_03 extends Thread{
    
    @Override
    public void run(){
        long MaxSecs = 5;
        Instant inicio = Instant.now();

        while (Duration.between(inicio, Instant.now()).getSeconds()<MaxSecs) {
            System.out.println("Todavía ejecuto");
            System.out.println("Estamos en el segundo: " + Duration.between(inicio, Instant.now()).getSeconds());
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("He terminado");
    }
    
    public static void main(String[] args) {
        Ejemplo_03 hiloTemporal = new Ejemplo_03();
        hiloTemporal.start();
        try {
            hiloTemporal.join();
        } catch (InterruptedException e) {
            e.printStackTrace();;
        }
    }    
}
