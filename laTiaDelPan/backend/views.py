from django.shortcuts import render

# Create your views here.

def registrarse(request):
    return render(request, 'registrarse.html')

def categoria(request):
    return render(request, 'categoria.html')