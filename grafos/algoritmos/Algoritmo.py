class Algoritmo:
    def __init__(self, nombre, tiempo_ejecucion, nodos, matriz_adyacencias, distancias, grafo_imagen_b64=None):
        self.nombre = nombre
        self.tiempo_ejecucion = tiempo_ejecucion
        self.matriz_adyacencias = matriz_adyacencias
        self.distancias = distancias
        self.nodos = nodos
        self.grafo_imagen_b64 = grafo_imagen_b64
