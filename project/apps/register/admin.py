from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(paises)
admin.site.register(sexos)
admin.site.register(UsuarioRegister)
admin.site.register(UsuarioReserva)