#proceso padre que escriba al hijo con pipes y que este reciba el mensaje, le responde, y el padre imprime 
import os
import time

r, w = os.pipe()
r2, w2 = os.pipe()
pid = os.fork()

if pid > 0: #padre
   os.close(r) #No vamos a leer en el padre
   os.close(w2) #no vamos a escribir  
   os.write(w, b"Hola proceso hijo") 
   os.wait()
   mensaje_hijo = os.read(r2, 1024).decode().lower()
   print(f"Desde el padre: {mensaje_hijo}")
else: #hijo
    time.sleep(0.1)
    os.close(r2)
    os.close(w)
    mensaje_padre = os.read(r, 1024).decode()
    if "hola" in mensaje_padre:
        os.write(w2, b"Buenas proceso padre")
    else:
        os.write(w2, b"Saluda primero")    
        