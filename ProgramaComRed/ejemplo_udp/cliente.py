import sys
import socket
# faltan cosas

if len(sys.argv) != 2:
    exit()
    
zocalo = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dir_server = ('127.0.0.1', 3000)

zocalo.sendto(sys.argv[1].encode())