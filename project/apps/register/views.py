from django.shortcuts import render
from .models import UsuarioRegister
from.forms import UsuarioForms, ReservaForms, UsuarioReserva
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from . import forms

# Create your views here.
name = "register"

def login_home(request):
    return render(request, "register/login.html")

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
    if request.method == "POST":
        formulario_reservar = ReservaForms(request.POST)
        if formulario_reservar.is_valid(): 
            info = formulario_reservar.cleaned_data
            registro = UsuarioReserva(nombre_r= info['nombre_r'], apellido_r = info['apellido_r'], dni_r = info['dni_r'], reserva_r = info['reserva_r'], problemas_r = info['problemas_r'])   
            registro.save()

            return render(request, 'register/reservado.html')
    
    else: 
        formulario_reservar = ReservaForms()
        
    
    return render(request, 'register/reservar.html', {"form": formulario_reservar})

def Login(request):
    if request.method == "POST":
        
        form= AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            
            user_name= form.cleaned_data.get("username")
            contraseña= form.cleaned_data.get("password")
            
            user= authenticate(username= user_name, password= contraseña)
            if user is not None:
                login(request, user)
                return render(request, "home/index.html", {"mensaje":f"Bienvenido {user_name}"})
            else:
                return render(request, "home/index.html", {"mensaje":"Error, datos incorrectos"})          
        else:
            
            return render(request, "home/index.html", {"mensaje": "Error, formulario erroneo"})
    else:
        form= AuthenticationForm()
    
    return render(request, "register/login.html", {'form_login':form})