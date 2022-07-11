from backend.Controladores.ConvertidorTipos import ConvertidorTipos
from datetime import datetime
from backend import models
from backend import modelsApp
from backend.Controladores.ControladorProductos import ControladorProductos

class ControladorFacturasProveedor:
    def AgregarFactura(factura: modelsApp.FacturaProveedor):
        res = modelsApp.Resultado()
        nuevaFactura = models.Fact_Proveedor()

        nuevaFactura.FAC_NUMERO = factura.Numero
        nuevaFactura.FAC_FECHA_VENTA = factura.FechaVenta
        nuevaFactura.FAC_TOTAL = factura.Total
        nuevaFactura.FAC_VIGENCIA = factura.Vigencia
        nuevaFactura.USU_USERNAME = models.Usuario.objects.get(USU_USERNAME = factura.Vendedor.Username)

        try:
            nuevaFactura.save()
            nuevaFactura.refresh_from_db()
            detalle: modelsApp.DetalleFacturaProveedor
            for detalle in factura.Detalle:
                try:
                    nuevoDetalle = models.Det_Fact_Proveedor()
                    nuevoDetalle.FAC_NUMERO = nuevaFactura
                    nuevoDetalle.PROD_CODIGO = models.Producto.objects.get(PROD_CODIGO = detalle.Prod.Codigo)
                    nuevoDetalle.DFT_CANTIDAD = detalle.Cantidad
                    nuevoDetalle.DFT_VALOR = detalle.Valor
                    nuevoDetalle.save()
                    ControladorProductos.DisminuirStockProducto(detalle.Prod.Codigo, detalle.Cantidad)

                except Exception as ex:
                    obj: models.Detalle_Boleta
                    for obj in models.Detalle_Boleta.objects.filter(BOL_NUMERO = nuevaFactura.BOL_NUMERO) :
                        obj.delete()
                    nuevaFactura.delete()

                    res.CodigoOperacion = -1
                    res.Mensaje = "Error al realizar la factura: " + str(ex)
                    #raise ex
                    return res

            res.CodigoOperacion = 200
            res.Mensaje = "Factura realizada"
            return res
        except:
            res.CodigoOperacion = -1
            res.Mensaje = "Error al realizar la factura: " + str(ex)
            return res

    def __ObtenerDetalleFactura(nroFacturaProv: int):
        resDetalle = map(ConvertidorTipos.ConvertirDetalleFacturaProveedor, list(models.Det_Fact_Proveedor.objects.filter(FAC_NUMERO = nroFacturaProv)))
        return resDetalle

    def LeerVenta(nroFacturaProv: int):
        res = modelsApp.Resultado()
        try:
            respuesta = models.Fact_Proveedor(models.Fact_Proveedor.objects.get(FAC_NUMERO = nroFacturaProv))
            resFactura = ConvertidorTipos.ConvertirFacturaProveedor(respuesta)
            resFactura.Detalle = ControladorFacturasProveedor.__ObtenerDetalleFactura(nroFacturaProv)
            return nroFacturaProv
        except models.Proveedor.DoesNotExist:
            res.CodigoOperacion = -2
            res.Mensaje = "Facturaa de Proveedor no existe"
            return res

    def AnularFactura(nroFactura: int):
        res = modelsApp.Resultado()
        try:
            resFactura = models.Fact_Proveedor(models.Fact_Proveedor.objects.get(FAC_NUMERO = nroFactura))
            resFactura.FAC_VIGENCIA = False

            resFactura.save()
            res.CodigoOperacion = 200
            res.Mensaje = "Factura anulada"
            return res
        except models.Boleta.DoesNotExist:
            res.CodigoOperacion = -2
            res.Mensaje = "Factura no existe"
            return res

    def ListarFacturas():
        res = modelsApp.Resultado()
        try:
            resFacturas = map(ConvertidorTipos.ConvertirFacturaProveedor, list(models.Fact_Proveedor.objects.all()))
            return resFacturas
        except Exception as e:
            res.CodigoOperacion = -9
            res.Mensaje = str(e)
            return res