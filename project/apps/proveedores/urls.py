from django.urls import path
from . import views

urlpatterns = [
    path("proveedores/", views.VerProveedores, name= "lista_de_proveedores"),

]
