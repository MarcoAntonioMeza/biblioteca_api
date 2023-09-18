from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        
        fields = ('__all__')
        

class LibroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Libro

        fields = ('__all__')



    #Forma uno de serializar los modelos relacionados
    editorial = serializers.PrimaryKeyRelatedField(queryset=Editorial.objects.all())
    """
    Salida
    {
        "id": 1,
        "editorial": 3,
        "titulo": "DEV",
        "autor": "Juanito",
        "anio_publicacion": 2010,
        "genero": "Código",
        "precio": "380.00",
        "image": "http://127.0.0.1:8000/resources/libro/WhatsApp_Image_2023-08-20_at_6.41.15_PM.jpeg"
    }

    """

    #Froma dos de serializar los modelos relacionados
    #editorial = EditorialSerializer()
    """
    Salida
    {
        "id": 1,
        "editorial": {
            "id": 3,
            "nombre": "Ejemplo",
            "direccion": "123 Calle Principal",
            "telefono": "555555555",
            "correo": "ejemplo@example.com"
        },
        "titulo": "DEV",
        "autor": "Juanito",
        "anio_publicacion": 2010,
        "genero": "Código",
        "precio": "380.00",
        "image": "http://127.0.0.1:8000/resources/libro/WhatsApp_Image_2023-08-20_at_6.41.15_PM.jpeg"
    }
    """


    #Forma tres de serializar modelos relacionados 

    #editorial = serializers.StringRelatedField()

    """
    def to_representation(self,instance):
        return{
            'id': instance.id,
            'nombre': instance.titulo,
            'anio_publicacion': instance.anio_publicacion,
            'genero': instance.genero,
            'precio': instance.precio,
            #'image': instance.image,
            'editorial': {
                'id' :instance.editorial.id,
            },
        }
    """

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ('__all__')

    #users  = User.objects.all()
    #libro = serializers.PrimaryKeyRelatedField(queryset = Libro.objects.all())
    #user = serializers.UserSerializer(users, many=True)

    editorial = serializers.StringRelatedField()

    def to_representation(self,instance):
        return{
            'id': instance.id,
            'fecha_prestamo': instance.fecha_prestamo,
            'fecha_entrega': instance.fecha_entrega,
            'user':{
                'id':instance.user.id,
                'user':instance.user.full_name
            },
            'libro':{
                'id':instance.libro.id,
                'titulo': instance.libro.titulo
            }
        }
    
