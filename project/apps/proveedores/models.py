from django.db import models

# Create your models here.

class Proveedores(models.Model):
    nombre= models.CharField(max_length=250, blank=False, null=True)
    apellidos= models.CharField(max_length=250, blank=True, null=False)
    email= models.EmailField(blank=False, null=False)
    empresa= models.CharField(max_length=250, blank=False, null=False,)
    descripcion= models.TextField(blank=True, null=True,)
    imagen= models.ImageField(upload_to= "img_producto", blank= False, null= False)
    
    def __str__(self) -> str:
        return f"{self.nombre} | {self.empresa}"