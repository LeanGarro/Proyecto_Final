from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_title= "usuarios Registros"

@admin.register(models.UsuarioReserva)
class ProductoModelAdmin(admin.ModelAdmin):
    list_display= ("atendido_r", "nombre_r", "apellido_r", "problemas_r",)
    list_filter= ("atendido_r",)
    search_fields= ("atendido_r", "problemas_r",)
    ordering= ("atendido_r",)



@admin.register(models.UserCustom)
class UserCustomAdmin(admin.ModelAdmin):
    list_display= ("user", "avatar")
    list_filter= ("user",)
    search_fields= ("user",)
