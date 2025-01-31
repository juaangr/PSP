import json  # Para manejar datos en formato JSON
import socket  # Para la comunicación en red

# Configuración del cliente
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creación del socket TCP/IP
direccion_server = ("localhost", 3000)  # Dirección y puerto del servidor
sock.connect(direccion_server)  # Conectar al servidor

def recibir_mensaje():
    """Recibe y procesa un mensaje del servidor."""
    try:
        data = sock.recv(1024)  # Recibe hasta 1024 bytes del servidor
        if not data:  # Si no hay datos, el servidor cerró la conexión
            print("El servidor cerró la conexión.")
            sock.close()
            exit(1)  # Terminar la ejecución
        return json.loads(data)  # Convertir el mensaje JSON en un diccionario
    except json.JSONDecodeError:
        print("Error al interpretar la respuesta del servidor.")
        return {"error": "Datos corruptos"}  # Retorna un mensaje de error

def main():
    while True:
        # Solicitar acción al usuario
        action = input("Introduce una acción (listar, crear, jugar, salir): ").strip().lower()

        if action == "listar":
            # Enviar acción "listar" al servidor
            sock.send(json.dumps({"action": "listar"}).encode())
            print(recibir_mensaje())  # Recibir y mostrar respuesta del servidor

        elif action == "crear":
            # Enviar acción "crear" al servidor
            sock.send(json.dumps({"action": "crear"}).encode())

            print(recibir_mensaje()["mensaje"])  # Recibir mensaje del servidor
            nombre_test = input().strip()  # Pedir nombre del test
            sock.send(json.dumps({"nombre": nombre_test}).encode())  # Enviar nombre del test

            while True:
                mensaje = recibir_mensaje()  # Recibir mensaje del servidor
                print(mensaje["mensaje"])  # Mostrar mensaje recibido

                if "enunciado" in mensaje["mensaje"].lower():
                    enunciado = input().strip()  # Pedir enunciado de la pregunta
                    sock.send(json.dumps({"enunciado": enunciado}).encode())
                    if enunciado.lower() == "fin":  # Si el usuario escribe "fin", termina la creación
                        break
                elif "opciones" in mensaje["mensaje"].lower():
                    opciones = input("Introduce las opciones separadas por coma: ").strip()
                    sock.send(json.dumps({"opciones": opciones}).encode())  # Enviar opciones
                elif "correcta" in mensaje["mensaje"].lower():
                    correcta = input("Introduce la respuesta correcta: ").strip()
                    sock.send(json.dumps({"correcta": correcta}).encode())  # Enviar respuesta correcta

            print(recibir_mensaje()["mensaje"])  # Mostrar mensaje de confirmación del servidor

        elif action == "jugar":
            # Enviar acción "jugar" al servidor
            sock.send(json.dumps({"action": "jugar"}).encode())
            nombre = input("Introduce el nombre del test a jugar: ").strip()
            sock.send(json.dumps({"nombre": nombre}).encode())  # Enviar nombre del test

            while True:
                pregunta = recibir_mensaje()  # Recibir pregunta del servidor

                if "puntuacion" in pregunta:  # Si el mensaje contiene "puntuacion", el test terminó
                    print(f"Puntuación final: {pregunta['puntuacion']} de {pregunta['total']}")
                    break

                print(pregunta["enunciado"])  # Mostrar enunciado de la pregunta
                for opcion in pregunta["opciones"]:
                    print(f"- {opcion}")  # Mostrar opciones de respuesta

                respuesta = input("Tu respuesta: ").strip()  # Pedir respuesta del usuario
                sock.send(json.dumps({"respuesta": respuesta}).encode())  # Enviar respuesta al servidor

        elif action == "salir":
            print("Cerrando conexión...")
            sock.close()  # Cerrar la conexión con el servidor
            break  # Salir del bucle

        else:
            print("Opción no válida. Usa: listar, crear, jugar o salir.")  # Mensaje de error para entrada incorrecta

main()  # Ejecutar la función principal
