import os

""" escribe un programa que use 3 llamadas consecutivas a fork para crear 
    procesos, cada proceso debe imprimir su nivel jerarquico
    Abuelo, hijo, nieto, bisnieto... """

print("Iniciamos")
# aqui tenemos la variable donde estara nuestro primer fork
pid_hijo = os.fork()

# ya que fork devuelve un int que es cero para el hijo y random para el padre
# llamamos a la variable pid_hijo
# lo vamos a meter dentro de un metodo para que sea mas facil su uso
def tres_procesos():

    if (pid_hijo == 0): # dentro del primer hijo 
        print(f"Soy el primer hijo: {os.getpid()}, mi padre es: {os.getpid()}")
        
        # que va a pasar en este segundo fork?
        # hara que pasemos a clonar tanto el padre como al hijo
        # (nieto1) (hijo del hijo) 
        pid_nieto = os.fork()

        if (pid_nieto == 0): # dentro del segundo hijo (nieto)
            print(f"Soy el primer nieto, con PID {os.getpid()}, mi padre es: {os.getppid()}")
            pid_bisnieto  = os.fork()

            if (pid_bisnieto == 0): # dentro del tercer hijo (bisnieto)            
                print(f"hola soy el bisnieto con pid {os.getpid()}, mi padre es: {os.getppid()}")
                # os.exit(0)
            else: # saliendo de dentro para afuera, nieto, espera a bisnieto 
                os.wait()
                os._exit(0) # Termina el nieto        

        else: # Hijo, espera al nieto 
            os.wait() 
            os._exit(0) # termina el hijo 

    else: # volvemos al padre (o abuelo)
        # print(f"(repetido) Soy el abuelo (o padre) con pid: {os.getpid()}") Lo quitamos porque ya hay un if que nos imprime 
        # aqui en el else ya estamos creando dos procesos por debajo
        #segundo fork desde el abuelo (el primero es el primer bloque if)
        pid_hijo2 = os.fork()
        if (pid_hijo2 == 0): # este es el segundo hijo del padre (o abuelo)

            print(f"Soy el segundo hijo, mi PID es: {os.getpid()}, mi padre es: {os.getppid()}")
            # fork dentro del hijo 2 del padre o abuelo
            pid_nieto2 = os.fork()
            if (pid_nieto2 == 0):
                print(f"Hola desde el segundo nieto, mi pid es: {os.getpid()}, mi padre es: {os.getppid()} ")
                pid_bisnieto2 = os.fork()                

                if (pid_bisnieto2 == 0): #estamos dentro del tercer fork
                    print(f"Soy el segundo bisnieto con PID: {os.getpid()}, mi padre es: {os.getppid()}")
                    # os._exit(0) esto no lo comprendo
                else: # salimos de dentro hacia afuera, nieto espera al bisnieto
                    os.wait()
                    os._exit(0)
            else: # estamos en el hijo dos otra vez, esperamos al nieto
                print(f"Soy el segundo hijo de nuevo despues del segundo nieto: PID: {os.getpid()}, mi padre es: {os.getppid()}")
                os.wait()
                os._exit(0)
        else: # estamos en el proceso padre de nuevo
            print(f"Soy el padre (o abuelo) con pid: {os.getpid()}, estoy esperando a que terminen mis hijos")
            os.wait()
            os.wait()
            os._exit(0)

if __name__ == "__main__":
    tres_procesos()