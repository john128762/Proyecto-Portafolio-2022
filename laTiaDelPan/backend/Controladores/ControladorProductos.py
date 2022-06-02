from itertools import product
from backend import models
from backend import modelsApp
from ConvertidorTipos import ConvertidorTipos
class ControladorProductos:
    
    def AgregarProducto(producto: modelsApp.Producto):
        res = modelsApp.Resultado()
        nuevoProducto = models.Producto()
        nuevoProducto.PROD_CODIGO = producto.Codigo
        nuevoProducto.PROD_ESTADO = producto.Estado
        nuevoProducto.PROD_NOMBRE = producto.Nombre
        nuevoProducto.PROD_STOCK = producto.Stock
        nuevoProducto.PROD_VALOR = producto.Valor
        nuevoProducto.PROV_RUT = producto.Prov.RUT.split("-")[0]
        nuevoProducto.CAT_ID = producto.Cat.Id
        try:
            nuevoProducto.save()
            res.CodigoOperacion = 200
            res.Mensaje = "Producto ingresado"
        except:
            res.CodigoOperacion = -1
            res.Mensaje = "Error al ingresar producto"
            return res

    def LeerProducto(codigo: str):
        res = modelsApp.Resultado()
        try:
            respuesta = models.Producto(models.Producto.objects.get(PROD_CODIGO = codigo))
            resProducto = ConvertidorTipos.ConvertirProducto(respuesta)
            return resProducto
        except models.Producto.DoesNotExist:
            res.CodigoOperacion = -2
            res.Mensaje = "Producto no existe"
            return res

    def ActualizarProducto(producto: modelsApp.Producto):
        res = modelsApp.Resultado()
        try:
            resProducto = models.Producto(models.Producto.objects.get(PROD_CODIGO = producto.Codigo))
            resProducto.PROD_ESTADO = producto.Estado
            resProducto.PROD_NOMBRE = producto.Nombre
            resProducto.PROD_STOCK = producto.Stock
            resProducto.PROD_VALOR = producto.Valor
            resProducto.CAT_ID = producto.Cat.Id
            resProducto.PROV_RUT = producto.Prov.Id

            resProducto.Save()
            res.CodigoOperacion = 200
            res.Mensaje = "Producto actualizado"
            return res
        except models.Producto.DoesNotExist:
            res.CodigoOperacion = -2
            res.Mensaje = "Producto no existe"
            return res

    def EliminarProducto(codigo: str):
        res = modelsApp.Resultado()
        try:
            models.Producto.delete(PROD_CODIGO = codigo)
            res.CodigoOperacion = 200
            res.Mensaje = "Producto eliminado"
            return res
        except models.Producto.DoesNotExist:
            res.CodigoOperacion = -2
            res.Mensaje = "Producto no existe"
            return res

    def ListarProductos():
        res = modelsApp.Resultado()
        try:
            resProductos = map(ConvertidorTipos.ConvertirProducto, list(models.Producto.objects.all()))
            return resProductos
        except Exception as e:
            res.CodigoOperacion = -9
            res.Mensaje = str(e)
            return res