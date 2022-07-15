from django.forms import PasswordInput
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from backend import modelsApp
from backend.Controladores.ControladorVentas import ControladorVentas
from backend.Controladores.ControladorFacturasProveedor import ControladorFacturasProveedor
from backend.Controladores.ControladorUsuarios import ControladorUsuarios
from django.contrib.auth import authenticate, login
import json
# Create your views here.

def loginView(request):
    if "username" in request.session:
        return HttpResponseRedirect("principal")
    return render(request, 'login.html')

def iniciarSesion(request):
    if request.method == "POST":
        user = request.POST["in_usuario"]
        passw = request.POST["in_password"]

        usuario = ControladorUsuarios.ValidarUsuario(username=user, password=passw)

        #usuario = authenticate(request, username=user, password=passw)
        if usuario is not None:
            #login(request, usuario)
            request.session["username"] = user
            request.session["esAdmin"] = usuario.Administrador
            request.session["nombreCompleto"] = usuario.Nombres + " " + usuario.Apellidos
        #if respuesta.CodigoOperacion == 200:
            #request.session["user"] = username
    return HttpResponseRedirect("/")

def cerrarSesion(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    if request.method == "POST":
        if "username" in request.session:
            del request.session["username"]
    return HttpResponseRedirect("/")

def paginaPrincipal(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    return render(request, 'paginaPrincipal.html')

def esAdmin(request):
    esAdmin = "esAdmin" in request.session and request.session["esAdmin"] == True
    return JsonResponse(status=200, data={"esAdmin" : str(esAdmin)})

def obtenerNombre(request):
    if "nombreCompleto" in request.session:
        return JsonResponse(status=200, data={"nombreCompleto":request.session["nombreCompleto"]})

def analisisVenta(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    request.session['username'] = "username"
    detV = ControladorVentas.ListarDetalleVentas()
    detF = ControladorFacturasProveedor.ListarDetalleFacturas()
    data = {'detalleV':detV, 'detalleF': detF}
    return render(request, 'analisisVentas.html', data)