from django import forms
from .models import ProductoModel


class ProductoForms(forms.ModelForm):
    class Meta:
        verbose_name= 'producto'
        verbose_name_plural= 'productos'
        model= ProductoModel
        fields= '__all__'
