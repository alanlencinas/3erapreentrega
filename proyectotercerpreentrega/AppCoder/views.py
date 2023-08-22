from django.shortcuts import render
from .models import Perfumeria, Cuidadocorporal, Maquillaje, Cabello, Clientes
from django.http import HttpResponse
from .forms import perfumeria_Formulario, cuidado_Corporal_Formulario, maquillaje_Formulario, cabello_Formulario, clientes_Formulario

# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cabello(request):
    if request.method =="POST":
        form=cabello_Formulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            codigo = info["Codigo"]
            nombre=info["Nombre"]
            sexo=info["Sexo"]  
            precio=info["Precio"]
            cabello = Cabello(Codigo=codigo, Nombre=nombre, Sexo=sexo, Precio=precio)
            cabello.save()
            formulario_cabello=cabello_Formulario()
            return render(request, "AppCoder/cabello.html", {"mensaje":"Producto de Cabello Creado", "formulario":formulario_cabello})
        else:
           return render(request, "AppCoder/cabello.html", {"mensaje":"Datos Invalidos"}) 
    else:
        formulario_cabello = cabello_Formulario()
    return render(request, "AppCoder/cabello.html", {'formulario':formulario_cabello})

def maquillaje(request):
    if request.method =="POST":
        form=maquillaje_Formulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            codigo = info["Codigo"]
            nombre=info["Nombre"]  
            precio=info["Precio"]
            maquillaje = Maquillaje(Codigo=codigo, Nombre=nombre, Precio=precio)
            maquillaje.save()
            formulario_maquillaje=maquillaje_Formulario()
            return render(request, "AppCoder/maquillaje.html", {"mensaje":"Maquillaje Creado", "formulario":formulario_maquillaje})
        else:
           return render(request, "AppCoder/maquillaje.html", {"mensaje":"Datos Invalidos"}) 
    else:
        formulario_maquillaje = maquillaje_Formulario()
    return render(request, "AppCoder/maquillaje.html", {'formulario':formulario_maquillaje})


def perfumeria(request):
    if request.method =="POST":
        form=perfumeria_Formulario(request.POST)
        if form.is_valid():
          info=form.cleaned_data
          codigo = info["Codigo"]
          nombre=info["Nombre"]  
          sexo=info["Sexo"]
          precio=info["Precio"]
          perfume = Perfumeria(Codigo=codigo, Nombre=nombre, Sexo=sexo, Precio=precio)
          perfume.save()
          formulario_perfumeria= perfumeria_Formulario
          return render(request, "AppCoder/perfumeria.html", {"mensaje":"Perfume Creado", "formulario":formulario_perfumeria})
        return render(request, "AppCoder/perfumeria.html", {'mensaje':'Datos Invalidos'})
    else:
        formulario_perfumeria = perfumeria_Formulario()
        return render(request, "AppCoder/perfumeria.html", {'formulario':formulario_perfumeria})
            
            
def clientes(request):
    if request.method =="POST":
        form=clientes_Formulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            apellido = info["Apellido"]
            nombre=info["Nombre"]
            dni=info["DNI"]  
            email=info["Email"]
            clientes = Clientes(Apellido=apellido, Nombre=nombre, DNI=dni, Email=email)
            clientes.save()
            formulario_clientes=clientes_Formulario()
            return render(request, "AppCoder/clientes.html", {"mensaje":"Cliente Creado", "formulario":formulario_clientes})
        else:
           return render(request, "AppCoder/clientes.html", {"mensaje":"Datos Invalidos"}) 
    else:
        formulario_clientes = clientes_Formulario()
    return render(request, "AppCoder/clientes.html", {'formulario':formulario_clientes}) 
    
def cuidadoCorporal(request):
    if request.method =="POST":
        form=cuidado_Corporal_Formulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            codigo = info["Codigo"]
            nombre=info["Nombre"]  
            sexo=info["Sexo"]
            precio=info["Precio"]
            cuidadocorporal = Cuidadocorporal(Codigo=codigo, Nombre=nombre, Sexo=sexo, Precio=precio)
            cuidadocorporal.save()
            formulario_cuidadocorporal=cuidado_Corporal_Formulario()
            return render(request, "AppCoder/cuidadocorporal.html", {"mensaje":"Cuidado Coporal Creado", "formulario":formulario_cuidadocorporal})
        else:
           return render(request, "AppCoder/cuidadocorporal.html", {"mensaje":"Datos Invalidos"}) 
    else:
        formulario_cuidadocorporal = cuidado_Corporal_Formulario()
    return render(request, "AppCoder/cuidadocorporal.html", {'formulario':formulario_cuidadocorporal})
        
        
