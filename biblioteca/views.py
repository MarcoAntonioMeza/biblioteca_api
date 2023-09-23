from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from . serializers import *
from .models import *

from usuario.models import Usuario

# Create your views here.
class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    """
    Para comprobar si esta autenticado se utiliza
    permission_classes = [permissions.IsAuthenticated]
    """
    #permission_classes = [permissions.AllowAny]
    serializer_class = EditorialSerializer
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


class LibroViewSet(viewsets.ModelViewSet): 
    queryset = Libro.objects.all()

    serializer_class = LibroSerializer 
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def buscar(self,request):
        # Obtén el término de búsqueda desde la solicitud
        termino_busqueda = request.query_params.get('q', '')
        # Obtener  el término de búsqueda desde la solicitud
        libros = Libro.objects.filter(titulo__icontains= termino_busqueda)

        #Serializa los resultados y devuelve la respuesta
        serialize = LibroSerializer(libros,many=True)
        return Response(serialize.data)

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    #permission_classes = [permissions.AllowAny]
    def search_by_user(self,request,id):
        try:
            user = Usuario.objects.get(pk=id)
            prestamos = Prestamo.objects.filter(user=user)
            serialize = PrestamoSerializer(prestamos,many=True)
            return Response(serialize.data)
        except Usuario.DoesNotExist:
            return Response(
                {'message': 'El usuario con el ID especificado no existe.'},
             status=status.HTTP_404_NOT_FOUND)
        
    def mis_prestamos(self,request):
        try:
            user = self.request.user
            prestamos = Prestamo.objects.filter(user=user)
            serialize = PrestamoSerializer(prestamos,many=True)
            return Response(serialize.data)
        except Exception as e:
            return Response(
                {'message': f' {e}'},
             status=status.HTTP_404_NOT_FOUND)

    

