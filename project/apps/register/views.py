from django.shortcuts import render
#from .models import usuario_register

# Create your views here.
name = "Register"

def register(request):
    return render(request, "register/register.html")

def login(request):
    return render(request, "register/login.html")





