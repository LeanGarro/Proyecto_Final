from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import Home

app_name = "home"


urlpatterns = [
    path("", Home, name="home"),

]

urlpatterns += staticfiles_urlpatterns()