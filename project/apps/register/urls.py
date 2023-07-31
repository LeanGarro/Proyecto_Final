from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("reservado/", views.formulario_reservar)
]

urlpatterns += staticfiles_urlpatterns()