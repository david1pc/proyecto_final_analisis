import numpy as np
import time
from collections import deque

from grafos.algoritmos.Algoritmo import Algoritmo


def bfs_modificado(graph, start, visited):
    queue = deque([start])
    while queue:
        current_node = queue.popleft()
        visited[current_node] = True
        for neighbor in range(len(graph[current_node])):
            if not visited[neighbor] and graph[current_node][neighbor] > 0:
                # Agregar la condición adicional aquí (por ejemplo, para evitar ciertos nodos)
                if neighbor not in queue:
                    queue.append(neighbor)


def ejecutar(cantidades_nodos):
    ejecuciones = []
    for matriz_adyacencias, nodos, num_aristas in cantidades_nodos:
        inicio = time.time()
        # Nodo de inicio
        start_node = 0
        # Inicializar la lista de nodos visitados
        visited = np.full(nodos, False)
        # Ejecución del algoritmo BFS modificado
        bfs_modificado(matriz_adyacencias, start_node, visited)
        fin = time.time()
        tiempo_ejecucion = fin - inicio

        # Convertir el resultado a listas para almacenarlo en Algoritmo
        matriz_adyacencias = matriz_adyacencias.tolist()
        distancias = visited.tolist()

        algoritmo = Algoritmo("BFS Modificado", tiempo_ejecucion, nodos, matriz_adyacencias, distancias, num_aristas)

        ejecuciones.append(algoritmo)
    return ejecuciones, 'BFS Modificado'
