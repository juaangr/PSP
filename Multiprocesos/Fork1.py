import os 

""" escribe un programa que use 3 llamadas consecutivas a fork para crear 
    procesos, cada proceso debe imprimir su nivel jerarquico
    Abuelo, hijo, nieto, bisnieto... """

def tres_forks():
    for _ in range (3): # creamos tres fork()
        PID = os.fork()
        if (PID==0): # Proceso hijo 
            if level == 0:
                print(f"Soy el hijo (PID:{os.getpid()}, mi padre es: {os.getppid()})")
            elif (level == 1):
                print(f"Soy el Nieto (PID: {os.getpid()}, mi Padre es: {os.getppid()})")
            elif (level == 2):
                print(f"Soy el Bisnieto (PID: {os.getpid}, mi padre es: {os.getppid()})")
        else:
            break
