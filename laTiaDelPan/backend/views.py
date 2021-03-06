from django.shortcuts import render
from backend import models
from backend import modelsApp
from backend.Controladores import MantenedorCategorias
from backend.Controladores import MantenedorProveedores
from django.http import HttpResponseRedirect
import logging

# Create your views here.

def usuario(request):
    dataUsu = models.Usuario.objects.all()
    usu = {'usuarioT':dataUsu}
    return render(request, 'usuario.html', usu)

def categoria(request):
    data = models.Categoria.objects.all()
    cat = {'categoriaT':data}
    return render(request, 'categoria.html', cat)

def producto(request):
    dataPro = models.Producto.objects.all()
    dataCat = models.Categoria.objects.all()
    dataProv = models.Proveedor.objects.all()
    prod = {'productoT':dataPro, 'categoriaSelect':dataCat, 'proveedorSelect':dataProv}
    return render(request, 'producto.html', prod)

def venta(request):
    return render(request, 'venta.html')