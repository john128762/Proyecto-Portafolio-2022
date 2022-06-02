from datetime import date, time, datetime

#from backend.models import Producto

class Proveedor:
    RUT = ""
    Nombre = ""
    Contacto = ""
    Estado = False
    def __init__(self, rut = "", nombre = "", contacto = "", estado = False):
        self.RUT = rut
        self.Nombre = nombre
        self.Contacto = contacto
        self.Estado = estado

class Categoria:
    Id = 0
    Nombre = ""
    Descripcion = ""
    Estado = False
    def __init__(self, id = 0, nombre = "", descripcion = "", estado = False):
        self.Id = id
        self.Nombre = nombre
        self.Descripcion = descripcion
        self.Estado = estado

class Usuario:
    RUT = ""
    Username = ""
    Nombres = ""
    Apellidos = ""
    Password = ""
    Vigencia = False
    Administrador = False
    def __init__(self, rut = "", user = "", nombres = "", apellidos = "", password = "", vigencia = False, administrador = False):
        self.RUT = rut
        self.Username = user
        self.Nombres = nombres
        self.Apellidos = apellidos
        self.Password = password
        self.Vigencia = vigencia
        self.Administrador = administrador

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
            self.Codigo = codigo
            self.Nombre = nombre
            self.Valor = valor
            self.Stock = stock
            self.Prov = proveedor
            self.Cat = categoria
            self.Estado = estado
        else:
            raise TypeError("El parametro categoria ingresado no es de tipo Categoria")

class DetalleBoleta:
    Prod = Producto()
    Cantidad = 0
    Valor = 0
    def __init__(self, producto: Producto = Producto(), cantidad = 0, valor = 0):
        self.Prod = producto
        self.Cantidad = cantidad
        self.Valor = valor

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
            self.Numero = numero
            self.FechaVenta = fechaventa
            self.Subtotal = subtotal
            self.Iva = iva
            self.Vigencia = vigencia
            self.Vendedor = vendedor
            self.Detalle = detalle
        else:
            raise TypeError ("El parametro vendedor ingresado no es de tipo Usuario")

class DetalleFacturaProveedor:
    Prod = Producto()
    Cantidad = 0
    Valor = 0
    def __init__(self, producto: Producto = Producto(), cantidad = 0, valor = 0):
        self.Prod = producto,
        self.Cantidad = cantidad,
        self.Valor = valor

class FacturaProveedor():
    Numero = 0
    FechaVenta = datetime.min
    Total = 0
    Detalle = [DetalleFacturaProveedor]
    def __init__(self, numero = 0, fechaventa: datetime = datetime.min, total = 0, detalle = None):
        self.Numero = numero
        self.FechaVenta = fechaventa
        self.Total = total
        self.Detalle = detalle

class VistaVentasPorMes:
    Periodo = ""
    Producto = ""
    Cantidad = 0
    Total = 0
    def __init__(self, periodo, producto, cantidad):
        self.Periodo = periodo
        self.Producto = producto
        self.Cantidad = cantidad
    def __init__(self):
        Periodo = ""
        Producto = ""
        Cantidad = 0
        Total = 0

class IngresosPorMes:
    Periodo = ""
    Ventas = 0
    def __init__(self, periodo, ventas):
        self.Periodo = periodo
        self.Ventas = ventas
    def __init__(self):
        Periodo = ""
        Ventas = 0        

class GastosPorMes:
    Periodo = ""
    GastosProveedor = 0
    GastosIva = 0
    def __init__(self, periodo, gastosProveedor, gastosIva):
        self.Periodo = periodo
        self.GastosProveedor = gastosProveedor
        self.GastosIva = gastosIva
    def __init__(self):
        Periodo = ""
        GastosProveedor = 0
        GastosIva = 0

class Resultado:
    CodigoOperacion = 0
    Mensaje = ""
    def __init__(self, codigo, mensaje):
        self.CodigoOperacion = codigo
        self.Mensaje = mensaje
    def __init__(self):
        Periodo = ""
        GastosProveedor = 0
        GastosIva = 0