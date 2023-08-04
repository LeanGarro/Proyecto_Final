from django.shortcuts import render
from . import models


def VerProveedores(request):
    Proveedores= models.Proveedores.objects.all()
    context= {"proveedores_list": Proveedores}
    return render(request, "proveedores/proveedores_show.html", context)
