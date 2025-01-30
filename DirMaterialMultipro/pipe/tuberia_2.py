import os

r1, w1 = os.pipe()
r2, w2 = os.pipe()

pid = os.fork()
if pid > 0: # padre
    # cerramos la lectura del hijo y la escritura del hijo
    os.close(r1) 
    os.close(w2)
    os.write(w1, 'Hola buenas desde el padre, ¿cómo estás?'.encode()) # si cambiamos la frase por un input podemos probar más cosas
    os.wait()
    respuesta = os.read(r2, 1024).decode()
    if "saluda" in respuesta:
        print("perdón")
    else:
        print("A seguir bien!")
else: # hijo
    # cerramos la lectura y escritura del padre
    os.close(r2)
    os.close(w1)
    mensaje = os.read(r1, 1024).decode()
    if "hola" in mensaje:
        os.write(w2,"Buenas desde el hijo".encode())
    else:
        os.write(w2,"Se saluda primero".encode())

    
    