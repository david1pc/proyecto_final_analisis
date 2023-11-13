import numpy as np
import time

from grafos.algoritmos.Algoritmo import Algoritmo


def topological_sort(graph):
    num_nodes = len(graph)
    in_degree = np.zeros(num_nodes, dtype=int)

    # Calcular grados de entrada
    for i in range(num_nodes):
        for j in range(num_nodes):
            if graph[i][j] > 0:
                in_degree[j] += 1

    # Inicializar la cola con nodos de grado de entrada cero
    queue = [node for node in range(num_nodes) if in_degree[node] == 0]
    sorted_nodes = []

    while queue:
        current_node = queue.pop(0)
        sorted_nodes.append(current_node)

        for neighbor in range(num_nodes):
            if graph[current_node][neighbor] > 0:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    return sorted_nodes


def ejecutar(matrices_adyacencias):
    ejecuciones = []
    for matriz_adyacencias, nodos in matrices_adyacencias:
        inicio = time.time()
        # Ejecución del algoritmo de orden topológico
        orden_topologico = topological_sort(matriz_adyacencias)
        fin = time.time()
        tiempo_ejecucion = fin - inicio

        # Convertir el resultado a listas para almacenarlo en Algoritmo
        matriz_adyacencias = matriz_adyacencias.tolist()
        orden_topologico = np.array(orden_topologico).tolist()

        algoritmo = Algoritmo("Topological Sort", tiempo_ejecucion, nodos, matriz_adyacencias, orden_topologico)

        ejecuciones.append(algoritmo)
    return ejecuciones, 'Topological Sort'
