#faltan cosas
import socket

dir_server = ("127.0.0.1", 3000)
try:
    socket.socket()


try:
    while True:
        mensaje = input("Introduce un mensaje")
        if mensaje == "exit".lower() or mensaje=="":
            break
        socket.send(mensaje.encode())
        respuesta = socket.recv(1024).decode()
        print(f"Respuesta del servidor: {respuesta}")
except Exception as e: 
    print(f"Error: {e}")
finally:
    socket.close()