import numpy as np
import time
import heapq

from grafos.algoritmos.Algoritmo import Algoritmo


def kruskal(graph):
    num_nodes = graph.shape[0]
    edges = []
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if graph[i][j] > 0:
                edges.append((i, j, graph[i][j]))

    edges.sort(key=lambda x: x[2])  # Ordenar aristas por peso
    parent = list(range(num_nodes))
    rank = [0] * num_nodes

    def find_set(x):
        if parent[x] != x:
            parent[x] = find_set(parent[x])
        return parent[x]

    def union_sets(x, y):
        root_x = find_set(x)
        root_y = find_set(y)
        if root_x != root_y:
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
                rank[root_y] += 1

    minimum_spanning_tree = np.zeros_like(graph)

    for edge in edges:
        u, v, weight = edge
        if find_set(u) != find_set(v):
            union_sets(u, v)
            minimum_spanning_tree[u][v] = weight
            minimum_spanning_tree[v][u] = weight

    return minimum_spanning_tree


def dijkstra_priority_queue(graph, start):
    num_nodes = graph.shape[0]
    distances = np.full(num_nodes, np.inf)
    distances[start] = 0
    visited = np.full(num_nodes, False)

    min_heap = [(0, start)]

    while min_heap:
        current_dist, current_node = heapq.heappop(min_heap)

        if current_dist > distances[current_node]:
            continue

        for neighbor in range(num_nodes):
            if not visited[neighbor] and graph[current_node][neighbor] > 0:
                new_distance = distances[current_node] + graph[current_node][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(min_heap, (new_distance, neighbor))

        visited[current_node] = True

    return distances


def ejecutar(cantidades_nodos):
    ejecuciones = []

    for matriz_adyacencias, nodos in cantidades_nodos:
        inicio = time.time()
        # Ejecución del algoritmo de Kruskal
        arbol_expansion_minima = kruskal(matriz_adyacencias)
        fin = time.time()
        tiempo_ejecucion = fin - inicio

        # Convertir el resultado a listas para almacenarlo en Algoritmo
        arbol_expansion_minima = arbol_expansion_minima.tolist()
        algoritmo = Algoritmo("kruskal", tiempo_ejecucion, nodos, matriz_adyacencias.tolist(), arbol_expansion_minima)
        ejecuciones.append(algoritmo)
    return ejecuciones, 'kruskal'
