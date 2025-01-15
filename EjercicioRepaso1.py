# imprimir en el proceso principal si en la ruta en la que estamos trabajando pone "home"

import subprocess
from multiprocessing import Process

# busco dentro de un array, otro
def doesHomeApear(path):
    global resultado # esta referencia global nos permite cambiar la funcion si es que está en otra
    resultado = "home" in path.decode().lower()

# el resultado de pwd nos devuelve un stream de bytes por eso tenemos que cambiarlo a un str
# esto lo conseguimos arriba en el decode() -> va vacío porque default devuelve str

pathh = subprocess.run(["pwd"], capture_output=True) # capturamos el output en esa variable
proceso_p = Process(target=doesHomeApear, args=(pathh.stdout,))
proceso_p.start() # empezar 
proceso_p.join() # esperar, va a sincronizar todo
print(resultado)

"""
esta porcion lo hace con subprocess mas mnos

result_basename = subprocess.run(["basename"], input=pathh.stdout, text=True)
if (result_basename == "home"):
    print("true")
else:
    print("False")
"""