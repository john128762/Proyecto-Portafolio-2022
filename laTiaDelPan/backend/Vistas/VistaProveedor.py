from django.shortcuts import render
from backend import models
from backend import modelsApp
from backend.Controladores import MantenedorProveedores
from django.http import HttpResponseRedirect

def proveedor(request):
    dataP = models.Proveedor.objects.all()
    prov = {'proveedorT':dataP}
    return render(request, 'proveedor.html', prov)

def nuevoProv(request):
    if request.method=='POST':
        rutProv = request.POST["rutProveedor"]
        nombreProv = request.POST["nombreProveedor"]
        contactoProv = request.POST["contactoProveedor"]

        proveedor = modelsApp.Proveedor()
        proveedor.RUT = rutProv
        proveedor.Nombre = nombreProv
        proveedor.Contacto = contactoProv
        MantenedorProveedores.MantenedorProveedores.AgregarProveedor(proveedor)
        
        return HttpResponseRedirect('/proveedor/')