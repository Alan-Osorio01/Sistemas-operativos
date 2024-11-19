import socket
import threading

# Configuración del servidor de recepción
HOST = '127.0.0.1'
PORT = 5000

def manejar_cliente(conexion, direccion):
    print(f"[NUEVA CONEXIÓN] Cliente conectado desde {direccion}")
    
    # Recibir datos del cliente
    datos = conexion.recv(1024).decode()
    print(f"[DATOS RECIBIDOS] {datos} de {direccion}")

    # Conectar al microservicio de procesamiento para enviarle los datos
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as procesador_socket:
        procesador_socket.connect(('127.0.0.1', 6000))
        procesador_socket.sendall(datos.encode())
        resultado = procesador_socket.recv(1024).decode()

    # Enviar el resultado al cliente
    conexion.sendall(resultado.encode())
    conexion.close()
    print(f"[CONEXIÓN CERRADA] Cliente {direccion} desconectado")

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f"[ESCUCHANDO] Microservicio de recepción en {HOST}:{PORT}")
    
    while True:
        conexion, direccion = servidor.accept()
        # Crear un hilo para cada cliente
        hilo = threading.Thread(target=manejar_cliente, args=(conexion, direccion))
        hilo.start()
        print(f"[HILOS ACTIVOS] {threading.active_count() - 1}")

if __name__ == "__main__":
    iniciar_servidor()
