from django.shortcuts import render
from backend import models
from backend import modelsApp
from backend.Controladores import MantenedorCategorias
from backend.Controladores import MantenedorProveedores
from django.http import HttpResponseRedirect
import logging

# Create your views here.

def registrarse(request):
    return render(request, 'registrarse.html')

def categoria(request):
    data = models.Categoria.objects.all()
    cat = {'categoriaT':data}
    return render(request, 'categoria.html', cat)

def producto(request):
    dataPro = models.Producto.objects.all()
    prod = {'productoT':dataPro}
    return render(request, 'producto.html', prod)

def venta(request):
    return render(request, 'venta.html')