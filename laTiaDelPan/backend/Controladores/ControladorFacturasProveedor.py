from backend.Controladores.ConvertidorTipos import ConvertidorTipos
from datetime import datetime
from backend import models
from backend import modelsApp

class ControladorFacturasProveedor:
    def AgregarFactura(factura):
        if isinstance(factura, modelsApp.FacturaProveedor):
            res = modelsApp.Resultado()

            nuevaFactura = models.Fact_Proveedor()
            nuevaFactura.FAC_NUMERO = factura.Numero
            nuevaFactura.FAC_FECHA_VENTA = factura.FechaVenta
            nuevaFactura.FAC_TOTAL = factura.Total

            try: 
                nuevaFactura.save()

                for detalle in factura.Detalle:
                    nuevaFacturaDetalleProv = models.Det_Fact_Proveedor()
                    nuevaFacturaDetalleProv.PROD_CODIGO = models.Producto.objects.get(PROD_CODIGO = detalle.Prod)
                    nuevaFacturaDetalleProv.DFT_CANTIDAD = detalle.Cantidad
                    nuevaFacturaDetalleProv.DFT_VALOR = detalle.Valor
                    nuevaFacturaDetalleProv.save()

                res.CodigoOperacion = 200
                res.Mensaje = "La Factura del Proveedor ingresado."
                return res
            except:
                res.CodigoOperacion = -1
                res.Mensaje = "Error al ingresar la factura del proveedor."
                return res
        else:
            raise TypeError("El parametro Detalle Factura Proveedor no es del tipo esperado")

    def __ObtenerDetalleFactura(nroFacturaProv: int):
        resDetalle = map(ConvertidorTipos.ConvertirDetalleFacturaProveedor, list(models.Det_Fact_Proveedor.objects.filter(FAC_NUMERO = nroFacturaProv)))
        return resDetalle

    def LeerVenta(nroFacturaProv: int):
        res = modelsApp.Resultado()
        try:
            respuesta = models.Fact_Proveedor(models.Fact_Proveedor.objects.get(FAC_NUMERO = nroFacturaProv))
            resFactura = ConvertidorTipos.ConvertirFacturaProveedor(respuesta)
            resFactura.Detalle = ControladorFacturasProveedor.__ObtenerDetalleVenta(nroFacturaProv)
            return nroFacturaProv
        except models.Proveedor.DoesNotExist:
            res.CodigoOperacion = -2
            res.Mensaje = "Facturaa de Proveedor no existe"
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