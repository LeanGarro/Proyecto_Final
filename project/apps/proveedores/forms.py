from django import forms
from . import models

class ProveedoresForm(forms.ModelForm):
        class Meta:
            verbose_name= 'Proveedor'
            verbose_name_plural= 'Proveedores'
            model= models.Proveedores
            fields= '__all__'
