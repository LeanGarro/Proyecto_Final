from django import forms
from .models import usuario_register, usuario_reserva

class usuario_forms(forms.ModelForm):
    class Meta:
        model = usuario_register
        fields= '__all__'

class reserva_forms(forms.ModelForm):
    class Meta:
        model= usuario_reserva
        fields= '__all__'

