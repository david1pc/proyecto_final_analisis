import numpy as np
import time

from grafos.algoritmos.Algoritmo import Algoritmo


def bfs(graph, start):
    num_nodes = len(graph)
    visited = np.full(num_nodes, False)  # Ningún nodo ha sido visitado aún
    distances = np.full(num_nodes, np.inf)  # Inicializar todas las distancias como infinito
    distances[start] = 0  # La distancia del nodo de inicio a sí mismo es 0

    queue = []
    queue.append(start)

    while queue:
        current_node = queue.pop(0)
        visited[current_node] = True

        for neighbor in range(num_nodes):
            if graph[current_node][neighbor] > 0 and not visited[neighbor]:
                # Si el nodo vecino tiene una arista y no ha sido visitado
                # Actualizar la distancia y agregar el nodo a la cola
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)
                visited[neighbor] = True

    return distances


def ejecutar(cantidades_nodos):
    ejecuciones = []

    for matriz_adyacencias, nodos in cantidades_nodos:
        inicio = time.time()
        # Nodo de inicio
        start_node = 0

        # Ejecución del algoritmo BFS
        distancias = bfs(matriz_adyacencias, start_node)

        fin = time.time()
        tiempo_ejecucion = fin - inicio

        algoritmo = Algoritmo("BFS", tiempo_ejecucion, nodos, matriz_adyacencias, distancias)
        ejecuciones.append(algoritmo)

    return ejecuciones, 'BFS'
