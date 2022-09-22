from django.db import models

# Create your models here.

class Peliculas(models.Model):

    nombre=models.CharField(max_length=40)
    duracion= models.IntegerField()

class Cines(models.Model):

    nombre=models.CharField(max_length=40)
    ubicacion=models.CharField(max_length=40)

class Categoria(models.Model):

    category=models.CharField(max_length=40)