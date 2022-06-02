from datetime import datetime
from ConvertidorTipos import ConvertidorTipos
from backend.models import Boleta
from backend import models
from backend import modelsApp

class ControladorVentas():
    def RealizarVenta(boleta: modelsApp.Boleta):
        res = modelsApp.Resultado()

        nuevaBoleta = models.Boleta()
        nuevaBoleta.BOL_FECHA_VENTA = boleta.FechaVenta
        nuevaBoleta.BOL_SUBTOTAL = boleta.Subtotal
        nuevaBoleta.BOL_IVA = boleta.Iva
        nuevaBoleta.BOL_VIGENCIA = boleta.Vigencia
        nuevaBoleta.USU_USERNAME = boleta.Vendedor.Username

        try:
            nuevaBoleta.Save()

            for detalle in boleta.Detalle:
                nuevoDetalle = models.Detalle_Boleta()
                nuevoDetalle.BOL_NUMERO = boleta.Numero
                nuevoDetalle.PROD_CODIGO = detalle.Prod.PROD_CODIGO
                nuevoDetalle.DET_CANTIDAD = detalle.Cantidad
                nuevoDetalle.DET_VALOR = detalle.Valor
                nuevoDetalle.save()

            res.CodigoOperacion = 200
            res.Mensaje = "Venta realizada"
            return res
        except:
            res.CodigoOperacion = -1
            res.Mensaje = "Error al realizar venta"
            return res

    def __ObtenerDetalleVenta(nroBoleta: int):
        resDetalle = map(ConvertidorTipos.ConvertirDetalleBoleta, list(models.Detalle_Boleta.objects.filter(BOL_NUMERO = nroBoleta)))
        return resDetalle

    def LeerVenta(nroBoleta: int):
        res = modelsApp.Resultado()
        try:
            respuesta = models.Boleta(models.Boleta.objects.get(BOL_NUMERO = nroBoleta))
            resBoleta = ConvertidorTipos.ConvertirBoleta(respuesta)
            resBoleta.Detalle = ControladorVentas.__ObtenerDetalleVenta(nroBoleta)
            return resBoleta
        except models.Usuario.DoesNotExist:
            res.CodigoOperacion = -2
            res.Mensaje = "Boleta no existe"
            return res

    def AnularVenta(nroBoleta: int):
        res = modelsApp.Resultado()
        try:
            resBoleta = models.Boleta(models.Boleta.objects.get(BOL_NUMERO = nroBoleta))
            resBoleta.BOL_VIGENCIA = False

            resBoleta.save()
            res.CodigoOperacion = 200
            res.Mensaje = "Boleta anulada"
            return res
        except models.Boleta.DoesNotExist:
            res.CodigoOperacion = -2
            res.Mensaje = "Boleta no existe"
            return res

    def ListarVentas():
        res = modelsApp.Resultado()
        try:
            resBoletas = map(ConvertidorTipos.ConvertirBoleta, list(models.Boleta.objects.all()))
            return resBoletas
        except Exception as e:
            res.CodigoOperacion = -9
            res.Mensaje = str(e)
            return res
