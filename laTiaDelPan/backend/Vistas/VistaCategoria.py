from django.shortcuts import render
from backend import models
from backend import modelsApp
from backend.Controladores import MantenedorCategorias
from django.http import HttpResponseRedirect

# Create your views here.

def categoria(request):
    data = MantenedorCategorias.MantenedorCategorias.ListarCategorias()
    cat = {'categoriaT':data}
    return render(request, 'categoria.html', cat)

def nuevaCategoria(request):
    if request.method=='POST':
        nombre = request.POST["nombreCategoria"]
        descripcion = request.POST["categoriaDescripcion"]

        categoria = modelsApp.Categoria()
        categoria.Nombre = nombre
        categoria.Descripcion = descripcion
        categoria.Estado = True
        MantenedorCategorias.MantenedorCategorias.AgregarCategoria(categoria)

        return HttpResponseRedirect('/categoria/')

def editarCategoria(request):
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
        respuesta = MantenedorCategorias.MantenedorCategorias.ActualizarCategoria(cate)
        return HttpResponseRedirect('/categoria/')

def eliminarCategoria(request):
    if request.method =='POST':
        idCat = request.POST["idCategoria"]
        respuesta = MantenedorCategorias.MantenedorCategorias.EliminarCategoria(idCat)
        return HttpResponseRedirect('/categoria/')