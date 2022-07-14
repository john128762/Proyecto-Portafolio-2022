from django.shortcuts import render
from backend import modelsApp
from backend.Controladores.ControladorVentas import ControladorVentas
from backend.Controladores.ControladorFacturasProveedor import ControladorFacturasProveedor

# Create your views here.

def login(request):
    return render(request, 'login.html')

def paginaPrincipal(request):
    return render(request, 'paginaPrincipal.html')

def analisisVenta(request):
    request.session['username'] = "username"
    detV = ControladorVentas.ListarDetalleVentas()
    detF = ControladorFacturasProveedor.ListarDetalleFacturas()
    data = {'detalleV':detV, 'detalleF': detF}
    return render(request, 'analisisVentas.html', data)