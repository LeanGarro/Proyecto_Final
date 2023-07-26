from django.shortcuts import render
from . import models

# Create your views here.

def VerProductos(request):
    productos= models.ProductoModel.objects.all()
    context= {"object_list": productos}
    return render(request, "productos/productos_show.html", context)
