from django.shortcuts import render
from backend.Controladores.ControladorVentas import ControladorVentas
from backend.Controladores.ControladorFacturasProveedor import ControladorFacturasProveedor

# Create your views here.

def login(request):
    return render(request, 'login.html')

def paginaPrincipal(request):
    return render(request, 'paginaPrincipal.html')

def analisisVenta(request):
    dataV = ControladorVentas.ListarVentas()
    dataF = ControladorFacturasProveedor.ListarFacturas()
    tabla = {'venta': dataV, 'factura':dataF}
    return render(request, 'analisisVentas.html', tabla)