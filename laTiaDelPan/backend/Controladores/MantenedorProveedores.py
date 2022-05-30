from re import M
import backend.modelsApp
import backend.models
from backend.Controladores.ConvertidorTipos import ConvertidorTipos

class MantenedorProveedores:
    def AgregarProveedor(proveedor: modelsApp.Proveedor):
        res = modelsApp.Resultado()
        nuevoProveedor = models.Proveedor()
        nuevoProveedor.PROV_RUT = str.split(proveedor.RUT, "-")[0]
        nuevoProveedor.PROV_DV = str.split(proveedor.RUT, "-")[1]
        nuevoProveedor.PROV_NOMBRE = proveedor.Nombre
        nuevoProveedor.PROV_CONTACTO = proveedor.Contacto
        nuevoProveedor.PROV_ESTADO = proveedor.Estado

        try:
            nuevoProveedor.save()
            res.CodigoOperacion = 200
            res.Mensaje = "Proveedor ingresado"
            return res
        except:
            res.CodigoOperacion = -1
            res.Mensaje = "Error al ingresar el proveedor"
            return res
        
    def LeerProveedor(rut: str):
        res = modelsApp.Resultado()
        try:
            respuesta = models.Proveedor(models.Proveedor.objects.get(PROV_RUT = str.split(rut, "-")[0]))
            resProveedor = ConvertidorTipos.ConvertirProveedor(respuesta)
            return resProveedor
        except models.Proveedor.DoesNotExist:
            res.CodigoOperacion = -2
            res.Mensaje = "Proveedor no existe"
            return res
            
    def ActualizarProveedor(proveedor: modelsApp.Proveedor):
        res = modelsApp.Resultado()
        try:
            resProveedor = models.Proveedor(models.Proveedor.objects.get(PROV_RUT = proveedor.RUT.split("-")[0]))
            resProveedor.PROV_NOMBRE = proveedor.Nombre
            resProveedor.PROV_CONTACTO = proveedor.Contacto
            resProveedor.PROV_ESTADO = proveedor.Estado
            
            resProveedor.Save()
            res.CodigoOperacion = 200
            res.Mensaje = "Proveedor actualizado"
            return res
        
        except models.Proveedor.DoesNotExist:
            res.CodigoOperacion = -2
            res.Mensaje = "Proveedor no existe"
            return res

    def EliminarProveedor(rut: str):
        res = modelsApp.Resultado()
        try:
            models.Proveedor.delete(PROV_RUT = rut.split("-")[0])
            res.CodigoOperacion = 200
            res.Mensaje = "Proveedor eliminador"
            return res
        except models.Proveedor.DoesNotExist:
            res.CodigoOperacion = -2
            res.Mensaje = "Proveedor no existe"
            return res

    def ListarProveedores():
        res = modelsApp.Resultado()
        try:
            resProveedores = map(ConvertidorTipos.ConvertirProveedor, list(models.Proveedor.objects.all()))
            return resProveedores
        except Exception as e:
            res.CodigoOperacion = -9
            res.Mensaje = str(e)
            return res
