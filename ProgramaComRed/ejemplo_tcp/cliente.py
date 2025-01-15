import	socket
import json

dir_server = ("127.0.0.1", 3000)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(dir_server)
print("conectado al server")

respuesta = json.loads(cliente.recv(1024)) # se queda ......


print(f"Respuesta del servidor: {respuesta['nombre']}") # falta respuesta xd

cliente.close()