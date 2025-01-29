from multiprocessing import Process, Value

def sumar(valor):
    print("EJECUTANFO SUMAR")
    for i in range(200):
        print("sumando...")
        with valor.get.lock():
            valor.value +=1
    for _ in range(99999999999):
        pass
def restar(valor):
    print("EJECUTANDO RESTA")
    for i in range(200):
        with valor.get.lock():
            valor.value-=1
def multiplicar(valor):
    with valor.get.lock():
     print("EJECUTANDO MULTIPLICAR")
     valor.value*=2
     #valor.value('i', 0)     