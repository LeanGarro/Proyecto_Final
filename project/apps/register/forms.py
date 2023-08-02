from django import forms
from .models import UsuarioReserva
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class ReservaForms(forms.ModelForm):
    class Meta:
        model= UsuarioReserva
        fields= ["nombre_r", "apellido_r", "dni_r", "reserva_r", "problemas_r"]
        
class CustomAutentificationUser(AuthenticationForm):
    class Meta:
        model= User
        fields= ["username", "password"]
        widgets= {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder":"User"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder":"Password"}),
        }
        
class CustomUserRegisterForm(UserCreationForm):
    class Meta:
        model= User
        fields= ["first_name","last_name","email","username"]
        help_text= {k: "" for k in fields}
        widgets= {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder":"Nombre"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder":"Apellido"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder":"Email"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder":"Nombre de usuario"}),
            #"password2": forms.PasswordInput(attrs={"class": "form-control m-1", "placeholder":"Contraseña",}),
            #"password1": forms.PasswordInput(attrs={"class": "form-control m-1", "placeholder":"Contraseña"}),

        }
