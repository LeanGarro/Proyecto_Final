from django.contrib import admin
from . import models

admin.site.site_title= "Productos"


@admin.register(models.ProductoModel)
class ProductoModelAdmin(admin.ModelAdmin):
    list_display= ("nombre", "marca", "precio",)
    list_filter= ("nombre", "marca", "precio",)
    search_fields= ("nombre", "marca",)
    ordering= ("nombre",)