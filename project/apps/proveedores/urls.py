from django.urls import path
from . import views

app_name='apps.proveedores'

urlpatterns = [
    path("proveedores/", views.VerProveedores, name= "Proveedores"),
    path("proveedores/delete/<IdProveedor>/", views.DeleteProveedores, name="DeleteProveedores"),
    path("proveedores/update/<NameProveedor>/", views.UpdateProveedores, name="UpdateProveedores"),
    path("proveedores/create/", views.CreatedProveedores, name="CreatedProveedores"),
    path("proveedores/searchbar/", views.SearchBar, name="SearchBar"),
    path("proveedores/search/", views.SearchProveedores, name="SearchProveedores"),

]
