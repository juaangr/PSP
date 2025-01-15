import socket
import random

dir_server = ('127.0.0.1', 3000)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(dir_server)

print(f"")
# faltan cosas 
while(True):
    data, address = server.recvfrom(1024)
    numero = random.randint(1,100)
    print(f"recibido {data.decode()}")