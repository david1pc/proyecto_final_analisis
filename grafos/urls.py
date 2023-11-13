from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('algoritmo/', views.ejecutar_algoritmos, name='algoritmo'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('historial/', views.ver_historial, name='historial'),
    path('login/', views.inicio_sesion),
    path('registro/', views.registro),
    path('logout/', views.cerrar_sesion, name='logout')
]