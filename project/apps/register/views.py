from django.shortcuts import render
from .models import usuario_register
from.forms import usuario_forms, reserva_forms, usuario_reserva

# Create your views here.
name = "register"

def reservar(request):
    return render(request, "register/reservar.html")

def registrado(request):
    return render(request, "register/registrado.html")

def login(request):
    return render(request, "register/login.html")

def reservado(request):
    return render(request, "register/reservado.html")

def formulario_registro(request):
    if request.method == "POST":
        formulario_register = usuario_forms(request.POST)
        
        if formulario_register.is_valid():
            info = formulario_register.cleaned_data
            registro = usuario_register(nombre= info['nombre'], apellido = info['apellido'], nacimiento = info['nacimiento'], usuario = info['usuario'], possword = info['possword'], pais = info['pais'], sexo = info['sexo'])          

            registro.save()
            
            return render(request, 'home/index.html')
    
    else:
        formulario_register = usuario_forms()
    
    return render(request, 'register/register.html', {"formulario_register": formulario_register})

def formulario_reservar(request):
    if request.method == "POST":
        formulario_reservar = reserva_forms(request.POST)
    
        if formulario_reservar.is_valid():
            info = formulario_reservar.cleaned_data
            registro = usuario_reserva(nombre= info['nombre'], apellido = info['apellido'], dni = info['dni'], resrva = info['reserva'], problemas = info['problemas'])          

            registro.save()
            return render(request, 'register/reservado.html')
    
    else: 
        formulario_reservar = reserva_forms()
    
    return render(request, 'register/reservar.html', {"formulario_reservar": formulario_reservar})




