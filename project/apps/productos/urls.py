from django.urls import path
from . import views

name = "apps.productos"

urlpatterns = [
    path("productos/", views.VerProductos, name= "lista_de_productos"),


]