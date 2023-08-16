from django.db import models

# Create your models here.

class Curso(models.Model):
    Nombre = models.CharField(max_length=50)
    Comision = models.IntegerField()
    
class Estudiante(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Email = models.EmailField()
    
class Profesor(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Email = models.EmailField()
    Profesion = models.CharField(max_length=50)
    
class Entregable(models.Model):
    Nombre = models.CharField(max_length=50)
    Fecha_Entrega = models.DateField()
    Entregado = models.BooleanField()
    
    
    
