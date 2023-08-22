from django.urls import path
from .views import *

urlpatterns = [
   
   
    path('perfumeria/', perfumeria, name = 'perfumeria' ),
    path('cuidadocorporal/', cuidadoCorporal, name = 'cuidadocorporal'),
    path('maquillaje/', maquillaje, name = 'maquillaje'),
    path('cabello/', cabello, name = 'cabello'), 
    path('clientes/', clientes, name = 'clientes'), 
]


