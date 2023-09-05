from django.shortcuts import render
from .models import Perfumeria, Cuidadocorporal, Maquillaje, Cabello, Clientes
from django.http import HttpResponse
from .forms import perfumeria_Formulario, cuidado_Corporal_Formulario, maquillaje_Formulario, cabello_Formulario, clientes_Formulario, RegistroUsuario_Formulario, UserEditForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
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
            mensaje = "Produco de Cabello Creado"
        else:
            mensaje = "Datos Inválidos"
    else:
        mensaje = None
    formulario_cabello = cabello_Formulario()
    cabellos = Cabello.objects.all()
    return render(request, "AppCoder/cabello.html", {'formulario':formulario_cabello, 'mensaje': mensaje, 'cabellos':cabellos})


def eliminarcabello(request, id):
    cabello = Cabello.objects.get(id=id)
    cabello.delete()
    cabellos = Cabello.objects.all()
    formulario_cabello = cabello_Formulario()
    mensaje = 'Producto de Cabello Eliminado'
    return render(request, "AppCoder/cabello.html", {"mensaje": mensaje, "formulario": formulario_cabello, "cabellos": cabellos})    

def editarcabello(request, id):
    cabello = Cabello.objects.get(id=id)
    if request.method=='POST':
        form=cabello_Formulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            cabello.Codigo = info["Codigo"]
            cabello.Nombre = info["Nombre"]
            cabello.Sexo = info["Sexo"]  
            cabello.Precio = info["Precio"]
            cabello.save()
            mensaje = "Produco de Cabello editado"
            cabellos = Cabello.objects.all()
            formulario_cabello = cabello_Formulario()
            return render(request, "AppCoder/cabello.html", {"formulario": formulario_cabello, "cabellos":cabellos, "mensaje": mensaje})
    else:
        formulario_cabello = cabello_Formulario(initial={"Codigo": cabello.Codigo, "Nombre": cabello.Nombre, "Sexo": cabello.Sexo, "Precio": cabello.Precio})
        return render(request, "AppCoder/editarcabello.html", {"formulario": formulario_cabello, "cabellos":cabello})

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
            mensaje = "Maquillaje Creado"
        else:
            mensaje = "Datos Inválidos"
    else:
        mensaje= None
    formulario_maquillaje = maquillaje_Formulario()
    maquillajes = Maquillaje.objects.all() 
    return render(request, "AppCoder/maquillaje.html", {'formulario':formulario_maquillaje, 'mensaje':mensaje, 'maquillajes':maquillajes})

def eliminarmaquillaje(request, id):
    maquillaje = Maquillaje.objects.get(id=id)
    maquillaje.delete()
    maquillajes = Maquillaje.objects.all()
    formulario_maquillaje = maquillaje_Formulario()
    mensaje = 'Producto de Maquillaje Eliminado'
    return render(request, "AppCoder/maquillaje.html", {"mensaje": mensaje, "formulario": formulario_maquillaje, "maquillajes": maquillajes})

def editarmaquillaje(request, id):
    maquillaje = Maquillaje.objects.get(id=id)
    if request.method == 'POST':
        form = maquillaje_Formulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            maquillaje.Codigo = info["Codigo"]
            maquillaje.Nombre = info["Nombre"]
            maquillaje.Precio = info["Precio"]
            maquillaje.save()
            mensaje = "Producto de maquillaje editado"
            maquillajes = Maquillaje.objects.all()
            formulario_maquillaje = maquillaje_Formulario()
            return render(request, "AppCoder/maquillaje.html", {"formulario": formulario_maquillaje, "maquillajes":maquillajes, "mensaje": mensaje})
    else:
        formulario_maquillaje = maquillaje_Formulario(initial={"Codigo": maquillaje.Codigo, "Nombre": maquillaje.Nombre, "Precio": maquillaje.Precio})
        return render(request, "AppCoder/editarmaquillaje.html", {"formulario": formulario_maquillaje, "maquillajes":maquillaje})
    


