from django.urls import path
from .views import *

urlpatterns = [
   
   
    path('perfumeria/', perfumeria, name = 'perfumeria' ),
    path('cuidadocorporal/', cuidadoCorporal, name = 'cuidadocorporal'),
    path('maquillaje/', maquillaje, name = 'maquillaje'),
    path('cabello/', cabello, name = 'cabello'), 
    path('clientes/', clientes, name = 'clientes'), 
    path('busquedaPerfume/', busquedaPerfume, name = 'busquedaPerfume'),
    path('buscar/', buscar, name = 'buscar'),
    path('eliminarperfume/<id>', eliminarperfume, name = 'eliminarperfume'),
    path('eliminarmaquillaje/<id>', eliminarmaquillaje, name = 'eliminarmaquillaje'),
    path('eliminarcuidadocorporal/<id>', eliminarcuidadocorporal, name = 'eliminarcuidadocorporal'),
    path('eliminarcabello/<id>', eliminarcabello, name = 'eliminarcabello'),
    path('eliminarcliente/<id>', eliminarcliente, name = 'eliminarcliente'),
    path('editarcabello/<id>', editarcabello, name = 'editarcabello'),
    path('editarperfume/<id>', editarperfume, name = 'editarperfume'),
    path('editarmaquillaje/<id>', editarmaquillaje, name = 'editarmaquillaje'),
    path('editarcliente/<id>', editarcliente, name = 'editarcliente'),
    path('busquedaPerfume', busquedaPerfume, name = 'busquedaPerfume'),

]


