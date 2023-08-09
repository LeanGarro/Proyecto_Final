from django.db import models
from django.contrib.auth.models import User

    
class UsuarioReserva(models.Model):
    atendido_r = models.BooleanField(default=False, verbose_name='atendido?')
    nombre_r = models.CharField(max_length=40, blank=False, null=False, default="nombre", verbose_name='nombre')
    apellido_r = models.CharField(max_length=40, blank=False, null=False,default="apellido", verbose_name='apellido')
    dni_r = models.CharField(max_length=12, blank=False, null=False,default="DNI", verbose_name='DNI' )
    reserva_r = models.DateField(blank=False, null=False,default="7/7/2007", verbose_name='reserva')
    problemas_r = models.TextField(max_length=250, blank=False, null=False, default='mi problema es: ', verbose_name='describir problemas')
    
    def __str__(self) -> str:
        return f"atendido: {self.atendido_r} | {self.nombre_r} {self.apellido_r}"
    

class UserCustom(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="UserCustom")
    avatar= models.ImageField(upload_to= "avatar", blank= False, null= False)
