from backend import models
from backend import modelsApp
from backend.Controladores.ConvertidorTipos import ConvertidorTipos
from datetime import datetime

class ControladorUsuarios:

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
            nuevoUsuario.USU_PASSWORD = usuario.Password
            nuevoUsuario.USU_ADMINISTRADOR = usuario.Administrador
            nuevoUsuario.USU_VIGENCIA = True
            nuevoUsuario.USU_FECHA_INGRESO = datetime.now()
            nuevoUsuario.USU_FECHA_MODIFICACION = datetime.now()

            try: 
                nuevoUsuario.save()
                res.CodigoOperacion = 200
                res.Mensaje = "Usuario ingresado."
                return res
            except:
                res.CodigoOperacion = -1
                res.Mensaje = "Error al ingresar el usuario."
                return res
        else:
            raise TypeError("El parametro usuario no es del tipo esperado")

    def ValidarUsuario(username, password):
        if isinstance(username, str) and isinstance(password, str):
            res = modelsApp.Resultado()
            try: 
                resUsuario = models.Usuario(models.Usuario.objects.get(USU_USERNAME = username))
                if password == resUsuario.USU_PASSWORD:
                    res.CodigoOperacion = 200
                    res.Mensaje = "Usuario validado"
                else:
                    res.CodigoOperacion = -3
                    res.Mensaje = "El RUT o contraseña es incorrecto"
                return res
            except models.Usuario.DoesNotExist:
                res.CodigoOperacion = -2
                res.Mensaje = "El usuario no existe"
                return res
        else:
            raise TypeError("Los parametros username y password no son del tipo esperado")
    
    def LeerUsuario(username):
        if isinstance(username, str):
            res = modelsApp.Resultado()
            try:
                respuesta = models.Usuario(models.Usuario.objects.get(USU_USERNAME = username))
                resUsuario = ConvertidorTipos.ConvertirUsuario(respuesta)
                return resUsuario
            except models.Usuario.DoesNotExist:
                res.CodigoOperacion = -2
                res.Mensaje = "El usuario no existe"
                return res
        else:
            raise TypeError("El parametro username no es del tipo esperado")
    
    def ActualizarUsuario(usuario):
        res = modelsApp.Resultado()
        if isinstance(usuario, modelsApp.Usuario):
            try:
                resUsuario = models.Usuario(models.Usuario.objects.get(USU_USERNAME = usuario.Username))
                resUsuario.USU_RUT = usuario.RUT.split("-")[0]
                resUsuario.USU_DV = usuario.RUT.split("-")[1]
                resUsuario.USU_PASSWORD = usuario.Password
                resUsuario.USU_NOMBRES = usuario.Nombres
                resUsuario.USU_APELLIDOS = usuario.Apellidos
                resUsuario.USU_VIGENCIA = usuario.Vigencia
                resUsuario.USU_ADMINISTRADOR = usuario.Administrador
                resUsuario.USU_FECHA_MODIFICACION = datetime.now

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
                models.Usuario.delete(USU_USERNAME = username)
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
            resUsuarios = map(ConvertidorTipos.ConvertirUsuario, list(models.Usuario.objects.all()))
            return resUsuarios
        except Exception as e:
            res.CodigoOperacion = -9
            res.Mensaje = str(e)
            return res

