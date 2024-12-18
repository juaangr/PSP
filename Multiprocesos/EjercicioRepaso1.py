# imprimir en el proceso principal si en la ruta en la que estamos trabajando pone "home"

import subprocess

path = subprocess.run(["pwd"], capture_output=True)
getHome = subprocess.run(["grep", "home"], input=path.stdout, texto=True)
(path)