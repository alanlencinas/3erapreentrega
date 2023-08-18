from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cabello(request):
    return render(request, 'AppCoder/cabello.html')

def cuidadocorporal(request):
    return render(request, 'AppCoder/cuidadocorporal.html')

def maquillaje(request):
    return render(request, 'AppCoder/maquillaje.html')

def perfumeria(request):
    return render(request, 'AppCoder/perfumeria.html')

def clientes(request):
    return render(request, 'AppCoder/clientes.html')