from grafos.algoritmos.Algoritmo import Algoritmo
import time


def minKey(key, mstSet):
    min_val = float('inf')
    min_index = -1

    for v in range(len(key)):
        if key[v] < min_val and not mstSet[v]:
            min_val = key[v]
            min_index = v

    return min_index

def primMST(graph):
    V = len(graph)
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V

    key[0] = 0
    parent[0] = -1

    for cout in range(V):
        u = minKey(key, mstSet)
        mstSet[u] = True

        for v in range(V):
            if 0 < graph[u][v] < key[v] and not mstSet[v]:
                key[v] = graph[u][v]
                parent[v] = u

    return graph


def ejecutar(matrices_adyacencias):
    ejecuciones = []
    for matriz_adyacencias, nodos, num_aristas in matrices_adyacencias:
        inicio = time.time()
        distancias = primMST(matriz_adyacencias)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        algoritmo = Algoritmo("Prim MST", tiempo_ejecucion, nodos, matriz_adyacencias, distancias, num_aristas)
        ejecuciones.append(algoritmo)
    return ejecuciones, 'Prim MST'
