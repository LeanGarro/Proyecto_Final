from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.register.models import UserCustom
# Create your views here.

def Home(request):
    return render(request, "home/index.html")

@login_required
def Perfil(request):
    if UserCustom.objects.get(user=request.user) == None:
        context= {"CustomUser": UserCustom.objects.get(user=request.user)}
    else:
        context= {"CustomUser": "algo"}
    return render(request, "home/perfil.html", context)