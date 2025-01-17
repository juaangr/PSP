import socket


def crear_server():
    dir_server = ("127.0.0.1", 3000)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(dir_server)



def escuchar_cliente(server):
    while True:
        print("Servidor a la escucha...")
        data, dir_cliente = server.recv(1024).decode()
        # print('Recibido {} bytes de la direccion {}'.format(len(data), dir_cliente))
        
def respuesta_cliente(cliente, direccion):
    try:
        print(f"Conexión establecida con: {direccion}")
        while True: 
            data = cliente.recv(1024).decode()
    
    