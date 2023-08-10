from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


def VerProveedores(request):
    """ esta funcion muestra todos los proveedores gracias al for ubidado en el HTML el cual trabaja con los datos que le pasa esta funcion """
    Proveedores= models.Proveedores.objects.all()
    context= {"proveedores_list": Proveedores}
    return render(request, "proveedores/ProveedoresShow.html", context)

@login_required
def DeleteProveedores(request, IdProveedor):
    """ ests funcion elimina a el proveedor seleccionado en el HTML """
    proveedor= models.Proveedores.objects.get(id= IdProveedor)
    proveedor.delete()
    
    Proveedores= models.Proveedores.objects.all()
    context= {"proveedores_list": Proveedores}
    return render(request, "proveedores/ProveedoresShow.html", context)

@login_required
def UpdateProveedores(request, NameProveedor):
    """ esta funcion actualiza a el proveedor seleccionado en el HTML gracias a un formulario """
    proveedor= models.Proveedores.objects.get(nombre= NameProveedor)
    
    if request.method == "POST" :
        form= forms.ProveedoresForm(request.POST, request.FILES)
        
        
        if form.is_valid():
            info= form.cleaned_data
            proveedor.nombre= info['nombre']
            proveedor.apellidos= info['apellidos']
            proveedor.email= info['email']
            proveedor.empresa= info['empresa']
            proveedor.descripcion= info['descripcion']
            proveedor.imagen= info['imagen']
            
            proveedor.save()
            return render(request, "home/index.html")          
    else:
        
        form= forms.ProveedoresForm(initial={'nombre': proveedor.nombre, 'apellidos': proveedor.apellidos, 'email': proveedor.email,
        'empresa': proveedor.empresa, 'descripcion': proveedor.descripcion, 'imagen': proveedor.imagen})
    
    return render(request, "proveedores/UpdateProveedores.html", {"form_provedores": form, "NameProducto": NameProveedor})

@login_required
def CreatedProveedores(request):
    if request.method == "POST":
        form= forms.ProveedoresForm(request.POST, request.FILES)
        
        if form.is_valid():
            info= form.cleaned_data
            form.save()
            
            return render(request, "home/index.html")
    else:
        form= forms.ProveedoresForm()
        
    return render(request, "proveedores/CreatedProveedores.html", {"form_created_provedores": form})

def SearchBar(request):
    return render(request, "proveedores/SearchBar.html")

def SearchProveedores(request):
    """ esta funcion busca un Proveedor en especifico en la DB y lo muestra en el HTML """
    if request.GET["BuscarProveedores"]:
        buscar= request.GET["BuscarProveedores"]
        proveedores= models.Proveedores.objects.filter(nombre__icontains= buscar)
        context= {"BusquedaProveedores": proveedores, "buscar":buscar}
        return render(request, "proveedores/SearchProveedores.html", context)
    else:
        return render(request, "proveedores/ProveedoresShow.html")