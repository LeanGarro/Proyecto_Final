from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from apps.register.views import formulario_registro

from .views import Home

app_name = "home"


urlpatterns = [
    path("", Home, name="home"),

]

urlpatterns += staticfiles_urlpatterns()