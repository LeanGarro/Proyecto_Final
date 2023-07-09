from django.db import models

# Create your models here.
class paises(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=56)

class sexos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, primary_key=True)



class usuario_register(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    usuario = models.CharField(max_length=15)
    possword = models.CharField(max_length=25)
    pais = models.ForeignKey(paises, null=False, blank=False, on_delete=models.SET_NULL)
    sexo = models.ForeignKey(sexos, null=False, blank=False, on_delete=models.SET_NULL)
