from distutils.log import debug
from django.shortcuts import render
from backend import models
from backend import modelsApp
from backend.Controladores import MantenedorCategorias
from django.http import HttpResponseRedirect
import logging

# Create your views here.

def registrarse(request):
    return render(request, 'registrarse.html')

def categoria(request):
    data = models.Categoria.objects.all()
    cat = {'categoriaT':data}
    return render(request, 'categoria.html', cat)

def nuevaCategoria(request):
    if request.method=='POST':
        nombre = request.POST["nombreCategoria"]
        descripcion = request.POST["categoriaDescripcion"]

        categoria = modelsApp.Categoria
        categoria.Nombre = nombre
        categoria.Descripcion = descripcion
        nuevaCategoria = categoria
        MantenedorCategorias.MantenedorCategorias.AgregarCategoria(nuevaCategoria)

def proveedor(request):
    dataP = models.Proveedor.objects.all()
    prov = {'proveedorT':dataP}
    return render(request, 'proveedor.html', prov)

def producto(request):
    dataPro = models.Producto.objects.all()
    prod = {'productoT':dataPro}
    return render(request, 'producto.html', prod)

def venta(request):
    return render(request, 'venta.html')