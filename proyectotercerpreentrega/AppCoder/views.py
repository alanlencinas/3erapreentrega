from django.shortcuts import render
from .models import Perfumeria
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
    perfumes = Perfumeria.objects.all()
    return render(request, 'AppCoder/perfumeria.html', {'perfumes': perfumes})

def clientes(request):
    return render(request, 'AppCoder/clientes.html')