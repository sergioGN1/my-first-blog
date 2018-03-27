from django.db import models

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=250)
    dni = models.CharField(max_length=9)
    telefono = models.IntegerField()
    cargo = models.CharField(max_length=250)

    def __str__(self):
        trabajador = self.nombre + " " + self.apellido
        return trabajador
# Create your models here.
