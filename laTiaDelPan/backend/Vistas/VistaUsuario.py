from django.shortcuts import render
from backend import models
from backend import modelsApp
from backend.Controladores import ControladorUsuarios
from django.http import HttpResponseRedirect

def usuario(request):
    dataUsu = models.Usuario.objects.all()
    usu = {'usuarioT':dataUsu}
    return render(request, 'usuario.html', usu)

def nuevoUsuario(request):
    if request.method=='POST':
        rutUsu = request.POST["rutUsuario"]
        userName = request.POST["userName"]
        nombreUsu = request.POST["nombreUsu"]
        apellidoUsu = request.POST["ApellidoUsu"]
        password = request.POST["password"]

        usuario = modelsApp.Usuario()
        usuario.RUT = rutUsu
        usuario.Username = userName
        usuario.Nombres = nombreUsu
        usuario.Apellidos = apellidoUsu
        usuario.Password = password
        usuario.Vigencia = True
        usuario.Administrador = True
        ControladorUsuarios.ControladorUsuarios.AgregarUsuario(usuario)

        return HttpResponseRedirect('/usuario/')

def editarUsuario(request):
    if request.method=='POST':
        print(request.POST)
        rutUsu = request.POST["rutUsuarioEdit"]
        #catAntigua = MantenedorCategorias.MantenedorCategorias.LeerCategoria(idCat)
        username = request.POST["userNameEdit"]
        nombre = request.POST["nombreUsuEdit"]
        apellido = request.POST["apellidoUsuEdit"]
        password = request.POST["passwordEdit"]
        if request.POST.get("usuVigenciaEdit"):
            vigencia = True
        else:
            vigencia = False
        if request.POST.get("usuAdminEdit"):
            admin = True
        else:
            admin = False
        usu = modelsApp.Usuario()
        usu.RUT = rutUsu
        usu.Username = username
        usu.Nombres = nombre
        usu.Apellidos = apellido
        usu.Password = password
        usu.Vigencia = vigencia
        usu.Administrador = admin
        respuesta = ControladorUsuarios.ControladorUsuarios.ActualizarUsuario(usu)
        print("Codigo: " + str(respuesta.CodigoOperacion)) 
        print("Mensaje: " + respuesta.Mensaje)
        return HttpResponseRedirect('/usuario/')

def eliminarUsuario(request):
    if request.method =='POST':
        print(request.POST)
        username = request.POST["idUsuario"]
        respuesta = ControladorUsuarios.ControladorUsuarios.EliminarUsuario(username)
        print("Codigo: " + str(respuesta.CodigoOperacion)) 
        print("Mensaje: " + respuesta.Mensaje)
        return HttpResponseRedirect('/usuario/')