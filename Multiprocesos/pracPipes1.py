import os

print("Inicio") # marcamos el inicio del programa

pid_hijo = os.fork() # guardamos el fork en la variable 
r,w = os.pipe # lo mismo con pipe, ya sabemos...

# creamos la lista de numeros
def listaNumeros():
    numbers = []
    for i in range(1, 11): # bucle que añade un numero a la lista del 1 al 10, range es excluyente en el segundo número
        numbers.append(i) # función de añadir

# si el pid es 0 (hijo)
if (pid_hijo == 0): #hijo
    os.close(r) # cerramos la lectura
    numbers = listaNumeros() # guardamos en la variable numbers el método que crea la lista
    for number in numbers: # Bucle que codea cada numero en una lista tipo str
        os.write(w, str(number).encode()) 
    os.close(w) # cerramos 
    os._exit(0) # salimos del proceso hijo
else: # padre
    os.close(w) # cerramos la escritura
    resultado = [] # creamos la lista resultado para manejar con facilidad el elevarlo al cuadrado
    while True: # mientras que sea verdadero
        num = os.read(r, 1024) # leemos los numeros
        if not num: # si no quedan más
            break # salimos del bucle
        num = int(num.decode().split) # decodeamos el tipo str en una lista 
        resultado.append(num**2) # Imprimimos el resultado ya elevado al cuadrado 

print(listaNumeros)
print("Estos son los cuadrados")
for res in resultado:
    print(res)

os.wait() # esperamos a que todos los procesos mueran

print("Fin") # marcamos el fin del programa