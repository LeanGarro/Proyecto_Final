"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.register.views import Login, register, formulario_reservar
from apps.productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("register/", register),
    path("login/", Login),
    path("reservas/", formulario_reservar),
    path("reservado/", formulario_reservar),
    path("productos/", views.VerProductos),
    path("productos/detail/<NameProducto>/", views.ProductoDetail, name= "DetailProducto"),
    path("productos/created/", views.ProductoCreated, name= "CreatedProducto"),
    path("productos/delete/<NameProducto>/", views.ProductoDelete, name= "DeleteProducto"),
    path("productos/update/<NameProducto>/", views.ProductoUpdate, name= "UpdateProducto"),
    
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
