import socket  # Importamos la librería socket para la comunicación en red
import json  # Importamos json para manejar datos en formato JSON


# Definimos la dirección IP y el puerto en el que el servidor estará escuchando
dir_server = ("localhost", 3000)

# Creamos un socket TCP
# AF_INET indica que usamos direcciones IPv4
# SOCK_STREAM indica que usamos el protocolo TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configuramos el socket para reutilizar la dirección y evitar errores al reiniciar el servidor
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Asociamos el socket a la dirección y puerto especificados
server.bind(dir_server)

# Hacemos que el servidor escuche conexiones entrantes, con una cola de hasta 10 clientes en espera
server.listen(10)

# Mostramos en consola que el servidor está activo y escuchando conexiones
print(f"Servidor escuchando en {dir_server[0]}:{dir_server[1]}")

# Bucle infinito para aceptar conexiones de clientes
while True:
    
    # Aceptamos una conexión entrante
    # socket_cliente es el socket que se usará para comunicarse con el cliente
    # dir_cliente contiene la dirección IP y el puerto del cliente conectado
    socket_cliente, dir_cliente = server.accept()

    # Creamos un diccionario con la información que se enviará al cliente
    info = json.dumps({"nombre": "Jose", "clase": "DAM"})  # Convertimos el diccionario a formato JSON
    # Enviamos la información codificada en bytes al cliente
    socket_cliente.send(info.encode())
    # Cerramos la conexión con el cliente después de enviar la respuesta
    socket_cliente.close()
