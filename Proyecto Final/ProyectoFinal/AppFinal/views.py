from django.shortcuts import render
from AppFinal.models import *
from django.http import HttpResponse
from AppFinal.forms import *
# Create your views here.

def inicio(request):
    
    return render(request, "AppFinal/inicio.html" )

def categoria(request):
    
    return render(request, "AppFinal/categoria.html" )

def cines(request):
    
    return render(request, "AppFinal/cines.html" )

def peliculas(request):
    
    return render(request, "AppFinal/peliculas.html" )

def formulario1(request):

    if request.method=="POST":

        formulario1 = FormularioPeliculas(request.POST)
        
        if formulario1.is_valid():

            info = formulario1.cleaned_data

            peliF = Peliculas(nombre=info["nombre"], duracion=info["duracion"])

            peliF.save()

            return render(request, r"AppFinal/inicio.html")

    else:

        formulario1 = FormularioPeliculas()

    return render(request, "AppFinal/formularioPeli.html", {"form1":formulario1})




def busquedaPelis(request):

    return render(request, "AppFinal/buscarPelis.html")

def resultados(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        duracion = Peliculas.objects.filter(nombre__icontains=nombre)
        
        return render(request, "AppFinal/resultados.html", {"nombre":nombre, "duracion":duracion})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)