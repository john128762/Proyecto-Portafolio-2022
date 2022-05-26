from nis import cat
from smtplib import SMTPAuthenticationError
from urllib.request import CacheFTPHandler
from laTiaDelPan.backend.Controladores.MantenedorCategorias import MantenedorCategorias
import models
import modelsApp

class ConvertidorTipos:

    @staticmethod
    def ConvertirUsuario(usuarioBDD: models.Usuario) -> modelsApp.Usuario:
        usuario = modelsApp.Usuario(usuarioBDD.USU_RUT + "-" + usuarioBDD.USU_DV, usuarioBDD.USU_USERNAME, usuarioBDD.USU_NOMBRES, usuarioBDD.USU_APELLIDOS, usuarioBDD.USU_PASSWORD, usuarioBDD.USU_VIGENCIA, usuarioBDD.USU_ADMINISTRADOR)
        return usuario

    @staticmethod
    def ConvertirCategoria(categoriaBDD: models.Categoria) -> modelsApp.Categoria:
        categoria = modelsApp.Categoria(categoriaBDD.CAT_ID, categoriaBDD.CAT_NOMBRE, categoriaBDD.CAT_DESCRIPCION, categoriaBDD.CAT_ESTADO)
        return categoria
    
    @staticmethod
    def ConvertirProveedor(proveedorBDD: models.Proveedor) -> modelsApp.Proveedor:
        proveedor = modelsApp.Proveedor(proveedorBDD.PROV_RUT + "-" + proveedorBDD.PROV_DV, proveedorBDD.PROV_NOMBRE, proveedorBDD.PROV_CONTACTO, proveedorBDD.PROV_ESTADO)
        return proveedor
    
    @staticmethod
    def ConvertirProducto(productoBDD: models.Producto) -> modelsApp.Producto:
        producto = modelsApp.Producto(productoBDD.PROD_CODIGO, productoBDD.PROD_NOMBRE, productoBDD.PROD_VALOR, productoBDD.PROD_STOCK, ConvertidorTipos.ConvertirProveedor(models.Proveedor.objects.get(PROV_RUT = productoBDD.PROV_RUT)), ConvertidorTipos.ConvertirCategoria(models.Categoria.objects.get(CAT_ID = productoBDD.CAT_ID)), productoBDD.PROD_ESTADO)
        return producto
    
    @staticmethod
    def ConvertirBoleta(boletaBDD: models.Boleta) -> modelsApp.Boleta:
        boleta = modelsApp.Boleta(boletaBDD.BOL_NUMERO, boletaBDD.BOL_FECHA_VENTA, boletaBDD.BOL_SUBTOTAL, boletaBDD.BOL_IVA, boletaBDD.BOL_VIGENCIA, ConvertidorTipos.ConvertirUsuario(models.Usuario.objects.get(USU_USUARIO = boletaBDD.USU_USERNAME)))
        return boleta