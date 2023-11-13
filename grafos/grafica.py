import base64
from io import BytesIO

import networkx as nx
import matplotlib.pyplot as plt


def obtener_imagen_grafo(matriz_adyacencias):
    # Crear un grafo dirigido desde las aristas
    grafo = nx.DiGraph(matriz_adyacencias)

    # Dibujar el grafo en un objeto BytesIO
    buf = BytesIO()
    # Establece el tamaño de la figura
    plt.figure(figsize=(14, 12))
    nx.draw(grafo, with_labels=True, node_color='lightblue', node_size=200, font_size=12, arrows=True)
    # Guarda la figura en el objeto BytesIO en formato PNG
    plt.savefig(buf, format="png")
    # Establece el puntero del objeto BytesIO al principio del archivo
    buf.seek(0)

    # Convierte la imagen a base64
    imagen_base64 = base64.b64encode(buf.read()).decode("utf-8")

    return imagen_base64
