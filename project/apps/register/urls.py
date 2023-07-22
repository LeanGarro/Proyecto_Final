from django.urls import path
from . import views

urlpatterns = [
    path("reservado/", views.formulario_reservar)
]