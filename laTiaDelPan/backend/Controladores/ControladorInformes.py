from pyexpat import model
import models
import modelsApp
from django.db import connection

class ControladorInformes:
    def ObtenerVentasMes(periodo):
        resultado = list()
        query = """SELECT TO_CHAR(BOL.BOL_FECHA_VENTA, 'MM/YYYY') AS PERIODO, PRD.PROD_NOMBRE AS PRODUCTO, COUNT(DET.PROD_CODIGO) AS CANTIDAD, SUM(DET.DET_VALOR) AS TOTAL
FROM DETALLE_BOLETA DET
INNER JOIN BOLETA BOL ON (DET.BOL_NUMERO = BOL.BOL_NUMERO)
INNER JOIN PRODUCTO PRD ON (DET.PROD_CODIGO = PRD.PROD_CODIGO)
WHERE TO_CHAR(BOL.BOL_FECHA_VENTA, 'MM/YYYY') = %s
GROUP BY TO_CHAR(BOL.BOL_FECHA_VENTA, 'MM/YYYY'), PRD.PROD_NOMBRE"""
        with connection.cursor() as cursor:
            cursor.execute(query, [periodo])
        return resultado

    def ObtenerIngresosMes(periodo):
        resultado = modelsApp.IngresosPorMes()
        return resultado

    def ObtenerGastosMes(periodo):
        resultado = modelsApp.GastosPorMes()
        return resultado

    def ObtenerVentasAño(año):
        resultado = list()
        return resultado

    def ObtenerIngresosAño(año):
        resultado = list()
        return resultado

    def ObtenerGastosAño(año):
        resultado = list()
        return resultado