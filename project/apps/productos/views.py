from django.shortcuts import render
from . import models
from . import forms

# Create your views here.

def VerProductos(request):
    productos= models.ProductoModel.objects.all()
    context= {"object_list": productos}
    return render(request, "productos/productos_show.html", context)

def ProductoDelete(request, NameProducto):
    product= models.ProductoModel.objects.get(nombre= NameProducto)
    product.delete()
    
    products= models.ProductoModel.objects.all()
    context= {"object_list": products}
    
    return render(request, "productos/productos_show.html", context)

def ProductoUpdate(request, NameProducto):
    product= models.ProductoModel.objects.get(nombre= NameProducto)
    
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

def ProductoCreated(request):
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
    """
    productos= models.ProductoModel.objects.get(nombre= NameProducto)
    context= {"product": productos}
    return render(request, "productos/DetailProducto.html", context) 
    """
    producto= forms.ProductoModel.objects.get(nombre= NameProducto)
    
    form= forms.ProductoForms(initial={'nombre': producto.nombre, 'marca': producto.marca, 'proveedor': producto.proveedor,
        'precio': producto.precio, 'descripcion': producto.descripcion, 'imagen': producto.imagen})
        
    return render(request, "productos/DetailProducto.html", {"form_detail": form})
    