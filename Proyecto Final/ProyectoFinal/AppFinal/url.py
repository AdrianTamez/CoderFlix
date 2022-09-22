from django.urls import path 
from AppFinal.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('categoria', categoria, name="Categorias"),
    path('cines', cines, name="Cines"),
    path('peliculas', peliculas, name="Peliculas"),
    path('agregarPeliculas', formulario1 ,name="agregarPeliculas"),
    path('resultados/', resultados ,name="resultadosBusqueda"),
    path('busquedaPelis/', busquedaPelis ,name="buscarPelis"),
    
    
    
]