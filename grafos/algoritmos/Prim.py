import numpy as np
import time

from grafos.algoritmos.Algoritmo import Algoritmo


def prim_algorithm(graph):
    num_nodes = graph.shape[0]
    mst = np.zeros_like(graph)  # Inicializar el árbol de expansión mínima
    visited = np.full(num_nodes, False)  # Ningún nodo ha sido visitado aún
    visited[0] = True  # Empezar desde el primer nodo

    num_edges = 1

    while num_edges < num_nodes:
        min_weight = np.inf
        min_edge = ()

        for i in range(num_nodes):
            if visited[i]:
                for j in range(num_nodes):
                    if not visited[j] and graph[i][j] > 0 and graph[i][j] < min_weight:
                        min_weight = graph[i][j]
                        min_edge = (i, j)

        mst[min_edge] = min_weight
        mst[min_edge[1], min_edge[0]] = min_weight
        visited[min_edge[1]] = True
        num_edges += 1

    return mst


def ejecutar(matrices_adyacencias):
    ejecuciones = []
    for matriz_adyacencias, nodos, num_aristas in matrices_adyacencias:
        inicio = time.time()

        # Obtener el árbol de expansión mínima
        distancias = prim_algorithm(matriz_adyacencias)

        fin = time.time()
        tiempo_ejecucion = fin - inicio

        matriz_adyacencias = matriz_adyacencias.tolist()
        distancias = distancias.tolist()

        algoritmo = Algoritmo("prim", tiempo_ejecucion, nodos, matriz_adyacencias, distancias, num_aristas)

        ejecuciones.append(algoritmo)
    return ejecuciones, 'Prim'
