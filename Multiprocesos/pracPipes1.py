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
    resultado = [] # creamos la lista resultado para manejar con facilidad el elevarlo al cuadrado
    while True:
        num = os.read(r, 1024) # leemos los numeros
        if not num:
            break
        num = int(num.decode().split)
        resultado.append(num**2) # elevamos al cuadrado     

print(listaNumeros)
print("Estos son los cuadrados")
for res in resultado:
    print(res)

os.wait()

print("Fin")