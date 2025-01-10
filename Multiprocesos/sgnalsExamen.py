import os
import signal
import time

# Variable global para almacenar el estado del cálculo
numero = 0
corriendo = False

def manejador_inicio(signum, frame):
    """Manejador para la señal de INICIO"""
    global corriendo
    corriendo = True

def manejador_para(signum, frame):
    """Manejador para la señal de PARA"""
    global corriendo
    corriendo = False

def manejador_muere(signum, frame):
    """Manejador para la señal de MUERE"""
    print("Terminando proceso...")
    os._exit(0)

def proceso_calculador():
    """Proceso que calcula múltiplos de 3"""
    global numero, corriendo

    # Asociar las señales a sus manejadores
    signal.signal(signal.SIGUSR1, manejador_inicio)  # INICIO
    signal.signal(signal.SIGUSR2, manejador_para)    # PARA
    signal.signal(signal.SIGTERM, manejador_muere)   # MUERE

    print(f"Proceso calculador iniciado. PID: {os.getpid()}")
    while True:
        if corriendo:
            print(f"Múltiplo de 3: {numero}")
            numero += 3
        time.sleep(1)

def proceso_controlador(pid_calculador):
    """Proceso que controla al calculador"""
    print(f"Proceso controlador iniciado. PID: {os.getpid()}")
    print("Comandos disponibles:")
    print("INICIO -> Reanudar cálculo")
    print("PARA -> Pausar cálculo")
    print("MUERE -> Terminar procesos")

    while True:
        comando = input("Introduce comando (INICIO, PARA, MUERE): ").strip().upper()
        if comando == "INICIO":
            os.kill(pid_calculador, signal.SIGUSR1)
        elif comando == "PARA":
            os.kill(pid_calculador, signal.SIGUSR2)
        elif comando == "MUERE":
            os.kill(pid_calculador, signal.SIGTERM)
            os._exit(0)
        else:
            print("Comando no reconocido. Intenta nuevamente.")

if __name__ == '__main__':
    # Crear proceso hijo para el cálculo
    pid_hijo = os.fork()

    if pid_hijo == 0:
        # Proceso hijo: calculador
        proceso_calculador()
    else:
        # Proceso padre: controlador
        proceso_controlador(pid_hijo)
