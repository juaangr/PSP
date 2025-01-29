import subprocess

# subprocess.run sirve para 
resultado_ls = subprocess.run(["ls", "-l", "."], capture_output=True)
resultado_wc = subprocess.run(["wc","-l"], input=resultado_ls.stdout)
print(resultado_ls-1) # el mnos uno sirve porque en la salida cuenta también la linea de "total"