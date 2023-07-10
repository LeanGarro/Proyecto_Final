from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from .views import Home

app_name = "Home"


urlpatterns = [
    path("", Home, name="Home"),

]

urlpatterns += staticfiles_urlpatterns()