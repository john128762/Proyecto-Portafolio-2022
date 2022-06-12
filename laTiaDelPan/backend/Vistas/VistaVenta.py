from django.shortcuts import render
from backend import models
from backend import modelsApp
from backend.Controladores.ControladorVentas import ControladorVentas
from django.http import HttpResponseRedirect
from django.contrib import messages

def venta(request):
    return render(request, 'venta.html')

