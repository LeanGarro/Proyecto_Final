from django import forms
from .models import UsuarioRegister, UsuarioReserva
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class UsuarioForms(forms.ModelForm):
    class Meta:
        model = UsuarioRegister
        fields= '__all__'

class ReservaForms(forms.ModelForm):
    class Meta:
        model= UsuarioReserva
        fields= ["nombre_r", "apellido_r", "dni_r", "reserva_r", "problemas_r"]
        
class AutentificationUser(AuthenticationForm):
    class Meta:
        model= User
        fields= ["username", "password"]
        widgets= {
            "username": forms.TextInput(),
            "password": forms.PasswordInput(),
        }
        
