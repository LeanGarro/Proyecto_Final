from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name='apps.register'

urlpatterns = [
    path("register/", views.register, name= "Register"),
    path("login/", views.Login, name= "Login"),
    path("reservas/", views.formulario_reservar, name= "Reservar"),
    path("reservado/", views.formulario_reservar, name= "Reservado"),
    path("update/avatar/", views.avatares, name= "UpdateAvatar"),
    path("update/newavatar/", views.AvatarNew, name= "UpdateNewAvatar"),
    path("update/user/", views.UserUpdate, name= "UpdateUser"),

]

urlpatterns += staticfiles_urlpatterns()