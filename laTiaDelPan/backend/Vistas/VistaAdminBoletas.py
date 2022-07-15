from decimal import Decimal
import json
from django.shortcuts import render
from backend import modelsApp
from backend.Vistas.FormVenta import FormVenta
from backend.Controladores.ControladorVentas import ControladorVentas
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.utils import timezone
from django.contrib import messages

#from laTiaDelPan.backend.views import Producto


def adminBoletas(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    dataBoleta = ControladorVentas.ListarVentas()
    return render(request, 'adminBoletas.html', {"dataBoletaT":dataBoleta})

def postBoleta(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    if is_ajax(request) and request.method == "POST":
        NroBoleta = int(json.loads(request.body)["nro_boleta"])
        try:
            Respuesta = ControladorVentas.LeerVenta(NroBoleta)
            if(isinstance(Respuesta, modelsApp.Boleta)):
                serializado = serializarBoleta(Respuesta)
                print(serializado)
                return JsonResponse({"instance":serializado}, status=200)
            else:
                return JsonResponse({"error": "Error: " + Respuesta.Mensaje}, status=500)
        except Exception as ex:
            return JsonResponse({"error: serverError"}, status=500)
    return JsonResponse({"error": ""}, status=400)

def anularBoleta(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    if request.method == "POST":
        numBoleta = int(request.POST["numBoleta"])
        res = ControladorVentas.AnularVenta(numBoleta)
        if isinstance(res, modelsApp.Resultado):
            if res.CodigoOperacion == 200:
                messages.success(request, f"La boleta N°{numBoleta} fue anulada.")
            else:
                messages.error(request, f"Error al anular la boleta N°{numBoleta}.")

    return HttpResponseRedirect('/adminBoletas/')

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def serializarBoleta(boleta: modelsApp.Boleta):
    nroBoleta = str(boleta.Numero)
    if not boleta.Vigencia:
        nroBoleta += " (ANULADA)"
    vendedor = boleta.Vendedor.Nombres + " " + boleta.Vendedor.Apellidos
    subTotal = str(boleta.Subtotal)
    iva = str(boleta.Iva)
    total = str(Decimal(subTotal) + Decimal(iva))
    detalleBoleta = []

    detalle: modelsApp.DetalleBoleta
    for detalle in boleta.Detalle:
        detalleBoleta.append({"producto" : detalle.Prod.Nombre, "valor" : str(detalle.Valor), "cantidad":str(detalle.Cantidad)})
    
    objeto = [{"model":"backend.Producto", "pk":str(nroBoleta), "fields":{"nroBoleta": nroBoleta, "vendedor": vendedor, "subTotal":subTotal,"iva":iva,"total":total, "detalleBoleta":detalleBoleta}}]
    serializado = json.dumps(objeto)
    return serializado