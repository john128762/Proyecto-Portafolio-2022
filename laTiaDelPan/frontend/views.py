from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def paginaPrincipal(request):
    return render(request, 'paginaPrincipal.html')

def analisisVenta(request):
    return render(request, 'analisisVentas.html')

def registrarse(request):
    return render(request, 'registrarse.html')