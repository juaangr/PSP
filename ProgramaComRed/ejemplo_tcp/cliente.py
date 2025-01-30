import socket  # Importamos la librería socket para la comunicación en red
import json  # Importamos json para manejar datos en formato JSON

# Definimos la dirección IP y el puerto del servidor al que queremos conectarnos
dir_server = ("127.0.0.1", 3000)

# Creamos un socket TCP
# AF_INET indica que usamos direcciones IPv4
# SOCK_STREAM indica que usamos el protocolo TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Nos conectamos al servidor en la dirección y puerto especificados
cliente.connect(dir_server)
print("Conectado al servidor")

# Esperamos recibir una respuesta del servidor (hasta 1024 bytes)
# recv() recibe datos en formato de bytes, por lo que debemos decodificarlos
respuesta = json.loads(cliente.recv(1024))  # Convertimos los datos JSON en un diccionario de Python

# Mostramos la respuesta del servidor
# Accedemos a los valores del diccionario y convertimos el nombre a mayúsculas
print(f"Respuesta del servidor: {respuesta['nombre'].upper()} {respuesta['clase']}")

# Cerramos la conexión con el servidor
cliente.close()
