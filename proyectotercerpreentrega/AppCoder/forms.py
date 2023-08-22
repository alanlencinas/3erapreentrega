from django import forms

class perfumeria_Formulario(forms.Form):
    Codigo = forms.IntegerField()
    Nombre = forms.CharField(max_length=50)
    Sexo = forms.CharField(max_length=50)
    Precio = forms.DecimalField(max_digits=10, decimal_places=2)
    
class cuidado_Corporal_Formulario(forms.Form):
    Codigo = forms.IntegerField()
    Nombre = forms.CharField(max_length=50)
    Sexo = forms.CharField(max_length=50)
    Precio = forms.DecimalField(max_digits=10, decimal_places=2)
    
class maquillaje_Formulario(forms.Form):
    Codigo = forms.IntegerField()
    Nombre = forms.CharField(max_length=50)
    Precio = forms.DecimalField(max_digits=10, decimal_places=2)
    
class cabello_Formulario(forms.Form):
    Codigo = forms.IntegerField()
    Nombre = forms.CharField(max_length=50)
    Sexo = forms.CharField(max_length=50)
    Precio = forms.DecimalField(max_digits=10, decimal_places=2)
    
class clientes_Formulario(forms.Form):
    Apellido = forms.CharField(max_length=50)
    Nombre = forms.CharField(max_length=50)
    DNI = forms.CharField(max_length=50)
    Email = forms.EmailField()