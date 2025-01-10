package Multihilos.HilosExamen;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<CalculadorDivisores> hilos = new ArrayList<>();
        int i;

        // Procesar los argumentos de entrada
        for (i = 0; i < args.length; i++) {
            try {
                // Convertir argumento a entero
                int numero = (int) Math.floor(Double.parseDouble(args[i]));
                CalculadorDivisores hilo = new CalculadorDivisores(numero);
                hilos.add(hilo);
                hilo.start(); // Iniciar el hilo
            } catch (NumberFormatException e) {
                // Manejo de excepciones si el argumento no es un número válido
                System.out.println(args[i] + " -> " + e.getMessage());
            }
        }

        // Esperar a que todos los hilos terminen
        for (i = 0; i < hilos.size(); i++) {
            try {
                hilos.get(i).join();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        // Imprimir resultados
        for (i = 0; i < hilos.size(); i++) {
            CalculadorDivisores hilo = hilos.get(i);
            System.out.print(hilo.getNumero() + " -> ");
            List<Integer> divisores = hilo.getDivisores();

            for (int j = 0; j < divisores.size(); j++) {
                System.out.print(divisores.get(j));
                if (j < divisores.size() - 1) {
                    System.out.print(", ");
                }
            }
            System.out.println();
        }
    }
}
