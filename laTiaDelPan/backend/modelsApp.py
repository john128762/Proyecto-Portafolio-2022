from datetime import date, time, datetime

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

class Categoria:
    Id = 0
    Nombre = ""
    Estado = False
    def __init__(self, id, nombre, estado):
        Id = id
        Nombre = nombre
        Estado = estado

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

class Boleta:
    Numero = 0
    FechaVenta = datetime.min
    Subtotal = 0
    Iva = 0
    Vigencia = False
    Vendedor = Usuario()
    def __init__(self, numero, fechaventa, subtotal, iva, vigencia, vendedor):
        if isinstance(vendedor, Usuario):
            Numero = numero
            FechaVenta = fechaventa
            Subtotal = subtotal
            Iva = iva
            Vigencia = vigencia
            Vendedor = vendedor
        else:
            raise TypeError ("El parametro vendedor ingresado no es de tipo Usuario")

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

class VistaVentasPorMes:
    Periodo = ""
    Producto = ""
    Cantidad = 0
    Total = 0
    def __init__(self, periodo, producto, cantidad):
        Periodo = periodo
        Producto = producto
        Cantidad = cantidad

class IngresosPorMes:
    Periodo = ""
    Ventas = 0
    def __init__(self, periodo, ventas):
        Periodo = periodo
        Ventas = ventas

class GastosPorMes:
    Periodo = ""
    GastosProveedor = 0
    GastosIva = 0
    def __init__(self, periodo, gastosProveedor, gastosIva):
        Periodo = periodo
        gastosProveedor = gastosProveedor
        GastosIva = gastosIva

class Resultado:
    CodigoOperacion = 0
    Mensaje = ""
    def __init__(self, codigo, mensaje):
        CodigoOperacion = codigo
        Mensaje = mensaje