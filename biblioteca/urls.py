from rest_framework import routers
from django.urls import path
from . views import *


rutas = routers.DefaultRouter()

rutas.register(r'editorial',EditorialViewSet,'editorial')
rutas.register(r'libro',LibroViewSet,'libro')
rutas.register(r'prestamo',PrestamoViewSet,'prestamo')

urlpatterns = [
    path('libro/buscar/',LibroViewSet.as_view({'get':'buscar'}), name='buscar-libro'),
    
    path('prestamo/por-usuario/<int:id>/', PrestamoViewSet.as_view({'get':'search_by_user'}), name='prestamos-por-usuario'),
]

urlpatterns += rutas.urls