from django.shortcuts import render
from backend import models
from backend import modelsApp
from backend.Controladores.MantenedorCategorias import MantenedorCategorias
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def categoria(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    data = MantenedorCategorias.ListarCategorias()
    cat = {'categoriaT':data}
    return render(request, 'categoria.html', cat)

def nuevaCategoria(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    if request.method=='POST':
        nombre = request.POST["nombreCategoria"]
        descripcion = request.POST["categoriaDescripcion"]

        categoria = modelsApp.Categoria()
        categoria.Nombre = nombre
        categoria.Descripcion = descripcion
        categoria.Estado = True
        respuesta = MantenedorCategorias.AgregarCategoria(categoria)
        if isinstance(respuesta, modelsApp.Resultado):
            if respuesta.CodigoOperacion == 200:
                messages.success(request, respuesta.Mensaje)
            else:
                messages.error(request, respuesta.Mensaje)
        return HttpResponseRedirect('/categoria/')

def editarCategoria(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    if request.method=='POST':
        idCat = request.POST["idEdit"]
        #catAntigua = MantenedorCategorias.MantenedorCategorias.LeerCategoria(idCat)
        nombreCat = request.POST["nombreCategoriaEdit"]
        descripcionCat = request.POST["categoriaDescripcionEdit"]
        estadoCat = "vigenciaEdit" in request.POST

        cate = modelsApp.Categoria()
        cate.Id = idCat
        cate.Nombre = nombreCat
        cate.Descripcion = descripcionCat
        cate.Estado = estadoCat
        respuesta = MantenedorCategorias.ActualizarCategoria(cate)
        if isinstance(respuesta, modelsApp.Resultado):
            if respuesta.CodigoOperacion == 200:
                messages.success(request, respuesta.Mensaje)
            else:
                messages.error(request, respuesta.Mensaje)        
        return HttpResponseRedirect('/categoria/')

def eliminarCategoria(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    if request.method =='POST':
        idCat = request.POST["idCategoria"]
        respuesta = MantenedorCategorias.EliminarCategoria(idCat)
        if isinstance(respuesta, modelsApp.Resultado):
            if respuesta.CodigoOperacion == 200:
                messages.success(request, respuesta.Mensaje)
            else:
                messages.error(request, respuesta.Mensaje)
        return HttpResponseRedirect('/categoria/')