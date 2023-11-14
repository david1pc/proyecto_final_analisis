import numpy as np
import time

from grafos.algoritmos.Algoritmo import Algoritmo


def bellman_ford(graph, start):
    num_nodes = len(graph)
    # Inicializar todas las distancias como infinito
    distancias = np.full(num_nodes, np.inf)
    # La distancia del nodo de inicio a sí mismo es 0
    distancias[start] = 0

    # Relajación de las aristas num_nodes - 1 veces
    for _ in range(num_nodes - 1):
        for u in range(num_nodes):
            for v in range(num_nodes):
                if graph[u][v] > 0 and distancias[u] + graph[u][v] < distancias[v]:
                    distancias[v] = distancias[u] + graph[u][v]

    # Verificar la existencia de ciclos de peso negativo
    for u in range(num_nodes):
        for v in range(num_nodes):
            if graph[u][v] > 0 and distancias[u] + graph[u][v] < distancias[v]:
                print("El grafo contiene un ciclo de peso negativo alcanzable desde el nodo de inicio.")
                return distancias

    return distancias


def ejecutar(cantidades_nodos):
    ejecuciones = []

    for matriz_adyacencias, nodos, num_aristas in cantidades_nodos:
        inicio = time.time()

        # Nodo de inicio
        start_node = 0

        # Ejecución del algoritmo de Bellman-Ford
        distancias = bellman_ford(matriz_adyacencias, start_node)

        fin = time.time()
        tiempo_ejecucion = fin - inicio

        algoritmo = Algoritmo("Bellman-Ford", tiempo_ejecucion, nodos, matriz_adyacencias, distancias, num_aristas)
        ejecuciones.append(algoritmo)

    return ejecuciones, 'Bellman-Ford'
