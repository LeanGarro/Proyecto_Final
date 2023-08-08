from django.shortcuts import render
from.forms import ReservaForms, UsuarioReserva, UserCustomForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserRegisterForm, CustomAutentificationUser
from django.contrib.auth.models import User

from . import models

# Create your views here.
name = "register"

def register(request):
    if request.method == "POST":
        
        form= CustomUserRegisterForm(request.POST)
        
        if form.is_valid():
            usuario= form.cleaned_data["username"]
            form.save()
            
            return render(request, "home/index.html", {"mensaje":"🥳te registraste correctamente🥳"})
        else:
            return render(request, "register/register.html", {"mensaje": "Hubo un error"})
    else:
        form= CustomUserRegisterForm()

    return render(request, "register/register.html", {'form_register':form})

@login_required
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
        
        form= CustomAutentificationUser(request, data= request.POST)
        if form.is_valid():
            
            user_name= form.cleaned_data.get("username")
            contraseña= form.cleaned_data.get("password")
            
            user= authenticate(username= user_name, password= contraseña)
            if user is not None:
                login(request, user)
                return render(request, "home/index.html", {"mensaje":""})
            else:
                return render(request, "home/index.html", {"mensaje":"Error, datos incorrectos"})          
        else:
            
            return render(request, "home/index.html", {"mensaje": "Error, formulario erroneo"})
    else:
        form= CustomAutentificationUser()
    
    return render(request, "register/login.html", {'form_login':form})

@login_required
def avatares(request):    
    if request.method == "POST":
        form= UserCustomForm(request.POST, request.FILES)
        
        if form.is_valid():
            user= User.objects.get(username= request.user)            
            avatar= models.UserCustom(user= user, avatar= form.cleaned_data['avatar'])
            avatar.save()
            
            
            return render(request, "home/perfil.html")
        
    else:
        form= UserCustomForm()

    return render(request, "register/UpdateAvatar.html", {"form_avatar":form})
        

"""
def UpdateProveedores(request, NameProveedor):
    proveedor= models.Proveedores.objects.get(nombre= NameProveedor)
    
    if request.method == "POST" :
        form= forms.ProveedoresForm(request.POST, request.FILES)
        
        
        if form.is_valid():
            info= form.cleaned_data
            proveedor.nombre= info['nombre']
            proveedor.apellidos= info['apellidos']
            proveedor.email= info['email']
            proveedor.empresa= info['empresa']
            proveedor.descripcion= info['descripcion']
            proveedor.imagen= info['imagen']
            
            proveedor.save()
            return render(request, "home/index.html")          
    else:
        
        form= forms.ProveedoresForm(initial={'nombre': proveedor.nombre, 'apellidos': proveedor.apellidos, 'email': proveedor.email,
        'empresa': proveedor.empresa, 'descripcion': proveedor.descripcion, 'imagen': proveedor.imagen})
    
    return render(request, "proveedores/UpdateProveedores.html", {"form_provedores": form, "NameProducto": NameProveedor})


"""