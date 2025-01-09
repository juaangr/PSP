from multiprocessing import Process, Array, Value
import os
import random

resultado = Value('i', 0)
longitud_lista = 10000000#int(input("Introduce el número deseado de elementos:"))
lista_num = Array('i',[random.randint(1,100) for x in range(longitud_lista)])
num_procesos = 1#int(input("Introduce el número deseado de procesos:"))
num_por_proc = len(lista_num) // num_procesos
print(lista_num)

def suma_array(valor, lista):
    print(lista)
    resultado_parcial = sum(lista)
    with valor.get_lock():
        valor.value += resultado_parcial
    print(f"La suma parcial del proceso con pid {os.getpid()} es : {resultado_parcial}")

for i in range(num_procesos):
    if i == num_procesos - 1:
        p = Process(target=suma_array, args=(resultado, lista_num[i*num_por_proc:]))
    else:
        p = Process(target=suma_array, args=(resultado, lista_num[i*num_por_proc: (i + 1)*num_por_proc]))
    p.start()
    p.join()

print(f"El resultado es :{resultado.value}")
