from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductoModel
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.


def VerProductos(request):
    """ la funcionalidad de esta vista es mostrar todos los productos gracias al for ubidado en el HTML el cual trabaja con los datos que le pasa esta funcion """
    productos= ProductoModel.objects.all()
    context= {"object_list": productos}
    return render(request, "productos/productos_show.html", context)

@login_required
def ProductoDelete(request, NameProducto):
    """ esta funcion elimina a el producto seleccionado en el HTML """
    product= ProductoModel.objects.get(nombre= NameProducto)
    product.delete()
    
    products= ProductoModel.objects.all()
    context= {"object_list": products}
    
    return render(request, "productos/productos_show.html", context)

@login_required
def ProductoUpdate(request, NameProducto):
    """ esta funcion actualiza a el producto seleccionado en el HTML gracias a un formulario """
    product= ProductoModel.objects.get(nombre= NameProducto)
    
    if request.method == "POST":
        form= forms.ProductoForms(request.POST, request.FILES)
        
        if form.is_valid():
            info= form.cleaned_data
            
            product.nombre= info['nombre']
            product.marca= info['marca']
            product.proveedor= info['proveedor']
            product.precio= info['precio']
            product.descripcion= info['descripcion']
            product.imagen= info['imagen']
            
            product.save()
            return render(request, "home/index.html")
    else:
        form= forms.ProductoForms(initial={'nombre': product.nombre, 'marca': product.marca, 'proveedor': product.proveedor,
        'precio': product.precio, 'descripcion': product.descripcion, 'imagen': product.imagen})
    
    return render(request, "productos/EditarProducto.html", {"form_edit": form, "NameProducto": NameProducto})

@login_required
def ProductoCreated(request):
    """ esta funcion crea un producto nuevo gracias a un formulario """
    if request.method == "POST":
        form= forms.ProductoForms(request.POST, request.FILES)
        
        if form.is_valid():
            info= form.cleaned_data
            form.save()
            
            return render(request, "home/index.html")
    else:
        form= forms.ProductoForms()
        
    return render(request, "productos/CreatedProducto.html", {"form_created": form})

def ProductoDetail(request, NameProducto):
    producto= ProductoModel.objects.get(nombre= NameProducto)
    
    form= forms.ProductoForms(initial={'nombre': producto.nombre, 'marca': producto.marca, 'proveedor': producto.proveedor,
        'precio': producto.precio, 'descripcion': producto.descripcion, 'imagen': producto.imagen})
        
    return render(request, "productos/DetailProducto.html", {"form_detail": form})

def ProductoSearch(request):
    """ esta funcion muestra la barra de busqueda en el HTML """
    return render(request, "productos/SearchProducto.html")

def Search(request):
    """ esta funcion busca un producto en especifico en la DB y lo muestra en el HTML """
    if request.GET["BuscarProductos"]:
        buscar= request.GET["BuscarProductos"]
        productos= ProductoModel.objects.filter(nombre__icontains= buscar)
        context= {"BusquedaProductos": productos, "buscar":buscar}
        return render(request, "productos/resultado.html", context)
    else:
        return render(request, "productos/productos_show.html")