from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import Home, Perfil, NavBar

app_name = "home"

urlpatterns = [
    path("", Home, name="home"),
    path("about/", TemplateView.as_view(template_name="home/about.html"), name= "about"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name= "logout"),
    path("perfil/", Perfil, name= "perfil"),
    path("aviso/", TemplateView.as_view(template_name="home/aviso_login.html"), name= "aviso"),
    path("navbar/", NavBar, name= "NavBar"),
]

urlpatterns += staticfiles_urlpatterns()
