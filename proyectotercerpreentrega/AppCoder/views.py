from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def crear_curso(request):
    
    nombre_curso = "Programacion Basica"
    comision_curso = 99998888
    print('Creando Curso')
    curso = Curso(Nombre=nombre_curso, Comision=comision_curso)
    curso.save()
    respuesta = f'Curso creado: {curso.Nombre} - {curso.Comision}'
    return HttpResponse(respuesta)

def listar_cursos(request):
    cursos = Curso.objects.all()
    respuesta = ''
    for curso in cursos:
        respuesta +=f'{curso.Nombre} - {curso.Comision}<br> ' 
    return HttpResponse(respuesta)

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'AppCoder/cursos.html', {'cursos': cursos})

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

