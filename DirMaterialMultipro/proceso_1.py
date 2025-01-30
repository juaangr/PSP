import signal

def avisa_proceso_2(pid):
    print("AVISANDO DEL PROCESO 2....")
    os.kill(pid, signal.SIGUSR1)

def matar_proceso_2(pid):
    print("Matando proceso 2...")
    os.kill(pid, signal.SIGINT)
    
def recibir_aviso(sigum, frame):
    print("Aviso recibido del proceso 2")

def recibir_matar(sigum, frame):
    print("Recibida la señal del proceso 2 para morir")
    print("ADIOS")

def leer_pid_proceso_2(): 
    problema_pid = True
    pid = None
    #while problema_pid:
     #   try:
           # pid = int(input())