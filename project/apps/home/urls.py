from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView


from .views import Home

app_name = "home"


urlpatterns = [
    path("", Home, name="home"),
    path("about/", TemplateView.as_view(template_name="home/about.html"), name="about"),

]

urlpatterns += staticfiles_urlpatterns()