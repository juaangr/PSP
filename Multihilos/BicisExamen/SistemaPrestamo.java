import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class SistemaPrestamo {
    private List<Bicicleta> bicicletas;
    private Lock lock;

    public SistemaPrestamo(int cantidadBicicletas) {
        this.bicicletas = new ArrayList<>();
        this.lock = new ReentrantLock();
        for (int i = 1; i <= cantidadBicicletas; i++) {
            bicicletas.add(new Bicicleta(i));
        }
    }

    public Bicicleta obtenerBicicleta() {
        lock.lock();
        try {
            for (Bicicleta bicicleta : bicicletas) {
                if (bicicleta.estaDisponible()) {
                    bicicletas.remove(bicicleta);
                    return bicicleta;
                }
            }
            return null;
        } finally {
            lock.unlock();
        }
    }

    public void devolverBicicleta(Bicicleta bicicleta) {
        lock.lock();
        try {
            bicicletas.add(bicicleta);
        } finally {
            lock.unlock();
        }
    }
}
