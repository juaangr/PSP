import os
from multiprocessing import Process, Value, Array
import random


lista = []

for _ in range(100):
    lista.append(random.randint(1,100))

def sum(value):
    for _ in range(50):
        lista.value += 1
def sub(lista):
    for _ in range(50):
        lista.value -= 1
        
print("A ver, empezamos") 
lista = value('i', 0)
lock = Lock() 
process_sum
process_sub