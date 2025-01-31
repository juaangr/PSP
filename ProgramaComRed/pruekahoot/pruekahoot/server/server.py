import socket  # Para la comunicación en red
import json  # Para manejar datos en formato JSON
import threading  # Para manejar múltiples clientes concurrentemente
import os  # Para interactuar con el sistema de archivos

# Configuración del servidor
direccion_server = ("localhost", 3000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creación del socket TCP/IP
server.bind(direccion_server)  # Enlazar el socket a la dirección y puerto
server.listen(5)  # Escuchar hasta 5 conexiones simultáneas
print(f"Servidor escuchando en {direccion_server}")

def enviar_mensaje(cliente, mensaje):
    """Envía un mensaje en formato JSON asegurando que el cliente lo reciba correctamente."""
    try:
        cliente.send(json.dumps(mensaje).encode())
    except:
        print("Error al enviar mensaje al cliente.")

def recibir_mensaje(cliente):
    """Recibe un mensaje del cliente y lo convierte en JSON."""
    try:
        data = cliente.recv(1024)  # Recibir hasta 1024 bytes
        if not data:
            return None  # Si no hay datos, retornar None
        return json.loads(data)  # Convertir de JSON a diccionario
    except json.JSONDecodeError:
        return None  # En caso de error en la conversión, retornar None

def listar(cliente):
    """Envía la lista de tests disponibles."""
    tests = [x for x in os.listdir() if x.startswith("test_") and x.endswith(".json")]
    enviar_mensaje(cliente, {"tests": tests} if tests else {"error": "No hay tests disponibles"})

def crear_test(cliente):
    """Permite a un cliente crear un test."""
    enviar_mensaje(cliente, {"mensaje": "Introduce el nombre del test"})
    
    data = recibir_mensaje(cliente)
    if not data:
        return
    nombre_test = data.get("nombre", "").strip().replace(" ", "_")  # Formatear el nombre del test

    preguntas = []
    while True:
        enviar_mensaje(cliente, {"mensaje": "Introduce el enunciado de la pregunta o 'fin' para terminar"})
        
        data = recibir_mensaje(cliente)
        if not data:
            return
        enunciado = data.get("enunciado", "").strip()

        if enunciado.lower() == "fin":  # Si el usuario escribe 'fin', salir del bucle
            break
        
        enviar_mensaje(cliente, {"mensaje": "Introduce las opciones de respuesta separadas por coma"})
        data = recibir_mensaje(cliente)
        if not data:
            return
        opciones = data.get("opciones", "").split(",")

        enviar_mensaje(cliente, {"mensaje": "Introduce la respuesta correcta"})
        data = recibir_mensaje(cliente)
        if not data:
            return
        correcta = data.get("correcta", "").strip()

        # Agregar la pregunta a la lista
        preguntas.append({"enunciado": enunciado, "opciones": opciones, "correcta": correcta})

    # Guardar el test en un archivo JSON
    with open(f"test_{nombre_test}.json", "w") as f:
        json.dump({"nombre": nombre_test, "preguntas": preguntas}, f, indent=4)

    enviar_mensaje(cliente, {"mensaje": "Test creado exitosamente"})

def jugar_test(cliente):
    """Permite jugar un test."""
    data = recibir_mensaje(cliente)
    if not data:
        return
    test_name = f"test_{data.get('nombre', '').strip()}.json"

    if not os.path.exists(test_name):  # Verificar si el test existe
        enviar_mensaje(cliente, {"error": "El test no existe"})
        return

    with open(test_name, "r") as f:
        test_data = json.load(f)  # Cargar el test desde el archivo

    puntuacion = 0
    for pregunta in test_data["preguntas"]:
        enviar_mensaje(cliente, pregunta)  # Enviar pregunta al cliente
        respuesta = recibir_mensaje(cliente)  # Recibir respuesta

        if respuesta and respuesta.get("respuesta", "").strip() == pregunta["correcta"]:
            puntuacion += 1  # Sumar puntuación si la respuesta es correcta

    # Enviar la puntuación final al cliente
    enviar_mensaje(cliente, {"puntuacion": puntuacion, "total": len(test_data["preguntas"])})

def manejar_cliente(cliente, direccion):
    """Maneja las acciones del cliente."""
    try:
        while True:
            data = recibir_mensaje(cliente)
            if not data:
                break

            action = data.get("action")
            if action == "listar":
                listar(cliente)
            elif action == "crear":
                crear_test(cliente)
            elif action == "jugar":
                jugar_test(cliente)
            else:
                enviar_mensaje(cliente, {"error": "Acción no válida"})

    except (ConnectionResetError, json.JSONDecodeError):
        print(f"Error con el cliente {direccion}")
    finally:
        cliente.close()
        print(f"Cliente {direccion} desconectado.")

# Bucle principal para aceptar clientes
while True:
    cliente, direccion = server.accept()  # Aceptar conexiones entrantes
    print(f"Cliente conectado {direccion}")
    threading.Thread(target=manejar_cliente, args=(cliente, direccion)).start()  # Crear un hilo para manejar al cliente
