package Multihilos.ArchivosJava_2;

//aqui ya estamos extendiendo de los hilos...
//a partir de aqui, "Ejemplo02_2"
public class Ejemplo02_2 extends Thread{
    @Override        
    public void run(){
        System.out.println(
            "Dentro del hilo: " + Thread.currentThread().getName()
            +"\n\tPrioridad: "+Thread.currentThread().getPriority()
            +"\n\tID: "+Thread.currentThread().threadId()
            +"\n\tHilos activos: "+Thread.activeCount()
        );
    }

    public static void main(String[] args) {
        Thread.currentThread().setName("Principal");
        System.out.println(Thread.currentThread().getName());
        System.out.println(Thread.currentThread());
        
        Ejemplo02_2 h =  null; // setteamos el hilo en nulo
        for (int i=0; i<3 ;i++){  // con este for recorremos el hilo
            h = new Ejemplo02_2(); // Crear hilo
            h.setName(" HILO" + i); // damos nombre
            h.setPriority(i +1); // damos prioridad
            h.start(); // iniciar hilo

            System.out.println(
                "información del"+ h.getName()+ ": "+h.toString()
            );
        }
        System.out.println("3 Hilos creados...");
        System.out.println("Hilos activos: " + Thread.activeCount());
    }
}