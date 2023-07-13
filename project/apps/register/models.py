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


class UsuarioRegister(models.Model):
    nombre = models.CharField(max_length=40, blank=False, null=False)
    apellido = models.CharField(max_length=40, blank=False, null=False)
    nacimiento = models.DateField(blank=False, null=True)
    usuario = models.CharField(max_length=15, blank=False, null=False)
    possword = models.CharField(max_length=25)
    pais = models.ForeignKey(paises, on_delete=models.CASCADE, blank=False, null=False)
    sexo = models.ForeignKey(sexos, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self):
        return f"id: {self.id} | {self.nombre} {self.apellido}"
    
class UsuarioReserva(models.Model):
    atendido_r = models.BooleanField(default=False, verbose_name='atendido?')
    nombre_r = models.CharField(max_length=40, blank=False, null=False, default="ponga su nombre", verbose_name='nombre')
    apellido_r = models.CharField(max_length=40, blank=False, null=False,default="ponga su apellido", verbose_name='apellido')
    dni_r = models.CharField(max_length=12, blank=False, null=False,default="ponga su DNI", verbose_name='DNI' )
    reserva_r = models.DateField(blank=False, null=False,default="7/7/2007", verbose_name='reserva')
    problemas_r = models.TextField(max_length=250, blank=False, null=False, default='ponga su problema', verbose_name='describir problemas')
    
    def __str__(self) -> str:
        return f"atendido: {self.atendido_r} | {self.nombre_r} {self.apellido_r}"
    
