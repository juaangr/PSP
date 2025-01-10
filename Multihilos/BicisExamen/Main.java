public class Main {
    public static void main(String[] args) {
        int cantidadBicicletas = 5; // Número de bicicletas en el sistema
        SistemaPrestamo sistemaPrestamo = new SistemaPrestamo(cantidadBicicletas);

        // Crear y ejecutar usuarios
        Usuario[] usuarios = new Usuario[10]; // 10 usuarios
        for (int i = 0; i < usuarios.length; i++) {
            usuarios[i] = new Usuario(i + 1, sistemaPrestamo);
            usuarios[i].start();
        }

        // Esperar a que todos los usuarios terminen
        for (Usuario usuario : usuarios) {
            try {
                usuario.join();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        System.out.println("Sistema de préstamo finalizado.");
    }
}
