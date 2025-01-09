import os
import time

print("LET'SSSS")

r, w = os.pipe() #creamos tuberias
pid = os.fork()
if pid > 0: #padre
    os.close(r) #no vamos a leer en el padre
    os.write(w, b"CACHIMBA")
    os.wait()#el proceso padre espera hasta que muera el hijo
else: #hijo
    time.sleep(0.5)
    os.close(w) #no vamos a escribir absolutamente nada con el hijo
    texto=os.read(r, 1024)
    if texto.lower()==b"cachimba":
        print("GEEET READYYYYYYYYY")
    os._exit(0)
os.close(w) #el padre, cierra el proceso de escritura
print("TO RUMBLEEEEEEE")