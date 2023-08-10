from django.shortcuts import render
from .forms import ReservaForms, UsuarioReserva, UserCustomForm, UserCustom, CustomUserRegisterForm
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
            return render(request, "register/register.html", {"mensaje": "Hubo un error", 'form_register':form})
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
    user= UserCustom.objects.get(user= request.user)
    if request.method == "POST":
        
        form= UserCustomForm(request.POST, request.FILES)
        
        if form.is_valid():
            info= form.cleaned_data
            user.avatar= info['avatar']
            
            user.save()
            
            return render(request, "home/index.html")
        else:
            render(request, "register/perfil.html", {"mensaje":"algo salio mal, intentalo de nuevo"})
    else:
        form= UserCustomForm()
    
    return render(request, "register/UpdateAvatar.html", {"form_avatar":form})
  
  
def AvatarNew(request):
    if request.method == "POST":
        user= User.objects.get(username= request.user)
        form= UserCustomForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            info= form.cleaned_data
            avatar= UserCustom(user=user, avatar=form.cleaned_data['avatar'])
            avatar.save()
            
            return render(request, "home/index.html")
    else:
        form= UserCustomForm()
    
    return render(request, "register/UpdateAvatar.html", {"form_avatar":form})

def UserUpdate(request):
    """ esta funcion actualiza a el user gracias a un formulario """
    user= User.objects.get(username= request.user)
    
    if request.method == "POST":
        form= CustomUserRegisterForm(request.POST, request.FILES)
        
        if form.is_valid():
            info= form.cleaned_data
            
            user.first_name= info['first_name']
            user.last_name= info['last_name']
            user.email= info['email']
            user.username= info['username']

            user.save()
            return render(request, "home/index.html")
    else:
        form= CustomUserRegisterForm(initial={'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email,
        'username': user.username})
    
    return render(request, "register/UpdateUser.html", {"form_datos": form})