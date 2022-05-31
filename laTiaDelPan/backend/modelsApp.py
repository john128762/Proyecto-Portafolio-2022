from datetime import date, time, datetime

from backend.models import Producto

class Proveedor:
    RUT = ""
    Nombre = ""
    Contacto = ""
    Estado = False
    def __init__(self, rut, nombre, contacto, estado):
        RUT = rut
        Nombre = nombre
        Contacto = contacto
        Estado = estado
    def __init__(self):
        RUT = ""
        Nombre = ""
        Contacto = ""
        Estado = False

class Categoria:
    Id = 0
    Nombre = ""
    Descripcion = ""
    Estado = False
    def __init__(self, id, nombre, descripcion, estado):
        Id = id
        Nombre = nombre
        Descripcion = descripcion
        Estado = estado
    
    def __init__(self):
        Id = 0
        Nombre = ""
        Descripcion = ""
        Estado = False

class Usuario:
    RUT = ""
    Username = ""
    Nombres = ""
    Apellidos = ""
    Password = ""
    Vigencia = False
    Administrador = False
    def __init__(self, rut, user, nombres, apellidos, password, vigencia, administrador):
        RUT = rut
        Username = user
        Nombres = nombres
        Apellidos = apellidos
        Password = password
        Vigencia = vigencia
        Administrador = administrador
    def __init__(self):
        RUT = ""
        Username = ""
        Nombres = ""
        Apellidos = ""
        Password = ""
        Vigencia = False
        Administrador = False

class DetalleBoleta:
    Prod = Producto()
    Cantidad = 0
    Valor = 0
    def __init__(self, producto: Producto, cantidad, valor):
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
    def __init__(self, numero, fechaventa, subtotal, iva, vigencia, vendedor, detalle):
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
    def __init__(self):
        Numero = 0
        FechaVenta = datetime.min
        Subtotal = 0
        Iva = 0
        Vigencia = False
        Vendedor = Usuario()
        Detalle = [DetalleBoleta]

class Producto:
    Codigo = 0
    Nombre = ""
    Valor = 0
    Stock = 0
    Rut = ""
    Prov = Proveedor()
    Cat = Categoria()
    Estado = False
    def __init__(self, codigo, nombre, valor, stock, proveedor: Proveedor, categoria: Categoria, estado):
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
    def __init__(self):
        Codigo = 0
        Nombre = ""
        Valor = 0
        Stock = 0
        Rut = ""
        Prov = Proveedor()
        Cat = Categoria()
        Estado = False

class DetalleFacturaProveedor:
    Prod = Producto()
    Cantidad = 0
    Valor = 0
    def __init__(self, producto: Producto, cantidad, valor):
        Prod = producto,
        Cantidad = cantidad,
        Valor = valor
    def __init__(self):
        Prod = Producto()
        Cantidad = 0
        Valor = 0

class FacturaProveedor():
    Numero = 0
    FechaVenta = datetime.min
    Total = 0
    Detalle = [DetalleFacturaProveedor]
    def __init__(self, numero, fechaventa: datetime, total, detalle: list):
        Numero = numero
        FechaVenta = fechaventa
        Total = total
        Detalle = detalle
    def __init__(self):
        Numero = 0
        FechaVenta = datetime.min
        Total = 0
        Detalle = [DetalleFacturaProveedor]

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