package Multihilos.HilosExamen;

import java.util.ArrayList;
import java.util.List;

public class CalculadorDivisores extends Thread {
    private int numero;
    private List<Integer> divisores;

    public CalculadorDivisores(int numero) {
        this.numero = numero;
        this.divisores = new ArrayList<>();
    }

    @Override
    public void run() {
        for (int i = 1; i <= numero; i++) {
            if (numero % i == 0) {
                divisores.add(i);
            }
        }
    }

    public int getNumero() {
        return numero;
    }

    public List<Integer> getDivisores() {
        return divisores;
    }
}
