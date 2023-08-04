from django.contrib import admin
from . import models

admin.site.site_title= "Proveedores"


@admin.register(models.Proveedores)
class ProductoModelAdmin(admin.ModelAdmin):
    list_display= ("nombre", "empresa")
    list_filter= ("nombre", "empresa")
    search_fields= ("nombre", "descripcion",)
    ordering= ("nombre",)