def perfumeria(request):
    if request.method == "POST":
        form = perfumeria_Formulario(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            codigo = info["Codigo"]
            nombre = info["Nombre"]
            sexo = info["Sexo"]
            precio = info["Precio"]
            perfume = Perfumeria(Codigo=codigo, Nombre=nombre, Sexo=sexo, Precio=precio)
            perfume.save()
            mensaje = "Perfume Creado"
        else:
            mensaje = "Datos Inválidos"
    else:
        mensaje = None
    formulario_perfumeria = perfumeria_Formulario()
    perfumeria = Perfumeria.objects.all()
    return render(request, "AppCoder/perfumeria.html", {"mensaje": mensaje, "formulario": formulario_perfumeria, "perfumeria": perfumeria})


def eliminarperfume(request, id):
    perfume = Perfumeria.objects.get(id=id)
    perfume.delete()
    perfumeria = Perfumeria.objects.all()
    formulario_perfume = perfumeria_Formulario()
    mensaje = 'Perfume Eliminado'
    return render(request, "AppCoder/perfumeria.html", {"mensaje": mensaje, "formulario": formulario_perfume, "perfumeria": perfumeria})


def editarperfume(request, id):
    perfume = Perfumeria.objects.get(id=id)
    if request.method=='POST':
        form=perfumeria_Formulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            perfume.Codigo = info["Codigo"]
            perfume.Nombre = info["Nombre"]
            perfume.Sexo = info["Sexo"]  
            perfume.Precio = info["Precio"]
            perfume.save()
            mensaje = "Perfume editado"
            perfumes = Perfumeria.objects.all()
            formulario_perfumeria = perfumeria_Formulario()
            return render(request, "AppCoder/perfumeria.html", {"formulario": formulario_perfumeria, "perfumeria":perfumes, "mensaje": mensaje})
    else:
        formulario_perfumeria = perfumeria_Formulario(initial={"Codigo": perfume.Codigo, "Nombre": perfume.Nombre, "Sexo": perfume.Sexo, "Precio": perfume.Precio})
        return render(request, "AppCoder/editarperfume.html", {"formulario": formulario_perfumeria, "perfumeria":perfume})    

            
            
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
            mensaje = "Cliente Creado"
        else:
            mensaje = "Datos Inválidos"
    else:
        mensaje = None
    formulario_clientes = clientes_Formulario()
    clientes = Clientes.objects.all()
    return render(request, "AppCoder/clientes.html", {'formulario':formulario_clientes, 'mensaje':mensaje, 'clientes': clientes}) 

def eliminarcliente(request, id):
    cliente = Clientes.objects.get(id=id)
    cliente.delete()
    clientes = Clientes.objects.all()
    formulario_clientes = clientes_Formulario()
    mensaje = 'Cliente Eliminado'
    return render(request, "AppCoder/clientes.html", {"mensaje": mensaje, "formulario": formulario_clientes, "clientes": clientes}) 


def editarcliente(request, id):
    cliente = Clientes.objects.get(id=id)
    if request.method == 'POST':
        form=clientes_Formulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            cliente.Apellido=info["Apellido"]
            cliente.Nombre=info["Nombre"]
            cliente.DNI=info["DNI"]
            cliente.Email=info["Email"]
            cliente.save()
            mensaje = "Cliente editado"
            clientes = Clientes.objects.all()
            formulario_cliente = clientes_Formulario()
            return render(request, "AppCoder/clientes.html", {"formulario": formulario_cliente, "clientes":clientes, "mensaje": mensaje})
    else:
        formulario_cliente = clientes_Formulario(initial={"Apellido": cliente.Apellido, "Nombre": cliente.Nombre, "DNI": cliente.DNI, "Email": cliente.Email})
        return render(request, "AppCoder/editarcliente.html", {"formulario": formulario_cliente, "clientes":cliente})    
            


    
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
            mensaje = "Producto Cuidado Corporal Creado"
        else:
            mensaje = "Datos Inválidos"
    else:
        mensaje = None
    formulario_cuidadocorporal = cuidado_Corporal_Formulario()
    cuidadoscorporales = Cuidadocorporal.objects.all()
    return render(request, "AppCoder/cuidadocorporal.html", {'formulario':formulario_cuidadocorporal, 'mensaje': mensaje, 'cuidadoscorporales': cuidadoscorporales})
        
def eliminarcuidadocorporal(request, id):
    cuidadocorporal = Cuidadocorporal.objects.get(id=id)
    cuidadocorporal.delete()
    cuidadoscorporales = Cuidadocorporal.objects.all()
    formulario_cuidadocorporal = cuidado_Corporal_Formulario()
    mensaje = 'Producto Cuidado Corporal Eliminado'
    return render(request, "AppCoder/cuidadocorporal.html", {"mensaje": mensaje, "formulario": formulario_cuidadocorporal, "cuidadoscorporales": cuidadoscorporales})

def editarcuidadocorporal(request, id):
    cuidadocorporal = Cuidadocorporal.objects.get(id=id)
    if request.method == 'POST':
        form=cuidado_Corporal_Formulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            cuidadocorporal.Codigo=info["Codigo"]
            cuidadocorporal.Nombre=info["Nombre"]
            cuidadocorporal.Sexo=info["Sexo"]
            cuidadocorporal.Precio=info["Precio"]
            cuidadocorporal.save()
            mensaje = "Cuidado Corporal editado"
            cuidadoscorporales = Cuidadocorporal.objects.all()
            formulario_cuidadocorporal = cuidado_Corporal_Formulario()
            return render(request, "AppCoder/cuidadocorporal.html", {"formulario": formulario_cuidadocorporal, "cuidadoscorporales":cuidadoscorporales, "mensaje": mensaje})
    else:
        formulario_cuidadocorporal = cuidado_Corporal_Formulario(initial={"Codigo": cuidadocorporal.Codigo, "Nombre": cuidadocorporal.Nombre, "Sexo": cuidadocorporal.Sexo, "Precio": cuidadocorporal.Precio})
        return render(request, "AppCoder/editarcuidadocorporal.html", {"formulario": formulario_cuidadocorporal, "cuidadoscorporales":cuidadocorporal})  

        
def busquedaPerfume(request):
    return render(request, "AppCoder/busquedaPerfume.html")
    
def buscar(request):
    if request.GET.get("codigo"):
        codigo = request.GET["codigo"]
        perfumes = Perfumeria.objects.filter(Codigo=codigo)        
        if not perfumes:  # Comprobar si perfumes está vacío
            return render(request, "AppCoder/resultadosBusqueda.html", {'mensaje': "No se encontró ningun registro"})
        else:
            return render(request, "AppCoder/resultadosBusqueda.html", {"perfumes": perfumes})
    else:
        return render(request, "AppCoder/busquedaPerfume.html", {"mensaje": "No ingresó ningún dato!"})



def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu = info["username"]
            clave= info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppCoder/inicio.html", {'mensaje': f'Usuario {usu} logueado correctamente'})
            else:
                return render(request, "AppCoder/login.html", {'mensaje': "Datos Invalidos"})
        else:
            return render(request, "AppCoder/login.html", {'formulario': form, 'mensaje': "Datos Invalidos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppCoder/login.html", {'formulario': form})
    
def registrar(request):
    if request.method=='POST':
        form=RegistroUsuario_Formulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()
            return render(request, "AppCoder/inicio.html", {'mensaje': f'Usuario {nombre_usuario} creado correctamente!'})
        else:
            return render(request, "AppCoder/registro.html", {'formulario': form, 'mensaje': "Datos Invalidos"})
    else:
        form=RegistroUsuario_Formulario()
        return render(request, "AppCoder/registro.html", {'formulario': form })
    



@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            
            # Cambiar la contraseña solo si se proporciona una nueva contraseña
            nueva_contraseña = info.get("password1")
            if nueva_contraseña:
                usuario.set_password(nueva_contraseña)
                update_session_auth_hash(request, usuario)  # Actualizar la sesión para evitar cerrar la sesión del usuario
                messages.success(request, f"La contraseña del usuario {usuario.username} ha sido cambiada correctamente.")

            usuario.save()
            messages.success(request, f"El usuario {usuario.username} ha sido editado correctamente.")
            return redirect('inicio')
        else:
            messages.error(request, "Datos Inválidos.")
    else:
        form = UserEditForm(instance=usuario)

    return render(request, "AppCoder/editarPerfil.html", {"formulario": form, "nombreusuario": usuario.username})
