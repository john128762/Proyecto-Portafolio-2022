from django.shortcuts import render

# Create your views here.

def registrarse(request):
    return render(request, 'registrarse.html')

def categoria(request):
    return render(request, 'categoria.html')

def proveedor(request):
    return render(request, 'proveedor.html')

def producto(request):
    return render(request, 'producto.html')

def venta(request):
    return render(request, 'venta.html')