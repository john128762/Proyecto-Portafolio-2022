from django.shortcuts import render, redirect
from backend import models
from backend import modelsApp
from backend.Controladores.MantenedorProveedores import MantenedorProveedores
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
#import jsons


def proveedor(request, respuesta=None):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    list(messages.get_messages(request))
    dataP = MantenedorProveedores.ListarProveedores()
    if(isinstance(dataP, modelsApp.Resultado)):
        print(dataP.Mensaje)
    prov = {'proveedorT':dataP}
    if isinstance(respuesta, modelsApp.Resultado):
        if respuesta.CodigoOperacion == 200:
            messages.success(request, respuesta.Mensaje)
        else:
            messages.error(request, respuesta.Mensaje)
    return render(request, 'proveedor.html', prov)

def nuevoProv(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    if request.method=='POST':
        rutProv = request.POST["rutProveedor"]
        nombreProv = request.POST["nombreProveedor"]
        contactoProv = request.POST["contactoProveedor"]

        nuevoProveedor = modelsApp.Proveedor()
        nuevoProveedor.RUT = rutProv
        nuevoProveedor.Nombre = nombreProv
        nuevoProveedor.Contacto = contactoProv
        nuevoProveedor.Estado = True
        respuesta = MantenedorProveedores.AgregarProveedor(nuevoProveedor)

        if isinstance(respuesta, modelsApp.Resultado):
            if respuesta.CodigoOperacion == 200:
                messages.success(request, respuesta.Mensaje)
            else:
                messages.error(request, respuesta.Mensaje)
        #return render(request, 'proveedor.html', prov)
        return HttpResponseRedirect("/proveedor/")

def editarProv(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    if request.method=='POST':

        rutProv = request.POST["rutProveedorEdit"]
        nombreProv = request.POST["nombreProveedorEdit"]
        contactoProv = request.POST["contactoProveedorEdit"]
        estadoProv = "vigenciaEdit" in request.POST

        nuevoProveedor = modelsApp.Proveedor(rutProv, nombreProv, contactoProv, estadoProv)
        respuesta = MantenedorProveedores.ActualizarProveedor(nuevoProveedor)
        if isinstance(respuesta, modelsApp.Resultado):
            if respuesta.CodigoOperacion == 200:
                messages.success(request, respuesta.Mensaje)
            else:
                messages.error(request, respuesta.Mensaje)

        return HttpResponseRedirect('/proveedor/')