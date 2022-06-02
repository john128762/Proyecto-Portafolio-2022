from ConvertidorTipos import ConvertidorTipos
from datetime import datetime
from backend import models
from backend import modelsApp

class ControladorFacturasProveedor:
    def AgregarFactura(factura: modelsApp.Factura):
        return 0