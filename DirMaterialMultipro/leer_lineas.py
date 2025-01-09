import subprocess

lineas = subprocess.run(["grep", "sancho", "quijote.txt"], capture_output=True)
x = subprocess.run(["wc", "-l"], capture_output=True, input=lineas.stdout)

print(lineas.stdout.decode)