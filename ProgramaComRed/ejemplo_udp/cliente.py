import socket  # Importamos la librería socket para la comunicación en red
import sys  # Importamos sys para manejar argumentos de línea de comandos

# Verificamos que se haya pasado exactamente un argumento al ejecutar el script
if len(sys.argv) != 2:
    exit()  # Si no se proporciona un argumento, se termina el programa

# Creamos un socket UDP
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Definimos la dirección del servidor al que vamos a enviar datos
direccion_server = ('127.0.0.1', 3000)

# sys.argv[1] es el argumento que el usuario proporciona al ejecutar el script.
# Lo codificamos a bytes y lo enviamos al servidor UDP en la dirección especificada
socket.sendto(sys.argv[1].encode(), direccion_server)

# Esperamos recibir una respuesta del servidor (hasta 1024 bytes)
data, address = socket.recvfrom(1024)

# Intentamos convertir la respuesta recibida a un entero
try:
    print(f"Recibido {int(data.decode())} de {address}")
except Exception as e:
    # Si la conversión a entero falla, imprimimos los datos en su formato original
    print(f"Recibido {data} de {address}")
    print(f"Error: {e}")  # Mostramos el error específico
