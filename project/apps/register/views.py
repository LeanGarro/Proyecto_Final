from django.shortcuts import render
from .models import UsuarioRegister
from.forms import UsuarioForms, ReservaForms, UsuarioReserva

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
        formulario_register = UsuarioForms(request.POST)
        if formulario_register.is_valid():
            info = formulario_register.cleaned_data
            registro = UsuarioRegister(nombre= info['nombre'], apellido = info['apellido'], nacimiento = info['nacimiento'], usuario = info['usuario'], possword = info['possword'], pais = info['pais'], sexo = info['sexo'])          

            registro.save()
            
            return render(request, 'home/index.html')
    
    else:
        formulario_register = UsuarioForms()
    
    return render(request, 'register/register.html', {"formulario_register": formulario_register})

def formulario_reservar(request):
    if request.method == "post":
        formulario_reservar = ReservaForms(request.POST)
        if formulario_reservar.is_valid(): 
            info = formulario_reservar.cleaned_data
            registro = UsuarioReserva(nombre_r= info['nombre_r'], apellido_r = info['apellido_r'], dni_r = info['dni_r'], reserva_r = info['reserva_r'], problemas_r = info['problemas_r'])   
            registro.save()

            return render(request, 'register/reservado.html')
    
    else: 
        formulario_reservar = ReservaForms()
    
    return render(request, 'register/reservar.html', {"form": formulario_reservar})

