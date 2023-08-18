from django.db import models

# Create your models here.

class Perfumeria(models.Model):
    Codigo = models.IntegerField()
    Nombre = models.CharField(max_length=50)
    Sexo = models.CharField(max_length=50)
    Precio = models.IntegerField()
    
class Ciudadocorporal(models.Model):
    Codigo = models.IntegerField()
    Nombre = models.CharField(max_length=50)
    Sexo = models.CharField(max_length=50)
    
class Maquillaje(models.Model):
    Codigo = models.IntegerField()
    Nombre = models.CharField(max_length=50)
    Precio = models.IntegerField()
    
class Cabello(models.Model):
    Codigo = models.IntegerField()
    Nombre = models.CharField(max_length=50)
    Sexo = models.CharField(max_length=50)
    
class Clientes(models.Model):
    Apellido = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)
    DNI = models.CharField(max_length=50)
    Email = models.EmailField()
    
    
    
