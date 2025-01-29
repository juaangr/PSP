import socket
import threading
import json 
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

direccion_server = ("localhost", 3000)

sock.connect(direccion_server)

mensaje = json.dumps({"action": "listar"})

sock.send(mensaje)
data = sock.recv(1024)
if not data:
    sock.close()
    sys.exit()
data_json = json.loads(data)
print(data_json)
