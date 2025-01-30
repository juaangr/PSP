import os

print("INICIO")
pid_hijo=os.fork()
if pid_hijo > 0: #padre
    os.wait()
    print(f"hola desde el padre tengo un pid de : {os.getpid()}")
else: #hijo
    pid_nieto_1 = os.fork()
    if pid_nieto_1 > 0: #hijo
        os.wait()
        print(f"Hola desde el hijo, tengo un pid de : {os.getpid()}")
        os.exit(0)
    else: #nieto_1
        pid_nieto_2 = os.fork() 
        if pid_nieto_2>0: #nieto1
            print(f"hola desde el primer nieto, mi pid es de : {os.getpid()}")
print("FINAL")        