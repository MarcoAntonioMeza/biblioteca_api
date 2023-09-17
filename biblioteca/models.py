from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Editorial(models.Model):

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=100)

    def  __str__(self):
        return self.nombre


class Libro(models.Model):
    
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField()
    genero = models.CharField(max_length=80)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='resources/libro', null=False, blank=True )

    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.titulo


class Prestamo(models.Model):
    fecha_prestamo = models.DateField()
    fecha_entrega = models.DateField()

    user = models.ForeignKey(User,on_delete = models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}-{self.libro}'



