import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Bicicleta {
    private int idBici;
    private int bateria; // Máximo de 100 minutos
    private Lock lock;

    public Bicicleta(int idBici) {
        this.idBici = idBici;
        this.bateria = 100;
        this.lock = new ReentrantLock();
    }

    public boolean usarBicicleta(int tiempo) {
        lock.lock();
        try {
            if (bateria >= tiempo) {
                bateria -= tiempo;
                return true;
            }
            return false;
        } finally {
            lock.unlock();
        }
    }

    public boolean estaDisponible() {
        lock.lock();
        try {
            return bateria > 0;
        } finally {
            lock.unlock();
        }
    }

    public int getIdBici() {
        return idBici;
    }
}
