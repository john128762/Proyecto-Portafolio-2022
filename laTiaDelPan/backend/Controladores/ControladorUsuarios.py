from backend import models
from backend import modelsApp
from backend.Controladores.ConvertidorTipos import ConvertidorTipos
from datetime import datetime
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import make_password, check_password
import bcrypt

class ControladorUsuarios():

    def ExistenMultiplesAdmin():
        try:
            return models.Usuario.objects.filter(USU_ADMINISTRADOR = True, USU_VIGENCIA = True).count() > 1
        except:
            return False

    def AgregarUsuario(usuario):
        if isinstance(usuario, modelsApp.Usuario):
            res = modelsApp.Resultado()

            nuevoUsuario = models.Usuario()
            nuevoUsuario.USU_USERNAME = usuario.Username
            rut = usuario.RUT.replace(".","")
            nuevoUsuario.USU_RUT = rut.split("-")[0]
            nuevoUsuario.USU_DV = rut.split("-")[1]
            nuevoUsuario.USU_NOMBRES = usuario.Nombres
            nuevoUsuario.USU_APELLIDOS = usuario.Apellidos
            nuevoUsuario.USU_PASSWORD = make_password(usuario.Password)
            nuevoUsuario.USU_ADMINISTRADOR = usuario.Administrador
            nuevoUsuario.USU_VIGENCIA = True
            nuevoUsuario.USU_FECHA_INGRESO = datetime.now()
            nuevoUsuario.USU_FECHA_MODIFICACION = datetime.now()

            try: 
                nuevoUsuario.save()
                if nuevoUsuario.USU_ADMINISTRADOR and ControladorUsuarios.ExistenMultiplesAdmin() and models.Usuario.objects.filter(USU_USERNAME = "admin").count() > 0:
                        usrAdmin = models.Usuario.objects.get(USU_USERNAME = "adminTemp999")
                        usrAdmin.delete()
                res.CodigoOperacion = 200
                res.Mensaje = "Usuario ingresado."
                return res
            except Exception as ex:
                res.CodigoOperacion = -1
                res.Mensaje = "Error al ingresar el usuario: " + str(ex)
                return res
        else:
            raise TypeError("El parametro usuario no es del tipo esperado")

    #def authenticate(self, request, username=None, password=None):

    def ValidarUsuario(username=None, password=None):
        try: 
            resUsuario = models.Usuario.objects.get(USU_USERNAME = username)
            res = check_password(password, resUsuario.USU_PASSWORD)
            if res:
                return ConvertidorTipos.ConvertirUsuario(resUsuario)
            else:
                return None
        except models.Usuario.DoesNotExist:
            return None
    
    def LeerUsuario(username):
        if isinstance(username, str):
            res = modelsApp.Resultado()
            try:
                respuesta = models.Usuario.objects.get(USU_USERNAME = username)
                resUsuario = ConvertidorTipos.ConvertirUsuario(respuesta)
                return resUsuario
            except models.Usuario.DoesNotExist:
                res.CodigoOperacion = -2
                res.Mensaje = "El usuario no existe"
                return res
        else:
            raise TypeError("El parametro username no es del tipo esperado")
    
    def ActualizarUsuario(usuario: modelsApp.Usuario):
        res = modelsApp.Resultado()
        if isinstance(usuario, modelsApp.Usuario):
            try:
                resUsuario = models.Usuario.objects.get(USU_USERNAME = usuario.Username)

                if resUsuario.USU_ADMINISTRADOR and resUsuario.USU_VIGENCIA and (not usuario.Administrador or not usuario.Vigencia) and not ControladorUsuarios.ExistenMultiplesAdmin():
                    res.CodigoOperacion = -10
                    res.Mensaje = "El sistema no puede quedar sin usuarios administradores."
                else:
                    resUsuario.USU_RUT = usuario.RUT.split("-")[0].replace(".","")
                    resUsuario.USU_DV = usuario.RUT.split("-")[1].replace(".","")
                    resUsuario.USU_PASSWORD = make_password(usuario.Password)
                    resUsuario.USU_NOMBRES = usuario.Nombres
                    resUsuario.USU_APELLIDOS = usuario.Apellidos
                    resUsuario.USU_VIGENCIA = usuario.Vigencia
                    resUsuario.USU_ADMINISTRADOR = usuario.Administrador
                    resUsuario.USU_FECHA_MODIFICACION = datetime.now()
                    resUsuario.save()                
                    res.CodigoOperacion = 200
                    res.Mensaje = "Usuario actualizado."
                return res
            except models.Usuario.DoesNotExist:
                res.CodigoOperacion = -2
                res.Mensaje = "El usuario no existe"
                return res

        else:
            raise TypeError("El parametro usuario no es del tipo esperado")
    
    def EliminarUsuario(username):
        res = modelsApp.Resultado()
        if isinstance(username, str):
            try:
                resUsuario = models.Usuario.objects.get(USU_USERNAME = username)
                if resUsuario.USU_ADMINISTRADOR and resUsuario.USU_VIGENCIA and not ControladorUsuarios.ExistenMultiplesAdmin():
                    res.CodigoOperacion = -10
                    res.Mensaje = "No se puede eliminar el unico administrador existente."
                else:
                    resUsuario.delete()
                    res.CodigoOperacion = 200
                    res.Mensaje = "Usuario eliminado."
                return res
            except models.Usuario.DoesNotExist:
                res.CodigoOperacion = -2
                res.Mensaje = "El usuario no existe"
                return res
        else:
            raise TypeError("El parametro username no es del tipo esperado")

    def ListarUsuarios():
        res = modelsApp.Resultado()
        try:
            resUsuarios = list(map(ConvertidorTipos.ConvertirUsuario, list(models.Usuario.objects.all())))
            return resUsuarios
        except Exception as e:
            res.CodigoOperacion = -9
            res.Mensaje = str(e)
            return res
