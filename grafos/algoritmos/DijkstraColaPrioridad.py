import numpy as np
import heapq
import time

from grafos.algoritmos.Algoritmo import Algoritmo


class Grafo:
    def __init__(self, num_nodos, matriz_adyacencias):
        self.num_nodos = num_nodos
        self.matriz_adyacencias = matriz_adyacencias

    def dijkstra(self, start):
        distances = np.full(self.num_nodos, np.inf)
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in enumerate(self.matriz_adyacencias[current_node]):
                if weight > 0:
                    new_distance = current_distance + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heapq.heappush(priority_queue, (new_distance, neighbor))
        return distances


def ejecutar(cantidades_nodos):
    ejecuciones = []
    for matriz_adyacencias, nodos, num_aristas in cantidades_nodos:
        inicio = time.time()
        grafo = Grafo(nodos, matriz_adyacencias)

        start_node = 0
        distancias = grafo.dijkstra(start_node)

        fin = time.time()
        tiempo_ejecucion = fin - inicio

        algoritmo = Algoritmo("Dijkstra Priority Queue", tiempo_ejecucion, nodos, grafo.matriz_adyacencias, distancias, num_aristas)
        ejecuciones.append(algoritmo)

    return ejecuciones, 'Dijkstra PQ'
