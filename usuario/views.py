from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from . serializers import UsuarioSerializer
from .models import Usuario


class UsaurioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()

    #permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]