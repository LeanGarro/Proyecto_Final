from django.urls import path
from . import views

urlpatterns = [
    path("registrado/", views.registrado),
]