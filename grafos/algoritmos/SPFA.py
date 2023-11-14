import numpy as np
import time
from collections import deque

from grafos.algoritmos.Algoritmo import Algoritmo


def spfa(graph, start):
    num_nodes = len(graph)
    distances = np.full(num_nodes, np.inf)
    distances[start] = 0
    in_queue = np.full(num_nodes, False)

    queue = deque([start])
    in_queue[start] = True

    while queue:
        current_node = queue.popleft()
        in_queue[current_node] = False

        for neighbor in range(num_nodes):
            if graph[current_node][neighbor] > 0:
                new_distance = distances[current_node] + graph[current_node][neighbor]

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

                    if not in_queue[neighbor]:
                        queue.append(neighbor)
                        in_queue[neighbor] = True

    return distances


def ejecutar(matrices_adyacencias):
    ejecuciones = []
    for matriz_adyacencias, nodos, num_aristas in matrices_adyacencias:
        inicio = time.time()
        # Nodo de inicio
        start_node = 0
        # Ejecución del algoritmo SPFA
        distancias = spfa(matriz_adyacencias, start_node)
        fin = time.time()
        tiempo_ejecucion = fin - inicio

        # Convertir el resultado a listas para almacenarlo en Algoritmo
        matriz_adyacencias = matriz_adyacencias.tolist()
        distancias = distancias.tolist()

        algoritmo = Algoritmo("SPFA", tiempo_ejecucion, nodos, matriz_adyacencias, distancias, num_aristas)

        ejecuciones.append(algoritmo)
    return ejecuciones, 'SPFA'
