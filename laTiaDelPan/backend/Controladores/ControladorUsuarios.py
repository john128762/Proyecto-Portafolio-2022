import models
import modelsApp
from datetime import datetime

def AgregarUsuario(usuario):
    if isinstance(usuario, modelsApp.Usuario):
        res = modelsApp.Resultado()

        nuevoUsuario = models.Usuario()
        nuevoUsuario.USU_RUT = usuario.RUT.split("-")[0]
        nuevoUsuario.USU_DV = usuario.RUT.split("-")[1]
        nuevoUsuario.USU_NOMBRES = usuario.Nombres
        nuevoUsuario.USU_APELLIDOS = usuario.Apellidos
        nuevoUsuario.USU_PASSWORD = usuario.Password
        nuevoUsuario.USU_ADMINISTRADOR = usuario.Administrador
        nuevoUsuario.USU_VIGENCIA = True
        nuevoUsuario.USU_FECHA_INGRESO = datetime.now()
        nuevoUsuario.USU_FECHA_MODIFICACION = datetime.now()

        try: 
            nuevoUsuario.save()
            res.CodigoOperacion = 200
            res.Mensaje = "Usuario ingresado."
        except:
            res.CodigoOperacion = -1
            res.Mensaje = "Error al ingresar el usuario."
    else:
        raise TypeError("El parametro usuario no es del tipo esperado")

#def ValidarUsuario(usuario, password):
#    if isinstance(usuario, str) and isinstance(password, str):
#        res = modelsApp.Resultado()
#        try: 
#            usuario = models.Usuario.objects.filter(USU_RUT = usuario)