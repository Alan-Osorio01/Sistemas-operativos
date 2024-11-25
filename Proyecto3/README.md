
# Proyecto de Microservicios para Operaciones Matemáticas
## Intengrantes:
1. Alan Osorio
2. Ana Amador
3. Daniela Lopez
4. Daniel Reyes
5. Paula Caballero 

## Descripción General
Este proyecto implementa un sistema de microservicios para procesar solicitudes de operaciones matemáticas. Utiliza sockets para la comunicación entre clientes y servidores.

## Archivos del Proyecto

### 1. `cliente.py`
- **Descripción**: Este script permite al usuario seleccionar una operación matemática (raíz cuadrada, potencia, logaritmo natural, factorial, seno, coseno) e ingresar un número. La solicitud se envía al servidor de recepción para su procesamiento.
- **Uso**: Ejecutar `python3 cliente.py` y seguir las instrucciones en consola para enviar una solicitud.

### 2. `clientep.py`
- **Descripción**: Variante del cliente utilizada para realizar pruebas de rendimiento. Envía solicitudes predefinidas en múltiples hilos para probar la capacidad de manejo de solicitudes del sistema.
- **Uso**: Ejecutar `python3 clientep.py` para iniciar las pruebas de estrés.

### 3. `proce.py`
- **Descripción**: Microservicio encargado de realizar el procesamiento de las operaciones matemáticas solicitadas. Procesa la operación recibida y devuelve el resultado.
- **Uso**: Ejecutar `python3 proce.py` para iniciar el microservicio de procesamiento.

### 4. `recep.py`
- **Descripción**: Servidor de recepción que actúa como intermediario. Recibe las solicitudes de los clientes, las envía al microservicio de procesamiento y devuelve el resultado al cliente.
- **Uso**: Ejecutar `python3 recep.py` para iniciar el microservicio de recepción.

## Cómo Ejecutar el Proyecto
1. Iniciar el servidor de recepción:
   ```bash
   python3 recep.py
   ```
2. Iniciar el microservicio de procesamiento:
   ```bash
   python3 proce.py
   ```
3. Ejecutar el cliente para enviar solicitudes:
   ```bash
   python3 cliente.py
   ```
   - Alternativamente, para pruebas de estrés:
   ```bash
   python3 clientep.py
   ```

## Requisitos
- Python 3.x
- Módulos: `socket`, `threading`

## Notas
- Este proyecto está diseñado para ejecutarse en una red local utilizando la dirección `127.0.0.1` y los puertos especificados.
