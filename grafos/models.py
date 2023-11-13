from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Grafo(models.Model):
    nombre = models.CharField(max_length=255)
    tiempo_ejecucion = models.FloatField()
    nodos = models.IntegerField()
    matriz_adyacencias = models.TextField()
    distancias = models.TextField()
    grafo_imagen_b64 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class UsuarioGrafo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    grafo = models.ForeignKey('Grafo', on_delete=models.CASCADE)
    grafica_tiempos = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.usuario.username} - {self.grafo.nombre}'
