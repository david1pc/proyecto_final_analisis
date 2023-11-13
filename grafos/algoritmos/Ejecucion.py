import numpy as np
import networkx as nx
import os

from concurrent.futures import ThreadPoolExecutor
from grafos.algoritmos import Dijkstra,\
    Prim,\
    AStar,\
    BFS, \
    DijkstraColaPrioridad, \
    BellmanFord, \
    FloydWarshall, \
    Kruskal, \
    DFS,\
    BFSModificado,\
    SPFA, \
    TopologicalSort, \
    PrimMST


def ejecutar_algoritmo(nombre, matrices_adyacencias):
    if nombre == 'dijkstra':
        return Dijkstra.ejecutar(matrices_adyacencias)
    elif nombre == 'prim':
        return Prim.ejecutar(matrices_adyacencias)
    elif nombre == 'astar':
        return AStar.ejecutar(matrices_adyacencias)
    elif nombre == 'bfs':
        return BFS.ejecutar(matrices_adyacencias)
    elif nombre == 'dijkstra_cola':
        return DijkstraColaPrioridad.ejecutar(matrices_adyacencias)
    elif nombre == 'floyd_warshall':
        return FloydWarshall.ejecutar(matrices_adyacencias)
    elif nombre == 'bellmanford':
        return BellmanFord.ejecutar(matrices_adyacencias)
    elif nombre == 'kruskal':
        return Kruskal.ejecutar(matrices_adyacencias)
    elif nombre == 'dfs':
        return DFS.ejecutar(matrices_adyacencias)
    elif nombre == 'bfs_modificado':
        return BFSModificado.ejecutar(matrices_adyacencias)
    elif nombre == 'SPFA':
        return SPFA.ejecutar(matrices_adyacencias)
    elif nombre == 'topological_sort':
        return TopologicalSort.ejecutar(matrices_adyacencias)
    elif nombre == 'prim_mst':
        return PrimMST.ejecutar(matrices_adyacencias)
    return


def obtener_matrices_adyacencias():
# cantidades_nodos = [512, 1024, 2048, 3096]
    cantidades_nodos = [50, 100, 150, 500]
    matrices_adyacencias = []
    for nodos in cantidades_nodos:
        # Generar un grafo aleatorio con n nodos y aristas con pesos aleatorios
        random_graph = nx.erdos_renyi_graph(nodos, 0.4)
        edges = random_graph.edges()
        for edge in edges:
            # Pesos aleatorios entre 1 y 200
            random_graph[edge[0]][edge[1]]['weight'] = np.random.randint(1, 200)
        # Convertir el grafo a una matriz de adyacencia
        matriz_adyacencias = nx.to_numpy_array(random_graph)
        matrices_adyacencias.append((matriz_adyacencias, nodos))
    return matrices_adyacencias


def ejecutar_algoritmos():
    algoritmos = ["dijkstra", "astar", "dijkstra_cola",
                   "bfs", "kruskal", "dfs", "prim", "SPFA", "topological_sort", "prim_mst", "bellmanford", "floyd_warshall"]
    ejecuciones = []
    matrices_adyacencias = obtener_matrices_adyacencias()
    cantidad_hilos = os.cpu_count()
    with ThreadPoolExecutor(max_workers=cantidad_hilos) as executor:
        futures = [executor.submit(ejecutar_algoritmo, nombre_algoritmo, matrices_adyacencias) for nombre_algoritmo in algoritmos]

        for future in futures:
            resultado = future.result()
            if resultado:
                ejecuciones.append(resultado)

    return ejecuciones
