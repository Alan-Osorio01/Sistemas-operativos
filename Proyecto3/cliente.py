import socket

# Configuración del cliente
HOST = '127.0.0.1'
PORT = 5000

def enviar_solicitud():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_socket:
        cliente_socket.connect((HOST, PORT))
        
        # Elegir operación STEM
        print("Seleccione una operación:")
        print("1 - Raíz cuadrada")
        print("2 - Potencia (cuadrado)")
        print("3 - Logaritmo natural")
        print("4 - Factorial")
        print("5 - Seno")
        print("6 - Coseno")
        operacion = input("Ingrese el número de la operación: ")
        
        numero = input("Ingrese un número para procesar: ")

        # Mapear la elección del usuario a la operación
        operaciones = {
            "1": "raiz",
            "2": "potencia",
            "3": "log",
            "4": "factorial",
            "5": "seno",
            "6": "coseno"
        }
        operacion_solicitada = operaciones.get(operacion, "raiz")
        
        # Enviar solicitud en formato "operacion,numero"
        solicitud = f"{operacion_solicitada},{numero}"
        cliente_socket.sendall(solicitud.encode())
        
        # Recibir y mostrar la respuesta del microservicio de procesamiento
        resultado = cliente_socket.recv(1024).decode()
        print(f"[RESULTADO] {resultado}")

if __name__ == "__main__":
    enviar_solicitud()
