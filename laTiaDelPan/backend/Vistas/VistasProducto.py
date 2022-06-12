from django.shortcuts import render
from backend import models
from backend import modelsApp
from backend.Controladores.ControladorProductos import ControladorProductos
from backend.Controladores.MantenedorProveedores import MantenedorProveedores
from backend.Controladores.MantenedorCategorias import MantenedorCategorias
from django.http import HttpResponseRedirect
from django.contrib import messages

from backend.Vistas.VistaProveedor import proveedor

def producto(request, respuesta=None):
    dataprov = MantenedorProveedores.ListarProveedores()
    dataPro = ControladorProductos.ListarProductos()
    dataCat = models.Categoria.objects.all()
    prod = {'productoT':dataPro, 'categoriaSelect':dataCat, 'proveedorSelect':dataprov}
    if isinstance(respuesta, modelsApp.Resultado):
        if respuesta.CodigoOperacion == 200:
            messages.success(request, respuesta.Mensaje)
        else:
            messages.error(request, respuesta.Mensaje)
    return render(request, 'producto.html', prod)

def nuevoProducto(request):
    if request.method=='POST':
        codigo = request.POST["codigoProducto"]
        nombre = request.POST["nombreProducto"]
        stock = request.POST["stockProducto"]
        valor = request.POST["valorProducto"]
        prodProve = request.POST["idProvProd"]
        prodCate = request.POST["idCatProd"]
        
        

        producto = modelsApp.Producto()
        producto.Codigo = codigo
        producto.Nombre = nombre
        producto.Stock = stock
        producto.Valor = valor
        producto.Prov = MantenedorProveedores.LeerProveedor(prodProve)
        print(prodCate)
        producto.Cat = MantenedorCategorias.LeerCategoria(prodCate)
        #producto.Cat.Id = prodCate
        producto.Estado = True
        print(producto.Cat)
        respuesta = ControladorProductos.AgregarProducto(producto)
        if isinstance(respuesta, modelsApp.Resultado):
            if respuesta.CodigoOperacion == 200:
                messages.success(request, respuesta.Mensaje)
            else:
                messages.error(request, respuesta.Mensaje)
        return HttpResponseRedirect('/producto/')