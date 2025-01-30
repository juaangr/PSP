import socket
import threading
import json 

dir_server = ("localhost", 3000)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(dir_server)

server.listen(5) # el num 5 es de ejemplo

def acciones(cliente, direccion):
    data = cliente.recv(1024)
    if not data:
        cliente.close()
        print("Conexion cerrada")
    data_json = json.loads(data)
    print(data_json)


while True:
    cliente, direccion = server.accept()
    threading.Thread(target=acciones, args=(cliente, direccion))