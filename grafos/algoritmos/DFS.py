import numpy as np
import time

from grafos.algoritmos.Algoritmo import Algoritmo


def dfs(graph, start, visited):
    stack = [start]
    while stack:
        current_node = stack.pop()
        if not visited[current_node]:
            visited[current_node] = True
            stack.extend(neighbor for neighbor in range(len(graph[current_node])) if
                         not visited[neighbor] and graph[current_node][neighbor] > 0)


def ejecutar(cantidades_nodos):
    ejecuciones = []
    for matriz_adyacencias, nodos, num_aristas in cantidades_nodos:
        inicio = time.time()
        # Nodo de inicio
        start_node = 0
        # Inicializar la lista de nodos visitados
        visited = np.full(nodos, False)
        # Ejecución del algoritmo DFS iterativo
        dfs(matriz_adyacencias, start_node, visited)
        fin = time.time()
        tiempo_ejecucion = fin - inicio

        # Convertir el resultado a listas para almacenarlo en Algoritmo
        matriz_adyacencias = matriz_adyacencias.tolist()
        distancias = visited.tolist()

        algoritmo = Algoritmo("dfs", tiempo_ejecucion, nodos, matriz_adyacencias, distancias, num_aristas)

        ejecuciones.append(algoritmo)
    return ejecuciones, 'DFS'
