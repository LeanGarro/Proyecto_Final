from django.db import models

# Create your models here.

class ProductoModel(models.Model):
    nombre= models.CharField(max_length=250, blank=False, null=False,)
    marca= models.CharField(max_length=250, blank=False, null=False,)
    proveedor= models.CharField(max_length=250, blank=False, null=False,)
    descripcion= models.TextField(max_length=250, blank=True, null=True,)
    imagen= models.ImageField(upload_to= "img_producto", blank= True, null= True)