from django import forms
from .models import ProductoModel


class ProductoForms(forms.ModelForm):
    class Meta:
        model= ProductoModel
        fields= '__all__'
