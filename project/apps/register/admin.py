from django.contrib import admin
from . import models

# Register your models here.
#admin.site.register(models.UsuarioReserva)

@admin.register(models.UsuarioReserva)
class ProductoModelAdmin(admin.ModelAdmin):
    list_display= ("atendido_r", "nombre_r", "apellido_r", "problemas_r",)
    list_filter= ("atendido_r",)
    search_fields= ("atendido_r", "problemas_r",)
    ordering= ("atendido_r",)