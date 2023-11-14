class Algoritmo:
    def __init__(self, nombre, tiempo_ejecucion, nodos, matriz_adyacencias, distancias, num_aristas, grafo_imagen_b64=None):
        self.nombre = nombre
        self.tiempo_ejecucion = tiempo_ejecucion
        self.matriz_adyacencias = matriz_adyacencias
        self.distancias = distancias
        self.nodos = nodos
        self.aristas = num_aristas
        self.grafo_imagen_b64 = grafo_imagen_b64
