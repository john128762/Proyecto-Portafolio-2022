from datetime import date, time, datetime

#from backend.models import Producto

class Proveedor:
    RUT = ""
    Nombre = ""
    Contacto = ""
    Estado = False
    def __init__(self, rut = "", nombre = "", contacto = "", estado = False):
        RUT = rut
        Nombre = nombre
        Contacto = contacto
        Estado = estado

class Categoria:
    Id = 0
    Nombre = ""
    Descripcion = ""
    Estado = False
    def __init__(self, id = 0, nombre = "", descripcion = "", estado = False):
        Id = id
        Nombre = nombre
        Descripcion = descripcion
        Estado = estado

class Usuario:
    RUT = ""
    Username = ""
    Nombres = ""
    Apellidos = ""
    Password = ""
    Vigencia = False
    Administrador = False
    def __init__(self, rut = "", user = "", nombres = "", apellidos = "", password = "", vigencia = False, administrador = False):
        RUT = rut
        Username = user
        Nombres = nombres
        Apellidos = apellidos
        Password = password
        Vigencia = vigencia
        Administrador = administrador

class Producto:
    Codigo = 0
    Nombre = ""
    Valor = 0
    Stock = 0
    Prov = Proveedor()
    Cat = Categoria()
    Estado = False
    def __init__(self, codigo = 0, nombre = "", valor = 0, stock = 0, proveedor: Proveedor = Proveedor(), categoria: Categoria = Categoria(), estado = False):
        if isinstance(categoria, Categoria):
            Codigo = codigo
            Nombre = nombre
            Valor = valor
            Stock = stock
            Prov = proveedor
            Cat = categoria
            Estado = estado
        else:
            raise TypeError("El parametro categoria ingresado no es de tipo Categoria")

class DetalleBoleta:
    Prod = Producto()
    Cantidad = 0
    Valor = 0
    def __init__(self, producto: Producto = Producto(), cantidad = 0, valor = 0):
        Prod = producto
        Cantidad = cantidad
        Valor = valor
    def __init__(self):
        Prod = Producto()
        Cantidad = 0
        Valor = 0

class Boleta:
    Numero = 0
    FechaVenta = datetime.min
    Subtotal = 0
    Iva = 0
    Vigencia = False
    Vendedor = Usuario()
    Detalle = [DetalleBoleta]
    def __init__(self, numero = 0, fechaventa = datetime.min, subtotal = 0, iva = 0, vigencia = False, vendedor = Usuario(), detalle = None):
        if isinstance(vendedor, Usuario):
            Numero = numero
            FechaVenta = fechaventa
            Subtotal = subtotal
            Iva = iva
            Vigencia = vigencia
            Vendedor = vendedor
            Detalle = detalle
        else:
            raise TypeError ("El parametro vendedor ingresado no es de tipo Usuario")

class DetalleFacturaProveedor:
    Prod = Producto()
    Cantidad = 0
    Valor = 0
    def __init__(self, producto: Producto = Producto(), cantidad = 0, valor = 0):
        Prod = producto,
        Cantidad = cantidad,
        Valor = valor

class FacturaProveedor():
    Numero = 0
    FechaVenta = datetime.min
    Total = 0
    Detalle = [DetalleFacturaProveedor]
    def __init__(self, numero = 0, fechaventa: datetime = datetime.min, total = 0, detalle = None):
        Numero = numero
        FechaVenta = fechaventa
        Total = total
        Detalle = detalle

class VistaVentasPorMes:
    Periodo = ""
    Producto = ""
    Cantidad = 0
    Total = 0
    def __init__(self, periodo, producto, cantidad):
        Periodo = periodo
        Producto = producto
        Cantidad = cantidad
    def __init__(self):
        Periodo = ""
        Producto = ""
        Cantidad = 0
        Total = 0

class IngresosPorMes:
    Periodo = ""
    Ventas = 0
    def __init__(self, periodo, ventas):
        Periodo = periodo
        Ventas = ventas
    def __init__(self):
        Periodo = ""
        Ventas = 0        

class GastosPorMes:
    Periodo = ""
    GastosProveedor = 0
    GastosIva = 0
    def __init__(self, periodo, gastosProveedor, gastosIva):
        Periodo = periodo
        gastosProveedor = gastosProveedor
        GastosIva = gastosIva
    def __init__(self):
        Periodo = ""
        GastosProveedor = 0
        GastosIva = 0

class Resultado:
    CodigoOperacion = 0
    Mensaje = ""
    def __init__(self, codigo, mensaje):
        CodigoOperacion = codigo
        Mensaje = mensaje
    def __init__(self):
        Periodo = ""
        GastosProveedor = 0
        GastosIva = 0