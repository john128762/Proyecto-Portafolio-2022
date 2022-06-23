from django.shortcuts import render
from backend import models
from backend import modelsApp
from backend.Controladores.ControladorFacturasProveedor import ControladorFacturasProveedor
from django.http import HttpResponseRedirect
from django.contrib import messages

def factura(request, respuesta=None):
    list(messages.get_messages(request))
    dataFact = ControladorFacturasProveedor.ListarFacturas()
    fact = {'facturaT':dataFact}
    if isinstance(respuesta, modelsApp.Resultado):
        if respuesta.CodigoOperacion == 200:
            messages.success(request, respuesta.Mensaje)
        else:
            messages.error(request, respuesta.Mensaje)
    return render(request, 'facturaProveedor.html', fact)