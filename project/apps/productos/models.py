from django.db import models
from proveedores.models import Proveedores
# Create your models here.

class ProductoModel(models.Model):
    nombre= models.CharField(max_length=250, blank=False, null=False)
    marca= models.CharField(max_length=250, blank=False, null=False,)
    #Proveedore= models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    proveedor= models.CharField(max_length=250, blank=False, null=False,)
    precio= models.DecimalField(max_digits=10, decimal_places=2, default=0,)
    descripcion= models.TextField(max_length=250, blank=True, null=True,)
    imagen= models.ImageField(upload_to= "img_producto", blank= False, null= False)

    def __str__(self) -> str:
        return f"{self.nombre} | marca: {self.marca} | precio: {self.precio}"