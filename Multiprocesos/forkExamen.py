import os

def crear_arbol():
    # Obtener el ID del proceso actual
    pid = os.getpid()
    # Obtener el ID del proceso padre
    ppid = os.getppid()
    
    # Crear el primer hijo
    pid_hijo = os.fork()
    
    if pid_hijo == 0:  # Proceso hijo
        print(f"Hijo: PID={pid}, PPID={ppid} (Soy hijo)")
        print(f"Proceso padre: PID={ppid} (Soy padre del hijo)")
    else:  # Proceso padre
        print(f"Padre: PID={pid}, PPID={ppid} (Soy el padre)")
        # Esperamos a que el hijo termine
        os.wait()

if __name__ == '__main__':
    crear_arbol()