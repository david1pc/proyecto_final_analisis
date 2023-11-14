import base64
from io import BytesIO

from matplotlib import pyplot as plt

from .algoritmos import Ejecucion

from django.utils import timezone
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import login, authenticate, logout
from .models import Grafo, UsuarioGrafo

# Importar estos módulos para manejar las operaciones de Matplotlib en el hilo principal
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

matplotlib.use('Agg')


def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        correo = request.POST['correo']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        contrasena = request.POST['contrasena']

        try:
            # Crea un nuevo usuario utilizando create_user para manejar contraseñas seguras
            usuario = User.objects.create_user(username=username, email=correo, password=contrasena, first_name=nombre, last_name=apellido)
            # Redirige a alguna página de éxito o inicio de sesión
            return render(request, 'registro.html', {"exito": "Se ha registrado con éxito."})

        except IntegrityError as e:
            if 'unique constraint' in str(e):
                # Maneja errores de integridad, como correo o username duplicados
                if User.objects.filter(email=correo).exists():
                    return render(request, 'registro.html', {"error": "El correo ya se encuentra en uso por otro usuario."})
                elif User.objects.filter(username=username).exists():
                    return render(request, 'registro.html', {"error": "El username ya se encuentra en uso por otro usuario."})
            else:
                # Maneja otros errores de integridad que no sean por correo o username duplicados
                return render(request, 'registro.html', {"error": "Ha ocurrido un error al registrarse. Vuelva a intentar."})

    return render(request, 'registro.html')


def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        contrasena = request.POST['contrasena']

        # Verifica las credenciales del usuario
        usuario = authenticate(request, username=username, password=contrasena)

        if usuario is not None:
            # Usuario autenticado, inicia la sesión
            login(request, usuario)
            # Redirige a alguna página de éxito o dashboard
            return redirect('dashboard')
        else:
            # Usuario no encontrado o contraseña incorrecta, muestra un mensaje de error
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})

    return render(request, 'login.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')


def index(request):
    return render(request, 'index.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def ejecutar_algoritmos(request):
    try:
        ejecuciones = Ejecucion.ejecutar_algoritmos()
    except Exception:
        return ejecutar_algoritmos(request)

    usuario_actual = request.user
    fecha_creacion = timezone.now()

    tiempos_por_algoritmo = {}

    for algoritmos, nombre_algoritmo in ejecuciones:
        for algoritmo in algoritmos:
            # Almacenar los tiempos de ejecución por algoritmo
            if nombre_algoritmo not in tiempos_por_algoritmo:
                tiempos_por_algoritmo[nombre_algoritmo] = []
            tiempos_por_algoritmo[nombre_algoritmo].append(algoritmo.tiempo_ejecucion)

    # Crear el gráfico de barras
    nombres_algoritmos = list(tiempos_por_algoritmo.keys())
    tiempos_totales = [sum(tiempos) for tiempos in tiempos_por_algoritmo.values()]

    # Configurar Matplotlib para el modo interactivo
    plt.ion()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(nombres_algoritmos, tiempos_totales)
    ax.set_xlabel('Algoritmos')
    ax.set_ylabel('Tiempo total de ejecución (ms)')
    ax.set_title('Tiempo total de ejecución de algoritmos')

    # Rotar y ajustar el tamaño de las etiquetas
    ax.tick_params(axis='x', labelsize=6)

    # Convertir el gráfico a una imagen para mostrar en la plantilla
    img_data = BytesIO()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(img_data)
    img_data.seek(0)
    img_base64 = base64.b64encode(img_data.read()).decode()

    plt.ioff()

    plt.close()

    for algoritmos, nombre_algoritmo in ejecuciones:
        for algoritmo in algoritmos:
            grafo = Grafo(
                nombre=algoritmo.nombre,
                tiempo_ejecucion=algoritmo.tiempo_ejecucion,
                nodos=algoritmo.nodos,
                matriz_adyacencias=algoritmo.matriz_adyacencias,
                distancias=algoritmo.distancias,
                aristas=algoritmo.aristas,
                grafo_imagen_b64=None
            )
            grafo.save()

            usuario_grafo = UsuarioGrafo(usuario=usuario_actual, grafo=grafo, fecha_creacion=fecha_creacion, grafica_tiempos=img_base64)
            usuario_grafo.save()

    return render(request, 'algoritmo.html', {'ejecuciones': ejecuciones, 'grafica_tiempos': img_base64})


@login_required
def ver_historial(request):
    usuario_actual = request.user
    resultados = UsuarioGrafo.objects.filter(usuario=usuario_actual).values(
        'fecha_creacion',
        'grafo__nombre',
        'grafo__tiempo_ejecucion',
        'grafo__nodos',
        'grafo__matriz_adyacencias',
        'grafo__distancias',
        'grafo__aristas',
        'grafo__grafo_imagen_b64',
        'grafica_tiempos'
    )
    grafos_por_fecha = {}
    for resultado in resultados:
        fecha_creacion = resultado['fecha_creacion']
        if fecha_creacion not in grafos_por_fecha:
            grafos_por_fecha[fecha_creacion] = []
        grafo_actual = {
            'nombre': resultado['grafo__nombre'],
            'tiempo_ejecucion': resultado['grafo__tiempo_ejecucion'],
            'nodos': resultado['grafo__nodos'],
            'matriz_adyacencias': resultado['grafo__matriz_adyacencias'],
            'distancias': resultado['grafo__distancias'],
            'aristas': resultado['grafo__aristas'],
            'grafo_imagen_b64': resultado['grafo__grafo_imagen_b64'],
            'grafica_tiempos': resultado['grafica_tiempos']
        }
        grafos_por_fecha[fecha_creacion].append(grafo_actual)

    lista_de_listas = [[fecha, grafos] for fecha, grafos in grafos_por_fecha.items()]

    return render(request, 'historial.html', {'resultados': lista_de_listas})
