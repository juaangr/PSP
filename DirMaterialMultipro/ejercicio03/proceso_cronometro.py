import time
import signal

inicio = None
final = None
signal_reloj = False


def inicio_reloj():
    global inicio
    print("¡Bienvenido al juego del cronómetro, la puntuación ideal es 0, a ver qué consigues tú!")
    for i in range(3,0,-1):
        print(f"Iniciamos reloj en:{i} segundos")
        time.sleep(1)
    inicio = time.time()

def mostrar_tiempo():
    global inicio, signal_reloj
    while not signal_reloj:
        print(f"{(time.time()-inicio)}")

def parar_reloj(signum, frame):
    global final, inicio, signal_reloj
    signal_reloj = True
    final = time.time()

def calcular_puntuacion():
    global inicio, final
    print(f"Tu puntuación es de: {((final-inicio)**2):.0f}")

signal.signal(signal.SIGUSR1, parar_reloj)

inicio_reloj()
mostrar_tiempo()
calcular_puntuacion()