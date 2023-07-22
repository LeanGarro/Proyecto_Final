from django import forms
from .models import UsuarioRegister, UsuarioReserva
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class UsuarioForms(forms.ModelForm):
    class Meta:
        model = UsuarioRegister
        fields= '__all__'

class ReservaForms(forms.ModelForm):
    class Meta:
        model= UsuarioReserva
        fields= ["nombre_r", "apellido_r", "dni_r", "reserva_r", "problemas_r"]
        
class CustomAutentificationUser(AuthenticationForm):
    class Meta:
        model= User
        fields= ["username", "password"]
        widgets= {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }
        
class CustomUserRegisterForm(UserCreationForm):
    email= forms.EmailField(label= "email(opcionl)",required=False)
    password1= forms.CharField(label= "Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields= ["username","email","password1", "password2"]
        help_text= {k: "" for k in fields}
        widgets= {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }
