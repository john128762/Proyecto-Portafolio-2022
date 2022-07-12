from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from tempfile import NamedTemporaryFile
import os
from decimal import Decimal
from backend.modelsApp import Boleta
from backend.modelsApp import DetalleBoleta
from backend.modelsApp import Producto

class GeneradorBoleta:

    def GenerarBoleta(boleta: Boleta):
        os.environ["INVOICE_LANG"] = "es"


        