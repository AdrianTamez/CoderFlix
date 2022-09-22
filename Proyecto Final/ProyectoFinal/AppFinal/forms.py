from django import forms

class FormularioPeliculas(forms.Form):

    nombre = forms.CharField()
    duracion = forms.IntegerField()