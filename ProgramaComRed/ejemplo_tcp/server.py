import socket
import json
#import time

dir_server = ("localhost", 3000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(dir_server)
server.listen(10) # escuchamos y encolamos 10 conexiones
print(f"Server escuchando en {dir_server}")

while True:
    # Aceptamos la conexión
    socket_cliente, dir_cliente = server.accept()
    # time.sleep(2) # para tardar en dar la 
    info = json.dumps({nombre: "Jose", clase: "dam"})
    socket_cliente.send("Holaaaaaaaa".encode("UTF-8"))
    socket_cliente.close()