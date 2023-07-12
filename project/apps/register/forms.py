from django import forms
from .models import usuario_register

class usuario_forms(forms.ModelForm):
    class Meta:
        model = usuario_register
        fields= '__all__'


