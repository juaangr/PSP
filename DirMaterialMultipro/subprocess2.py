import os
import time

print("inicio")

r, w = os.pipe() #creamos 4 tuberias
pid = os.fork()
if pid > 0: #padre 
    os.close(r) #no vamosa leer
    os.write(w, b"hola")
    os.wait()
else:#hijo
    time.sleep(0.1)
    os.close(w)#no vamos a escribir
    texto = os.read(r,1024)
    if texto.lower() ==b"hola":
        print("adios")
    os.exit(0)    
#padre
os.close(w)
print("fin")