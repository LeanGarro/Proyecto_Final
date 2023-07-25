from django.db import models

# Create your models here.

class ProductoModel(models.Model):
    nombre= models.CharField(max_length=250, blank=False, null=False, unique= True)
    marca= models.CharField(max_length=250, blank=False, null=False,)
    proveedor= models.CharField(max_length=250, blank=False, null=False,)
    precio= models.DecimalField(max_digits=10, decimal_places=2, default=0,)
    descripcion= models.TextField(max_length=250, blank=True, null=True,)
    imagen= models.ImageField(upload_to= "img_producto", blank= True, null= True)

    def __str__(self) -> str:
        return f"{self.nombre} | marca: {self.marca} | precio: {self.precio}"