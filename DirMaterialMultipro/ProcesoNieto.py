import os

def main(): print("inicio")
pid_hijo = os.fork()
if pid_hijo== 0:
    pid_nieto=os.fork()
    if pid_nieto ==0:
        print(f"hola, soy el nieto con PID {os.getpid} y mi padre es el proceso con PID {os.getppid()}")
        os.exit(0)
    else:
        print(f"Hola soy el hijo con PID {os.getpid} y mi padre es el proceso con PID {os.getppid()}")
 





print("soy el proceso padre con PID: ", os.getpid())
pid = os.fork()
print(pid)
if pid > 0:
        #Codigo del proceso padre
        print("soy el proceso padre con PID: ", os.getpid())
        print("soy el proceso padre, mi hijo tiene PID: ", pid)
        #esperar a que el hijo muera/termine
        os.wait()
elif pid == 0:  
        print("soy el proceso hijo con PID: ", os.getpid())
        print("soy el proceso hijo, mi padre tiene PID: ", os.getpid())
else: 
        pid = os.fork()
        #codigo del proceso hijo
        print("soy el proceso nieto con PID: ", os.getpid())
        print("soy el proceso nieto, mi padre tiene PID: ", os.getpid())