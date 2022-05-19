from django.db import models

# Create your models here.
class Proveedor(models.Model):
    PROV_RUT = models.IntegerField(primary_key=True)
    PROV_DV = models.CharField(max_length = 1)
    PROV_NOMBRE = models.CharField(max_length=40)
    PROV_CONTACTO = models.CharField(max_length=40)
    PROV_ESTADO = models.BooleanField()

class Categoria(models.Model):
    CAT_ID = models.AutoField(primary_key=True)
    CAT_NOMBRE = models.CharField(max_length=20)
    CAT_ESTADO = models.BooleanField()

class Usuario (models.Model):
    USU_RUT = models.IntegerField(primary_key=True)
    USU_DV = models.CharField(max_length=1)
    USU_USERNAME = models.CharField(max_length = 20)
    USU_NOMBRES = models.CharField(max_length = 40)
    USU_APELLIDOS = models.CharField(max_length = 40)
    USU_PASSWORD = models.CharField(max_length = 40)
    USU_VIGENCIA = models.BooleanField()
    USU_ADMINISTRADOR = models.BooleanField()
    USU_FECHA_INGRESO = models.DateTimeField()
    USU_FECHA_MODIFICACION = models.DateTimeField()

class Boleta (models.Model):
    BOL_NUMERO = models.AutoField(primary_key=True)
    BOL_FECHA_VENTA = models.DateTimeField()
    BOL_SUBTOTAL = models.DecimalField()
    BOL_IVA = models.DecimalField()
    BOL_VIGENCIA = models.BooleanField()
    USU_RUT = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Producto(models.Model):
    PROD_CODIGO = models.CharField(max_length = 15, primary_key=True)
    PROD_NOMBRE = models.CharField(max_length=40)
    PROD_VALOR = models.DecimalField()
    PROD_STOCK = models.IntegerField()
    PROV_RUT = models.ForeignKey(Proveedor, on_delete=models.RESTRICT)
    CAT_ID = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    PROD_ESTADO = models.BooleanField()

class Detalle_Boleta(models.Model):
    BOL_NUMERO = models.ForeignKey(Boleta, on_delete=models.RESTRICT)
    PROD_CODIGO = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    DET_CANTIDAD = models.IntegerField()
    DET_VALOR = models.DecimalField()

class Fact_Proveedor(models.Model):
    FAC_NUMERO = models.AutoField(primary_key=True)
    FAC_FECHA_VENTA = models.DateTimeField()
    FAC_TOTAL = models.DecimalField()

class Det_Fact_Proveedor(models.Model):
    FAC_NUMERO = models.ForeignKey(Fact_Proveedor, on_delete=models.RESTRICT)
    PROD_CODIGO = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    DFT_CANTIDAD = models.IntegerField()
    DFT_VALOR = models.DecimalField()