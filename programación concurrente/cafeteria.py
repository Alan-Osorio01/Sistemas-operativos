import threading
import time
import random
from queue import Queue

# Colas para manejar las dos fases del pedido
cola_tomar_cobrar = Queue()  # Cola para tomar y cobrar pedidos
cola_preparar_servir = Queue()  # Cola para preparar, servir y limpiar

# Definición de tareas de la primera fase: Tomar y Cobrar
def tomar_orden(cliente_id):
    print(f"Tomando orden del cliente {cliente_id}...")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"Orden del cliente {cliente_id} tomada.")

def cobrar_pedido(cliente_id):
    print(f"Cobrando el pedido del cliente {cliente_id}...")
    time.sleep(random.uniform(0.5, 1))
    print(f"Pedido del cliente {cliente_id} cobrado.")

# Definición de tareas de la segunda fase: Preparar, Servir y Limpiar
def preparar_cafe(cliente_id):
    print(f"Preparando el café para el cliente {cliente_id}...")
    time.sleep(random.uniform(1, 2))
    print(f"Café para el cliente {cliente_id} preparado.")

def servir_pedido(cliente_id):
    print(f"Sirviendo el pedido del cliente {cliente_id}...")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"Pedido del cliente {cliente_id} servido.")

def limpiar_estacion(cliente_id):
    print(f"Limpiando estación de preparación para el cliente {cliente_id}...")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"Estación limpia para el cliente {cliente_id}.")

# Función para la primera fase: Tomar y Cobrar
def fase_tomar_cobrar():
    while True:
        cliente_id = cola_tomar_cobrar.get()
        if cliente_id is None:
            break  # Termina el hilo si no hay más pedidos

        # Procesar tomar y cobrar para el cliente
        tomar_orden(cliente_id)
        cobrar_pedido(cliente_id)

        # Agregar el pedido a la segunda cola para la preparación
        cola_preparar_servir.put(cliente_id)
        cola_tomar_cobrar.task_done()

# Función para la segunda fase: Preparar, Servir y Limpiar
def fase_preparar_servir():
    while True:
        cliente_id = cola_preparar_servir.get()
        if cliente_id is None:
            break  # Termina el hilo si no hay más pedidos

        # Procesar preparación, servir y limpieza para el cliente
        preparar_cafe(cliente_id)
        servir_pedido(cliente_id)
        limpiar_estacion(cliente_id)
        cola_preparar_servir.task_done()

# Crear y ejecutar hilos para varios pedidos
def simulacion_cafeteria():
    print("Simulación de la cafetería con procesamiento en dos fases concurrentes.\n")

    # Crear el hilo para la fase de tomar y cobrar
    trabajador_tomar_cobrar = threading.Thread(target=fase_tomar_cobrar)
    trabajador_tomar_cobrar.start()

    # Crear hilos para la fase de preparar, servir y limpiar
    num_trabajadores_preparar_servir = 2  # Ajusta el número de trabajadores según necesidad
    trabajadores_preparar_servir = []
    for _ in range(num_trabajadores_preparar_servir):
        trabajador = threading.Thread(target=fase_preparar_servir)
        trabajador.start()
        trabajadores_preparar_servir.append(trabajador)

    # Agregar pedidos a la cola de tomar y cobrar
    for cliente_id in range(1, 6):  # Simulamos 5 clientes
        cola_tomar_cobrar.put(cliente_id)

    # Esperar a que todos los pedidos en la primera fase se completen
    cola_tomar_cobrar.join()

    # Señalar a los hilos de la segunda fase que finalicen
    for _ in trabajadores_preparar_servir:
        cola_preparar_servir.put(None)

    # Esperar a que todos los hilos terminen la segunda fase
    for trabajador in trabajadores_preparar_servir:
        trabajador.join()

    print("\nTodos los pedidos han sido gestionados.")

# Ejecutar la simulación
simulacion_cafeteria()