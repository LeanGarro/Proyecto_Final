from django.db import models

name = "Register"
#Create your models here.
class paises(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=56, blank=False, null=False)

class sexos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)



class usuario_register(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False, null=False)
    apellido = models.CharField(max_length=40, blank=False, null=False)
    usuario = models.CharField(max_length=15, blank=False, null=False)
    possword = models.CharField(max_length=25)
    pais = models.ForeignKey(paises, null=False, blank=False, on_delete=models.CASCADE)
    sexo = models.ForeignKey(sexos, null=False, blank=False, on_delete=models.CASCADE)
    nacimiento = models.DateTimeField(auto_now_add=True)
