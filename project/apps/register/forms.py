from django import forms
from .models import UsuarioRegister, UsuarioReserva

class UsuarioForms(forms.ModelForm):
    class Meta:
        model = UsuarioRegister
        fields= '__all__'

class ReservaForms(forms.ModelForm):
    class Meta:
        model= UsuarioReserva
        fields= ["nombre_r", "apellido_r", "dni_r", "reserva_r", "problemas_r"]

