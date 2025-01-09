import subprocess

salida = subprocess.run(("wc", "-l", "quijote.txt"), capture_output=True)
print(salida)