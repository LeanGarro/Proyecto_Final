from django.shortcuts import render
from.forms import ReservaForms, UsuarioReserva
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserRegisterForm, CustomAutentificationUser

# Create your views here.
name = "register"

def register(request):
    if request.method == "POST":
        print("paso el post")
        form= CustomUserRegisterForm(request.POST)
        if form.is_valid():
            print("paso el is valid")
            usuario= form.cleaned_data["username"]
            form.save()
            return render(request, "home/index.html", {"mensaje":"🥳te registraste correctamente🥳"})
        else:
            return render(request, "home/index.html", {"mensaje": "Hubo un error"})
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