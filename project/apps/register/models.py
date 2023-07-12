from django.db import models


#Create your models here.
class paises(models.Model):
    nombre = models.CharField(max_length=56, blank=False, null=False)
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "paises"

class sexos(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "sexos"


class usuario_register(models.Model):
    nombre = models.CharField(max_length=40, blank=False, null=False)
    apellido = models.CharField(max_length=40, blank=False, null=False)
    nacimiento = models.DateField(blank=False, null=True)
    usuario = models.CharField(max_length=15, blank=False, null=False)
    possword = models.CharField(max_length=25)
    pais = models.ForeignKey(paises, on_delete=models.CASCADE, blank=False, null=False)
    sexo = models.ForeignKey(sexos, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self):
        return f"id: {self.id} | {self.nombre} {self.apellido}"
    
class usuario_reserva(models.Model):
    atendido = models.BooleanField(default=False)
    nombre = models.CharField(max_length=40, blank=False, null=False)
    apellido = models.CharField(max_length=40, blank=False, null=False)
    dni = models.IntegerField(blank=False, null=False)
    reserva = models.DateField(blank=False, null=False)
    problemas = models.TextField(max_length=250, blank=False, null=False)
    
    def __str__(self) -> str:
        return f"atendido: {self.atendido} | {self.nombre} {self.apellido}"
    
