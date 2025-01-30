# faltan cosas
import socket
import threading


def responder_cliente(cliente, direccion):
    try:
        print(f"Conexion establecida con {direccion}")
        while True:
            data = cliente.recv(1024).decode()
            # print(data)
            if not data:
                break
            print("Mensaje recibido")

def main():
    # creamos el socket tcp
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    dir_server = ("127.0.0.1", 3000)
    server.bind(dir_server)
    
    server.listen(5)
    print(f"servidor escuchando en: {dir_server}")
    while True:
        cliente, dir_cliente = server.accept()
        hilo = threading.Thread(target=responder_cliente, )