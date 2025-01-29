import java.util.Random;

public class Usuario extends Thread {
    private int idUsuario;
    private SistemaPrestamo sistemaPrestamo;
    private int intentos;

    public Usuario(int idUsuario, SistemaPrestamo sistemaPrestamo) {
        this.idUsuario = idUsuario;
        this.sistemaPrestamo = sistemaPrestamo;
        this.intentos = 20; // Número máximo de intentos para encontrar una bicicleta
    }

    @Override
    public void run() {
        System.out.println("Usuario " + idUsuario + " buscando una bicicleta...");
        Random random = new Random();

        while (intentos > 0) {
            Bicicleta bicicleta = sistemaPrestamo.obtenerBicicleta();
            if (bicicleta != null) {
                int tiempoUso = 5 + random.nextInt(16); // Tiempo aleatorio entre 5 y 20 minutos
                System.out.println("Usuario " + idUsuario + " usando la bicicleta " + bicicleta.getIdBici() +
                                   " durante " + tiempoUso + " minutos.");
                if (bicicleta.usarBicicleta(tiempoUso)) {
                    try {
                        Thread.sleep(tiempoUso * 1000L); // Simular el uso (1 segundo = 1 minuto)
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                    System.out.println("Usuario " + idUsuario + " terminó su trayecto.");
                } else {
                    System.out.println("Usuario " + idUsuario + " encontró la bicicleta " + bicicleta.getIdBici() +
                                       " sin suficiente batería.");
                }
                sistemaPrestamo.devolverBicicleta(bicicleta);
                return;
            } else {
                System.out.println("Usuario " + idUsuario + " no encontró bicicleta disponible. Reintentando...");
                intentos--;
                try {
                    Thread.sleep(500); // Medio minuto simulado
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        }
        System.out.println("Usuario " + idUsuario + " no pudo encontrar una bicicleta tras 20 intentos y abandona.");
    }
}

