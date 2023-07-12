from django.urls import path
from . import views

urlpatterns = [
    path("registrado/", views.formulario_registro),
    path("reservado/", views.formulario_reservar)
]