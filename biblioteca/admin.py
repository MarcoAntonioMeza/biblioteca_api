from django.contrib import admin
from .models import *

# Register your models here.
tupla = Libro , Editorial, Prestamo
admin.site.register(tupla)