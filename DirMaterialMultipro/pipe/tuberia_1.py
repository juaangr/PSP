import os
import time
print("INICIO")
r, w = os.pipe() # creamos 4 tuberias
pid = os.fork()
if pid > 0: # padre
    os.close(r) # no vamos a leer
    os.write(w, "Hola".encode())
    os.wait()
else: #hijo
    time.sleep(0.1)
    os.close(w) #no vamos a escribir
    texto = os.read(r,1024).decode()
    if texto.lower() == "hola":
        print("Adios")
    os._exit(0)
# padre
os.close(w)
print("FIN")
