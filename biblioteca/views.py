from django.shortcuts import render

# Create your views here.

from .models import *
from rest_framework import viewsets, permissions
from . serializers import *

class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    """
    Para comprobar si esta autenticado se utiliza
    permission_classes = [permissions.IsAuthenticated]
    """
    #permission_classes = [permissions.AllowAny]
    serializer_class = EditorialSerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [permissions.AllowAny]


class LibroViewSet(viewsets.ModelViewSet): 
    queryset = Libro.objects.all()

    serializer_class = LibroSerializer 
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [permissions.AllowAny]

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [permissions.AllowAny]

