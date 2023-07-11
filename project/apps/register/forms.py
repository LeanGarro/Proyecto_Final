from django import forms
from .models import usuario_register
from django.shortcuts import render

class usuario_forms(forms.ModelForm):
    class Meta:
        model = usuario_register
        fields= []
        
    nombre = forms.CharField()
    apellido = forms.CharField()
    nacimiento = forms.DateField()
    usuario = forms.CharField()
    possword = forms.CharField()
    pais = forms.CharField()
    sexo = forms.CharField()



def formulario_registro(request):
    if request.method == "POST":
        formulario_register = usuario_forms(request.POST)
        
        if formulario_register.is_valid():
            info = formulario_register.cleaned_data
            registro = usuario_register(nombre= info['nombre'], apellido = info['apellido'], nacimiento = info['nacimiento'], usuario = info['usuario'], possword = info['possword'], pais = info['pais'], sexo = info['sexo'])          

            registro.save()
            
            return render(request, 'project/apps/Home/templates/home/index.html')
    
    else:
        
        formulario_register = usuario_forms()
    
    return render(request, "project/apps/Register/templates/register/register.html", {"formulario_register": formulario_register})