from django.shortcuts import render
from backend import models
#from backend import modelsApp
#from backend.Controladores import MantenedorCategorias
#from backend.Controladores import ControladorUsuarios
from django.http import HttpResponseRedirect

# Create your views here.

def registrarse(request):
    return render(request, 'registrarse.html')

def categoria(request):
    data = models.Categoria.objects.all()
    cat = {'categoriaT':data}
    return render(request, 'categoria.html', cat)

def nuevaCategoria(request):
    if request.method=='POST':
        nombreCat = request.POST.get("nombreCategoria")
        descripcionCat = request.POST.get('categoriaDescripcion')

        #nuevaCategoria = modelsApp.Categoria(Nombre=nombreCat, Descripcion=descripcionCat)
        #MantenedorCategorias.AgregarCategoria(nuevaCategoria)

        return HttpResponseRedirect('/categoria/')
    else:
        return HttpResponseRedirect('/categoria.html/')

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