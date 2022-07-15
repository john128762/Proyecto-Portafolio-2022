from django.shortcuts import render
from backend import models
from backend import modelsApp
from backend.Controladores.ControladorUsuarios import ControladorUsuarios
from django.http import HttpResponseRedirect
from django.contrib import messages

def usuario(request, respuesta=None):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    list(messages.get_messages(request))
    dataUsu = list(ControladorUsuarios.ListarUsuarios())
    for usuario in dataUsu:
        usuario.Password = ""
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
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    if request.method=='POST':
        rutUsu = request.POST["rutUsuario"]
        userName = request.POST["userName"]
        nombreUsu = request.POST["nombreUsu"]
        apellidoUsu = request.POST["ApellidoUsu"]
        password = request.POST["password"]
        admin = "usuAdmin" in request.POST

        usuario = modelsApp.Usuario()
        usuario.RUT = rutUsu
        usuario.Username = userName
        usuario.Nombres = nombreUsu
        usuario.Apellidos = apellidoUsu
        usuario.Password = password
        usuario.Vigencia = True
        usuario.Administrador = admin
        respuesta = ControladorUsuarios.AgregarUsuario(usuario)
        if isinstance(respuesta, modelsApp.Resultado):
            if respuesta.CodigoOperacion == 200:
                messages.success(request, respuesta.Mensaje)
            else:
                messages.error(request, respuesta.Mensaje)

        return HttpResponseRedirect('/usuario/')

def editarUsuario(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    if request.method=='POST':

        rutUsu = request.POST["rutUsuarioEdit"]
        username = request.POST["userNameEdit"]
        nombre = request.POST["nombreUsuEdit"]
        apellido = request.POST["apellidoUsuEdit"]
        password = request.POST["passwordEdit"]
        vigencia = "usuVigenciaEdit" in request.POST
        admin = "usuAdminEdit" in request.POST

        #if username == request.session["username"] and not vigencia or not admin:
            #messages.error(request, "No se puede desactivar el mismo usuario que esta logueado en esta sesion")
            #return HttpResponseRedirect('/usuario')

        nuevoUsu = modelsApp.Usuario(rutUsu, username, nombre, apellido, password, vigencia, admin)
        respuesta = ControladorUsuarios.ActualizarUsuario(nuevoUsu)
        if isinstance(respuesta, modelsApp.Resultado):
            if respuesta.CodigoOperacion == 200:
                messages.success(request, respuesta.Mensaje)
            else:
                messages.error(request, respuesta.Mensaje)
        return HttpResponseRedirect('/usuario/')

def eliminarUsuario(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    if request.method =='POST':
        username = request.POST["idUsuario"]
        if username == request.session["username"]:
            messages.error(request, "No se puede eliminar el mismo usuario que esta logueado en esta sesion")
            return HttpResponseRedirect('/usuario')
        respuesta = ControladorUsuarios.EliminarUsuario(username)
        if isinstance(respuesta, modelsApp.Resultado):
            if respuesta.CodigoOperacion == 200:
                messages.success(request, respuesta.Mensaje)
            else:
                messages.error(request, respuesta.Mensaje)
        return HttpResponseRedirect('/usuario/')