from decimal import Decimal
import json
from django.shortcuts import render
from backend import modelsApp
from backend.Vistas.FormVenta import FormVenta
from backend.Controladores.ControladorVentas import ControladorVentas
from backend.Controladores.ControladorProductos import ControladorProductos
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.utils import timezone

#from laTiaDelPan.backend.views import Producto


def venta(request):
    request.session['username'] = "username"
    form = FormVenta()
    return render(request, 'venta.html', {"form": form})

def postProducto(request):
    if is_ajax(request) and request.method == "POST":
        form = FormVenta(request.POST)
        if form.is_valid():
            #print(form.cleaned_data["codigo"])
            try:
                respuesta = ControladorProductos.LeerProducto(form.cleaned_data["codigo"])
                if (isinstance(respuesta, modelsApp.Producto) and respuesta.Estado == True):
                    if(respuesta.Stock > 0):
                        serializado = serializarProducto(respuesta)
                        return JsonResponse({"instance": serializado}, status=200)
                    else:
                        return JsonResponse({"error":"noStock"})
                else:
                    return JsonResponse({"error": "doesNotExist"})
            except Exception as ex:
                return JsonResponse({"error": "Error al buscar producto: " + str(ex)}, status=500)
        else:
            return JsonResponse({"error":form.errors}, status=400)
    return JsonResponse({"error": ""}, status=400)

def realizarVenta(request):
    if is_ajax(request) and request.method == "POST":
        body = request.body
        obj = json.loads(body)
        
        Boleta = modelsApp.Boleta()
        Boleta.FechaVenta = timezone.now()
        Boleta.Subtotal = Decimal(obj["subtotal"])
        Boleta.Iva = Decimal(obj["iva"])
        Boleta.Vigencia = True
        Boleta.Vendedor = modelsApp.Usuario(user=request.session["username"])
        Boleta.Detalle = []

        for detalle in obj["datos"]:
            Boleta.Detalle.append(modelsApp.DetalleBoleta(modelsApp.Producto(detalle["codigo"]), int(detalle["cantidad"]), Decimal(detalle["valor"])))

        res = ControladorVentas.RealizarVenta(Boleta)

        if isinstance(res, modelsApp.Resultado):
            if res.CodigoOperacion == 200:
                return JsonResponse(status=200, data={"info":"success"})
            else:
                return JsonResponse(status=500, data={"error":"Error al realizar la venta " + res.Mensaje})

    return HttpResponseRedirect('/venta/')

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def serializarProducto(producto: modelsApp.Producto):
    strPK = '"pk": ' + str(producto.Codigo) + ','
    strFields = '"fields": ' + json.dumps(producto, cls=modelsApp.ProductoEncoder) + "}]"
    serializado = '[{"model": "backend.Producto", ' + strPK + strFields
    print(serializado)
    return serializado