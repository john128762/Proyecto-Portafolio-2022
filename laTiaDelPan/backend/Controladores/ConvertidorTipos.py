from backend import models
from backend import modelsApp

class ConvertidorTipos:

    @staticmethod
    def FormatearRUT(rut: str):
        if "-" in rut:
            cuerpo = int(rut.split("-")[0])
            dv = rut.split("-")[1]
            cuerpo = "{:,}".format(cuerpo).replace(",",".")
            return cuerpo + "-" + dv
        else:
            return rut

    @staticmethod
    def ConvertirUsuario(usuarioBDD: models.Usuario) -> modelsApp.Usuario:
        usuario = modelsApp.Usuario(ConvertidorTipos.FormatearRUT(str(usuarioBDD.USU_RUT) + "-" + usuarioBDD.USU_DV), usuarioBDD.USU_USERNAME, usuarioBDD.USU_NOMBRES, usuarioBDD.USU_APELLIDOS, usuarioBDD.USU_PASSWORD, usuarioBDD.USU_VIGENCIA, usuarioBDD.USU_ADMINISTRADOR)
        return usuario

    @staticmethod
    def ConvertirCategoria(categoriaBDD: models.Categoria) -> modelsApp.Categoria:
        categoria = modelsApp.Categoria(categoriaBDD.CAT_ID, categoriaBDD.CAT_NOMBRE, categoriaBDD.CAT_DESCRIPCION, categoriaBDD.CAT_ESTADO)
        return categoria
    
    @staticmethod
    def ConvertirProveedor(proveedorBDD: models.Proveedor) -> modelsApp.Proveedor:
        proveedor = modelsApp.Proveedor(ConvertidorTipos.FormatearRUT(str(proveedorBDD.PROV_RUT) + "-" + str(proveedorBDD.PROV_DV)), proveedorBDD.PROV_NOMBRE, proveedorBDD.PROV_CONTACTO, proveedorBDD.PROV_ESTADO)
        return proveedor
    
    @staticmethod
    def ConvertirProducto(productoBDD: models.Producto) -> modelsApp.Producto:
        producto = modelsApp.Producto(productoBDD.PROD_CODIGO, productoBDD.PROD_NOMBRE, productoBDD.PROD_VALOR, productoBDD.PROD_STOCK, ConvertidorTipos.ConvertirProveedor(productoBDD.PROV_RUT), ConvertidorTipos.ConvertirCategoria( productoBDD.CAT_ID), productoBDD.PROD_ESTADO)
        return producto
    
    @staticmethod
    def ConvertirBoleta(boletaBDD: models.Boleta) -> modelsApp.Boleta:
        boleta = modelsApp.Boleta(boletaBDD.BOL_NUMERO, boletaBDD.BOL_FECHA_VENTA, boletaBDD.BOL_SUBTOTAL, boletaBDD.BOL_IVA, boletaBDD.BOL_VIGENCIA, ConvertidorTipos.ConvertirUsuario(models.Usuario.objects.get(USU_USUARIO = boletaBDD.USU_USERNAME)))
        return boleta
    
    @staticmethod
    def ConvertirDetalleBoleta(detalleBDD: models.Detalle_Boleta) -> modelsApp.DetalleBoleta:
        detalle = modelsApp.DetalleBoleta(ConvertidorTipos.ConvertirProducto(models.Producto.objects.get(COD_PRODUCTO = detalleBDD.PROD_CODIGO)), detalleBDD.DET_CANTIDAD, detalleBDD.DET_VALOR)
        return detalle

    @staticmethod
    def ConvertirFacturaProveedor(facturaBDD: models.Fact_Proveedor) -> modelsApp.FacturaProveedor:
        factura = modelsApp.FacturaProveedor(facturaBDD.FAC_NUMERO, facturaBDD.FAC_FECHA_VENTA, facturaBDD.FAC_TOTAL)
        return factura
    
    @staticmethod
    def ConvertirDetalleFacturaProveedor(detalleBDD: models.Det_Fact_Proveedor) -> modelsApp.DetalleFacturaProveedor:
        detalle = modelsApp.DetalleFacturaProveedor(ConvertidorTipos.ConvertirProducto(models.Producto.objects.get(COD_PRODUCTO = detalleBDD.PROD_CODIGO)), detalleBDD.DFT_CANTIDAD, detalleBDD.DFT_VALOR)
        return detalle
    
