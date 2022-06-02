from backend import models
from backend import modelsApp
from datetime import datetime
from backend.Controladores.ConvertidorTipos import ConvertidorTipos
from laTiaDelPan.backend.models import Categoria
#import ConvertidorTipos
class MantenedorCategorias:
    def AgregarCategoria(categoria):
        resultado = modelsApp.Resultado()
        if isinstance(categoria, modelsApp.Categoria):
            nuevaCategoria = models.Categoria()
            nuevaCategoria.CAT_ESTADO = categoria.Estado
            nuevaCategoria.CAT_NOMBRE = categoria.Nombre
            nuevaCategoria.CAT_DESCRIPCION = categoria.Descripcion
            try:
                nuevaCategoria.save()
                resultado.CodigoOperacion = 200
                resultado.Mensaje = "Categoria agregada."
                return resultado
            except:
                resultado.CodigoOperacion = -1
                resultado.Mensaje = "Error al ingresar categoria"
                return resultado
        else:
            raise TypeError("El parametro categoria no es del tipo esperado.")
    
    def LeerCategoria(id):
        resultado = modelsApp.Resultado
        try:
            respuesta = models.Categoria(models.Categoria.objects.get(CAT_ID = id))
            resCategoria = modelsApp.Categoria()
            resCategoria.Id = respuesta.CAT_ID
            resCategoria.Descripcion = respuesta.CAT_DESCRIPCION
            resCategoria.Nombre = respuesta.CAT_NOMBRE
            resCategoria.Estado = respuesta.CAT_ESTADO
        except models.Categoria.DoesNotExist:
            resultado.CodigoOperacion = -2
            resultado.Mensaje = "La categoria no existe"
        return None
    
    def ActualizarCategoria(categoria):
        resultado = modelsApp.Resultado()
        if isinstance(categoria, modelsApp.Categoria):
            try:
                resCategoria = models.Categoria(models.Categoria.objects.get(CAT_ID = categoria.Id))
                resCategoria.CAT_ESTADO = categoria.Estado
                resCategoria.CAT_NOMBRE = categoria.Nombre
                resCategoria.CAT_DESCRIPCION = categoria.Descripcion
                resCategoria.Save()
                resultado.CodigoOperacion = 200
                resultado.Mensaje = "Categoria actualizada."
                return resultado
            except:
                resultado.CodigoOperacion = -2
                resultado.Mensaje = "Error al actualizar categoria"
                return resultado
        else:
            raise TypeError("El parametro categoria no es del tipo esperado")
    
    def EliminarCategoria(id):
        resultado = modelsApp.Resultado()
        if isinstance(id, int) or (isinstance(id, str) and id.isnumeric()):
            try:
                models.Categoria.delete(CATID = id)
                resultado.CodigoOperacion = 200
                resultado.Mensaje = "Categoria eliminada"
                return resultado
            except models.Categoria.DoesNotExist:
                resultado.CodigoOperacion = -1
                resultado.Mensaje = "Categoria no existe"
                return resultado
        else:
            raise TypeError("El parametro id no es del tipo esperado")

    def ListarCategorias():
        res = modelsApp.Resultado
        try:
            resCategorias = map(ConvertidorTipos.ConvertirCategoria, list(models.Categoria.objects.all))
            return resCategorias
        except Exception as e:
            res.CodigoOperacion = -9
            res.Mensaje = str(e)
            return res