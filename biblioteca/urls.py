from rest_framework import routers
from . views import *


rutas = routers.DefaultRouter()

rutas.register(r'editorial',EditorialViewSet,'editorial')
rutas.register(r'libro',LibroViewSet,'libro')
rutas.register(r'prestamo',PrestamoViewSet,'prestamo')

urlpatterns = rutas.urls