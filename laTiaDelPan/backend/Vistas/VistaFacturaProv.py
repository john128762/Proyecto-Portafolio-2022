import json
from django.shortcuts import render
from backend import models
from backend import modelsApp
from backend.Vistas.FormFactura import FormFactura
from backend.Controladores.ControladorFacturasProveedor import ControladorFacturasProveedor
from backend.Controladores.ControladorProductos import ControladorProductos
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from django.utils import timezone

def factura(request):

    if "username" not in request.session:
        return HttpResponseRedirect("/")
    form = FormFactura()
    return render(request, 'facturaProveedor.html', {"form": form})

def postProducto(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    if is_ajax(request) and request.method == "POST":
        form = FormFactura(request.POST)
        if form.is_valid():
            #print(form.cleaned_data["codigo"])
            try:
                producto = ControladorProductos.LeerProducto(form.cleaned_data["codigo"])
                #print(producto.Codigo)
                #print(json.dumps(producto, cls=modelsApp.ProductoEncoder))
                serializado = serializarProducto(producto)
                #print(serializado)
                #print(serializado2)
                return JsonResponse({"instance": serializado}, status=200)
                #return JsonResponse({"instance": serializado2}, status=200)
            except models.Producto.DoesNotExist:
                #resultado = modelsApp.Resultado(-1, "El producto no existe.")
                messages.error(request, "El producto no existe.")
                #return JsonResponse("error": "El producto no existe.")
            #producto = ControladorProductos.LeerProducto(1)
            
            
        else:
            return JsonResponse({"error":form.errors}, status=400)
    return JsonResponse({"error": ""}, status=400)

def realizarFactura(request):
    if "username" not in request.session:
        return HttpResponseRedirect("/")
    if is_ajax(request) and request.method == "POST":
        print(request.session)
        body = request.body
        obj = json.loads(body)
        
        FacturaProveedor = modelsApp.FacturaProveedor()
        FacturaProveedor.FechaVenta = timezone.now()
        FacturaProveedor.Total = obj["factInTotal"]
        FacturaProveedor.Vigencia = True
        FacturaProveedor.Vendedor = modelsApp.Usuario(user=request.session["username"])
        FacturaProveedor.Detalle = []

        for detalle in obj["datos"]:
            FacturaProveedor.Detalle.append(modelsApp.DetalleFacturaProveedor(modelsApp.Producto(detalle["codigo"]), detalle["cantidad"], detalle["valor"]))

        res = ControladorFacturasProveedor.AgregarFactura(FacturaProveedor)

        if res.CodigoOperacion == 200:
            messages.success(request, res.Mensaje)
        else:
            messages.error(request, res.Mensaje)

    return HttpResponseRedirect('/facturaProveedor/')

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def serializarProducto(producto: modelsApp.Producto):
    #serializado = '"model": "backend.Producto", "pk: {pkField}, "fields": {fieldsField}]'
    strPK = '"pk": ' + str(producto.Codigo) + ','
    strFields = '"fields": ' + json.dumps(producto, cls=modelsApp.ProductoEncoder) + "}]"
    serializado = '[{"model": "backend.Producto", ' + strPK + strFields
    return serializado