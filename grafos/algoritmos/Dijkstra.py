import numpy as np
import time

from grafos.algoritmos.Algoritmo import Algoritmo


def dijkstra(graph, start):
    num_nodes = graph.shape[0]
    distances = np.full(num_nodes, np.inf)  # Inicializar todas las distancias como infinito
    distances[start] = 0  # La distancia del nodo de inicio a sí mismo es 0
    visited = np.full(num_nodes, False)  # Ningún nodo ha sido visitado aún

    for _ in range(num_nodes):
        current_node = np.argmin(distances * (1 - visited))  # Obtener el nodo no visitado con la menor distancia

        for neighbor in range(num_nodes):
            if not visited[neighbor] and graph[current_node][neighbor] > 0:
                # Si el nodo vecino no ha sido visitado y hay un camino hacia él
                # Verificar si el camino actual es más corto que el almacenado previamente
                new_distance = distances[current_node] + graph[current_node][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        visited[current_node] = True  # Marcar el nodo como visitado

    return distances


def ejecutar(matrices_adyacencias):
    ejecuciones = []
    for matriz_adyacencias, nodos, num_aristas in matrices_adyacencias:
        inicio = time.time()

        # Nodo de inicio
        start_node = 0

        # Ejecución del algoritmo
        distancias = dijkstra(matriz_adyacencias, start_node)

        fin = time.time()
        tiempo_ejecucion = fin - inicio

        matriz_adyacencias = matriz_adyacencias.tolist()
        distancias = distancias.tolist()

        # imagen_grafo_b64 = obtener_imagen_grafo(matriz_adyacencias)
        algoritmo = Algoritmo("dijkstra", tiempo_ejecucion, nodos, matriz_adyacencias, distancias, num_aristas)

        ejecuciones.append(algoritmo)
    return ejecuciones, 'Dijkstra'
