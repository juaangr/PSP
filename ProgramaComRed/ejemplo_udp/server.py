'''
Este servidor responde siempre con un número aleatorio al cliente que se conecta.
'''
import socket
import random


direccion_server = ('127.0.0.1', 3000)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# asociamos el socket a la dirección y el puerto especificados
server.bind(direccion_server)

print(f"Servidor escuchando en la dirección: {direccion_server[0]}:{direccion_server[1]}")

# Bucle infinito que hace que el server siga escuchando conexiones
while(True):
    # esperamos recibir datos de algun cliente (hasta 1024 bytes)
    data, address = server.recvfrom(1024)
    # generamos un num aleatorio entre uno y cien
    numero = random.randint(1, 100)
    # Mostramos en consola el mensaje recibido y la direccion del cliente
    print(f"Recibido {data.decode()} de {address}")
    # enviamos el numero aleatorio como respuesta al cliente
    server.sendto(str(numero).encode(), address)