from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.register.models import UserCustom
# Create your views here.

def Home(request):
    return render(request, "home/index.html")

@login_required
def Perfil(request):
    try:
        user_custom = UserCustom.objects.get(user=request.user)
        context= {"CustomUser": user_custom}
    except UserCustom.DoesNotExist:
        context= {"CustomUser": None}
    return render(request, "home/perfil.html", context)

def NavBar(request):
    try:
        user_custom = UserCustom.objects.get(user=request.user)
        context= {"CustomUser": user_custom}
    except UserCustom.DoesNotExist:
        context= {"CustomUser": None}
    return render(request, "home/nav_var.html", context)