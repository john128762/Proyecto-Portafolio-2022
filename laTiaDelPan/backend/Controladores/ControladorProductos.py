from itertools import product
from backend import models
from backend import modelsApp
from backend.Controladores.ConvertidorTipos import ConvertidorTipos

class ControladorProductos:
    
    def AgregarProducto(producto: modelsApp.Producto):
        res = modelsApp.Resultado()
        nuevoProducto = models.Producto()

        rutProv = producto.Prov.RUT.replace(".","")
        print(producto.Cat)


        nuevoProducto.PROD_CODIGO = producto.Codigo
        nuevoProducto.PROD_ESTADO = producto.Estado
        nuevoProducto.PROD_NOMBRE = producto.Nombre
        nuevoProducto.PROD_STOCK = producto.Stock
        nuevoProducto.PROD_VALOR = producto.Valor
        #nuevoProducto.PROV_RUT = rutProv.split("-")[0]
        nuevoProducto.PROV_RUT = models.Proveedor.objects.get(PROV_RUT = rutProv.split("-")[0])
        nuevoProducto.CAT_ID = models.Categoria.objects.get(CAT_ID = producto.Cat.Id)
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
            respuesta = models.Producto.objects.get(PROD_CODIGO = codigo)
            resProducto = ConvertidorTipos.ConvertirProducto(respuesta)
            return resProducto
        except models.Producto.DoesNotExist:
            res.CodigoOperacion = -2
            res.Mensaje = "Producto no existe"
            return res

    def ActualizarProducto(producto: modelsApp.Producto):
        res = modelsApp.Resultado()
        rutProv = producto.Prov.RUT.replace(".","")
        try:
            resProducto = models.Producto.objects.get(PROD_CODIGO = producto.Codigo)
            resProducto.PROD_ESTADO = producto.Estado
            resProducto.PROD_NOMBRE = producto.Nombre
            resProducto.PROD_STOCK = producto.Stock
            resProducto.PROD_VALOR = producto.Valor
            resProducto.CAT_ID = models.Categoria.objects.get(CAT_ID = producto.Cat.Id)
            resProducto.PROV_RUT = models.Proveedor.objects.get(PROV_RUT = rutProv.split("-")[0])

            resProducto.save()
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
            resProducto = models.Producto.objects.get(PROD_CODIGO = codigo)
            resProducto.delete()
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
            resProductos = list(map(ConvertidorTipos.ConvertirProducto, list(models.Producto.objects.all())))
            return resProductos
        except Exception as e:
            res.CodigoOperacion = -9
            res.Mensaje = str(e)
            return res