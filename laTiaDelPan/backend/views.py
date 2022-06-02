from distutils.log import debug
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

def nuevaCategoria(request):
    if request.method=='POST':
        nombre = request.POST["nombreCategoria"]
        descripcion = request.POST["categoriaDescripcion"]

        categoria = modelsApp.Categoria()
        categoria.Nombre = nombre
        categoria.Descripcion = descripcion
        MantenedorCategorias.MantenedorCategorias.AgregarCategoria(categoria)

        return HttpResponseRedirect('/categoria/')


def editarCategoria(request):
    if request.method=='POST':
        idCat = request.POST["idEdit"]
        MantenedorCategorias.MantenedorCategorias.LeerCategoria(idCat)
        nombreCat = request.POST["nombreCategoria"]
        descripcionCat = request.POST["categoriaDescripcion"]

        cate = modelsApp.Categoria()
        cate.Nombre = nombreCat
        cate.Descripcion = descripcionCat
        MantenedorCategorias.MantenedorCategorias.ActualizarCategoria(cate)
        return HttpResponseRedirect('/categoria/')

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

def producto(request):
    dataPro = models.Producto.objects.all()
    prod = {'productoT':dataPro}
    return render(request, 'producto.html', prod)

def venta(request):
    return render(request, 'venta.html')