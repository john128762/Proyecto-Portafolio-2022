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
    CAT_DESCRIPCION = models.CharField(max_length=100)
    CAT_ESTADO = models.BooleanField()
    def __str__(self):
        return self.CAT_NOMBRE

class Usuario (models.Model):
    USU_RUT = models.IntegerField()
    USU_DV = models.CharField(max_length=1)
    USU_USERNAME = models.CharField(primary_key=True, max_length = 20, default="default")
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
    BOL_SUBTOTAL = models.DecimalField(decimal_places=0, max_digits=10)
    BOL_IVA = models.DecimalField(decimal_places=0, max_digits=10)
    BOL_VIGENCIA = models.BooleanField()
    USU_USERNAME = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Producto(models.Model):
    PROD_CODIGO = models.AutoField(primary_key=True)
    PROD_NOMBRE = models.CharField(max_length=40)
    PROD_VALOR = models.DecimalField(decimal_places=0, max_digits=10)
    PROD_STOCK = models.IntegerField()
    PROV_RUT = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    CAT_ID = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    PROD_ESTADO = models.BooleanField()
    def __str__(self):
        return self.PROD_NOMBRE

class Detalle_Boleta(models.Model):
    BOL_NUMERO = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    PROD_CODIGO = models.ForeignKey(Producto, on_delete=models.CASCADE)
    DET_CANTIDAD = models.IntegerField()
    DET_VALOR = models.DecimalField(decimal_places=0, max_digits=10)

class Fact_Proveedor(models.Model):
    FAC_NUMERO = models.AutoField(primary_key=True)
    FAC_FECHA_VENTA = models.DateTimeField()
    FAC_TOTAL = models.DecimalField(decimal_places=0, max_digits=10)
    FAC_VIGENCIA = models.BooleanField(default=False)
    USU_USERNAME = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Det_Fact_Proveedor(models.Model):
    FAC_NUMERO = models.ForeignKey(Fact_Proveedor, on_delete=models.CASCADE)
    PROD_CODIGO = models.ForeignKey(Producto, on_delete=models.CASCADE)
    DFT_CANTIDAD = models.IntegerField()
    DFT_VALOR = models.DecimalField(decimal_places=0, max_digits=10)

