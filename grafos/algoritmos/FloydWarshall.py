import numpy as np
import time

from grafos.algoritmos.Algoritmo import Algoritmo


def floyd_warshall(graph):
    num_nodes = len(graph)
    distancias = np.copy(graph)

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if distancias[i][k] + distancias[k][j] < distancias[i][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]

    return distancias


def ejecutar(cantidades_nodos):
    ejecuciones = []

    for matriz_adyacencias, nodos, num_aristas in cantidades_nodos:
        inicio = time.time()

        # Ejecución del algoritmo de Floyd-Warshall
        distancias = floyd_warshall(matriz_adyacencias)

        fin = time.time()
        tiempo_ejecucion = fin - inicio

        algoritmo = Algoritmo("Floyd-Warshall", tiempo_ejecucion, nodos, matriz_adyacencias, distancias, num_aristas)
        ejecuciones.append(algoritmo)

    return ejecuciones, 'Floyd-Warshall'
