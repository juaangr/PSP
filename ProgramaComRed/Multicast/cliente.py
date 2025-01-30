import socket
import struct
import sys

mensaje = ""
multicast_group = ('224.0.0.1', 5000)

# creamos el socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# establecemos un timeout para que no se quede bloqueado
# por intentar siempre recibir respuestas
sock.timeout(2)

# establecemos el num de saltos, como va a ser un program
# "local", le pondremos 1


# supongo que aqui van más cosas
#######################################


# ahora solo queda enviar la informacion como lo hariamos 
# en un 
