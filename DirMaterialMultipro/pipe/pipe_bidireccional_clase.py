import os
import time
r,w = os.pipe()
r2,w2 = os.pipe()

pid = os.fork()

if pid > 0: # padre
    os.close(r)
    os.close(w2)
    os.write(w, b"Hola proceso hijo")
    os.wait()
    mensaje_hijo = os.read(r2, 1024).decode()
    print(f"Desde el padre: {mensaje_hijo}")
else:
    time.sleep(0.1)
    os.close(w)
    os.close(r2)
    mensaje_padre = os.read(r, 1024).decode().lower()
    if "hola" in mensaje_padre:
        os.write(w2, b"Buenas proceso padre")
    else:
        os.write(w2, b"Saluda primero")

