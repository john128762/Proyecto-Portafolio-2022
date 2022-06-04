from django.shortcuts import render
from backend import models
from backend import modelsApp
from backend.Controladores.ControladorUsuarios import ControladorUsuarios
from django.http import HttpResponseRedirect
from django.contrib import messages

def usuario(request, respuesta=None):
    list(messages.get_messages(request))
    dataUsu = ControladorUsuarios.ListarUsuarios()
    if(isinstance(dataUsu, modelsApp.Resultado)):
        print(dataUsu.Mensaje)
    usu = {'usuarioT':dataUsu}
    if isinstance(respuesta, modelsApp.Resultado):
        if respuesta.CodigoOperacion == 200:
            messages.success(request, respuesta.Mensaje)
        else:
            messages.error(request, respuesta.Mensaje)
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
        respuesta = ControladorUsuarios.AgregarUsuario(usuario)
        if isinstance(respuesta, modelsApp.Resultado):
            if respuesta.CodigoOperacion == 200:
                messages.success(request, respuesta.Mensaje)
            else:
                messages.error(request, respuesta.Mensaje)

        return HttpResponseRedirect('/usuario/')

def editarUsuario(request):
    if request.method=='POST':

        rutUsu = request.POST["rutUsuarioEdit"]
        username = request.POST["userNameEdit"]
        nombre = request.POST["nombreUsuEdit"]
        apellido = request.POST["apellidoUsuEdit"]
        password = request.POST["passwordEdit"]
        vigencia = "usuVigenciaEdit" in request.POST
        admin = "usuAdminEdit" in request.POST

        nuevoUsu = modelsApp.Usuario(rutUsu, username, nombre, apellido, password, vigencia, admin)
        respuesta = ControladorUsuarios.ActualizarUsuario(nuevoUsu)
        if isinstance(respuesta, modelsApp.Resultado):
            if respuesta.CodigoOperacion == 200:
                messages.success(request, respuesta.Mensaje)
            else:
                messages.error(request, respuesta.Mensaje)
        return HttpResponseRedirect('/usuario/')

def eliminarUsuario(request):
    if request.method =='POST':
        print(request.POST)
        username = request.POST["idUsuario"]
        respuesta = ControladorUsuarios.EliminarUsuario(username)
        if isinstance(respuesta, modelsApp.Resultado):
            if respuesta.CodigoOperacion == 200:
                messages.success(request, respuesta.Mensaje)
            else:
                messages.error(request, respuesta.Mensaje)
        return HttpResponseRedirect('/usuario/')