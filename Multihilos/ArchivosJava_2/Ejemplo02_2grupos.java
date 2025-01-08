package Multihilos.ArchivosJava_2;

import javax.management.RuntimeErrorException;

public class Ejemplo02_2grupos extends Thread{
    @Override
    public void run(){
        System.out.println("Información del hilo: "+ Thread.currentThread());
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        System.out.println(Thread.currentThread().getName()+"Finalizando la ejecución");
    }
    public static void main(String[] args) {
        Thread.currentThread().setName("Principal");
        System.out.println(Thread.currentThread().getName());
        System.out.println(Thread.currentThread());

        ThreadGroup grupo = new ThreadGroup("Grupo de hilos");
        Ejemplo02_2grupos h = new Ejemplo02_2grupos();
        Thread h1 = new Thread(grupo, h, "Hilo 1");
        Thread h2 = new Thread(grupo, h, "Hilo 2");
        Thread h3 = new Thread(grupo, h, "Hilo 3");
        h1.start();
        h2.start();
        h3.start();
        System.out.println("Tres hilos creados...");
        System.out.println("hilos activos:" + Thread.activeCount());
    }  
}
