import socket


# establecer la conn -> seleccionamos las opciones ->
# -> los enlazamos

dir_server = ('127.0.0.1', 3000) 

# socket.socket() crea un nuevo socket usando la dir de la fam dada
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# le metemos las options que queremos para el socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
# los enlazamos, queremos que el server se conecte al socket
server.bind(dir_server)
server.listen(15)
print(f"Server escuchando en: {dir_server}")


# Mientras la conexión sea verdadera (esta abierta)
while True: 
    clientSocket, dir_client = server.accept()
    clientSocket.send(f"HOLA".encode())
    clientSocket.close()