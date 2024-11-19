import socket
import threading
import math

# Configuración del microservicio de procesamiento
HOST = '127.0.0.1'
PORT = 6000

def manejar_procesamiento(conexion, direccion):
    print(f"[PROCESAMIENTO] Conexión desde {direccion}")
    
    # Recibir datos y procesar la solicitud STEM
    datos = conexion.recv(1024).decode()
    print(f"[DATOS A PROCESAR] {datos}")

    # Interpretar la solicitud en formato "operacion,numero"
    try:
        operacion, valor = datos.split(",")
        numero = float(valor)
        
        if operacion == "raiz":
            resultado = math.sqrt(numero)
            respuesta = f"Raíz cuadrada de {numero} es {resultado:.2f}"
        elif operacion == "potencia":
            resultado = math.pow(numero, 2)  # Ejemplo: elevar al cuadrado
            respuesta = f"{numero} elevado al cuadrado es {resultado:.2f}"
        elif operacion == "log":
            resultado = math.log(numero)
            respuesta = f"Logaritmo natural de {numero} es {resultado:.2f}"
        elif operacion == "factorial":
            resultado = math.factorial(int(numero))
            respuesta = f"Factorial de {int(numero)} es {resultado}"
        elif operacion == "seno":
            resultado = math.sin(numero)
            respuesta = f"Seno de {numero} es {resultado:.2f}"
        elif operacion == "coseno":
            resultado = math.cos(numero)
            respuesta = f"Coseno de {numero} es {resultado:.2f}"
        else:
            respuesta = "Operación no reconocida."
    except ValueError:
        respuesta = "Error: Datos recibidos no válidos."

    # Enviar el resultado de vuelta
    conexion.sendall(respuesta.encode())
    conexion.close()
    print(f"[PROCESO COMPLETO] Resultado enviado a {direccion}")

def iniciar_procesador():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f"[ESCUCHANDO] Microservicio de procesamiento en {HOST}:{PORT}")
    
    while True:
        conexion, direccion = servidor.accept()
        # Crear un hilo para cada solicitud de procesamiento
        hilo = threading.Thread(target=manejar_procesamiento, args=(conexion, direccion))
        hilo.start()

if __name__ == "__main__":
    iniciar_procesador()
