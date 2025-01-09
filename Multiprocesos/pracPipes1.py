import os

print("Ini")

pid_hijo = os.fork()
r,w = os.pipe

# creamos la lista de numeros
def listaNumeros():
    numbers = []
    for i in range(1, 11):
        numbers.append(i)

# si el pid es 0 (hijo)
if (pid_hijo == 0): #hijo
    os.close(r) # cerramos la lectura
    numbers = listaNumeros()
    for number in numbers:
        os.write(w, str(number).encode())
    os.close(w)
    os._exit(0)
else: # padre
    os.close(w)
    # result = []
    while True:
        num = os.read(r, 1024) # leemos los numeros
        if not num:
            break
    
print("Fin")










"""Un proceso productor que genera una lista de números
del uno al diez y los envía a través de una pipe 
/ el proces consumidor los recibe y eleva al cuadrado 
cada número / el proces principal imprime
    
# crea y ejecuta el proceso productor
def productor(w):
    numbers = list(range[1,10])
    for number in numbers:
        os.write(w, f"{number}".encode())
    os.close(w)
                    
# crea y ejecuta el proceso consumidor    
def consumidor(r):

    
numbers = list(range(1, 11))
for number in numbers:
    os.write(pipe_out, f"{number}\n".encode())  # Escribir cada número en una línea
    os.close(pipe_out)
        
        
        
        """