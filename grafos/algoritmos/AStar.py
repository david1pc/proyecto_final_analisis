import numpy as np
import heapq
import networkx as nx
import time

from grafos.algoritmos.Algoritmo import Algoritmo


def heuristic(node, goal):
    # Heurística: distancia euclidiana entre el nodo y el objetivo
    return np.linalg.norm(np.array(node) - np.array(goal))


def astar(graph, start, goal, came_from):
    num_nodes = len(graph)
    open_list = []  # Lista de nodos pendientes de explorar
    heapq.heappush(open_list, (0, start))  # Tupla: (costo hasta ahora, nodo)
    g_scores = np.full(num_nodes, np.inf)  # Costos reales desde el nodo inicial
    g_scores[start] = 0
    f_scores = np.full(num_nodes, np.inf)  # Costos estimados desde el nodo inicial hasta el objetivo
    f_scores[start] = heuristic(start, goal)

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node == goal:
            # Se alcanzó el objetivo, reconstruir el camino y retornarlo
            path = [goal]
            while current_node != start:
                current_node = came_from[current_node]
                path.append(current_node)
            return list(reversed(path)), g_scores[goal]

        for neighbor in range(num_nodes):
            if graph[current_node][neighbor] > 0:
                tentative_g_score = g_scores[current_node] + graph[current_node][neighbor]

                if tentative_g_score < g_scores[neighbor]:
                    came_from[neighbor] = current_node
                    g_scores[neighbor] = tentative_g_score
                    f_scores[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_scores[neighbor], neighbor))

    # No se encontró un camino
    return None, np.inf

def ejecutar(cantidades_nodos):
    ejecuciones = []

    for matriz_adyacencias, nodos, num_aristas in cantidades_nodos:
        inicio = time.time()

        # Nodo de inicio y nodo objetivo
        start_node = 0
        goal_node = nodos - 1

        # Almacena el nodo previo en el camino óptimo
        came_from = np.full(nodos, -1)

        # Ejecución del algoritmo A*
        camino, costo = astar(matriz_adyacencias, start_node, goal_node, came_from)

        fin = time.time()
        tiempo_ejecucion = fin - inicio

        algoritmo = Algoritmo("A*", tiempo_ejecucion, nodos, matriz_adyacencias, camino, num_aristas)
        ejecuciones.append(algoritmo)
    return ejecuciones, 'A*'
