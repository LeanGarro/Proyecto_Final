from django.urls import path
from . import views

app_name = "apps.productos"

urlpatterns = [
    path("productos/", views.VerProductos, name= "lista_de_productos"),
    path("productos/created/", views.ProductoCreated, name= "CreatedProducto"),
    path("productos/delete/<NameProducto>/", views.ProductoDelete, name= "DeleteProducto"),
    path("productos/update/<NameProducto>/", views.ProductoUpdate, name= "UpdateProducto"),
    path("buscar/", views.Search),
    path("buscarproducto/", views.ProductoSearch, name= "SearchProducto"),
    
]