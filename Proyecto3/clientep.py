import threading
import socket

# Configuración del cliente
HOST = '127.0.0.1'
PORT = 5000

def enviar_solicitud():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_socket:
        cliente_socket.connect((HOST, PORT))
        solicitud = "raiz,16"  # Solicitud de prueba
        cliente_socket.sendall(solicitud.encode())
        resultado = cliente_socket.recv(1024).decode()
        print(f"[RESULTADO] {resultado}")

# Crear múltiples hilos de clientes para realizar la prueba de estrés
def prueba_estres(num_solicitudes):
    hilos = []
    for _ in range(num_solicitudes):
        hilo = threading.Thread(target=enviar_solicitud)
        hilo.start()
        hilos.append(hilo)

    for hilo in hilos:
        hilo.join()

if __name__ == "__main__":
    # Ejecutar 100 solicitudes de prueba concurrentemente
    prueba_estres(3000)
