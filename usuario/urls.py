from rest_framework import routers
from django.urls import path
from . views import *


rutas = routers.DefaultRouter()

rutas.register(r'user',UsaurioViewSet,'usuario')


urlpatterns = [
    #path('libro/buscar/',LibroViewSet.as_view({'get':'buscar'}), name='buscar-libro'),
]

urlpatterns += rutas.urls