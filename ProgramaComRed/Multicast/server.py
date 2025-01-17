import socket
import struct
import sys

multicast_group = "224.0.0.1"
server_address = ('', 5000)

sock = socket.socket()


# escuchamos en el puerto
sock.bind(server_address)

group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq
)

#bucle que escucha/respuesta de peticiones
while True:
    print("")
    data, direccion = sock.recvfrom(1024)
    