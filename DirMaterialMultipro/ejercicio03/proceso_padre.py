import signal
import os
import subprocess


'''
Este proceso lanza el segundo proceso, dándole su PID,
en ese momento, se queda esperando una línea de teclado
para poder pararlo y ver cómo de lejos nos hemos quedado de los 10 segundos
'''

p_cronometro = subprocess.Popen(["python", "proceso_cronometro.py"])

input("Presiona Enter para parar el cronometro")

os.kill(p_cronometro.pid, signal.SIGUSR1)

