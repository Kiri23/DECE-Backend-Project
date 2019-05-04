from django.db import models


class Registracion(models.Model):
    nombre = models.CharField(max_length=900)
    apellido = models.CharField(max_length=900)
    correo_electronico = models.EmailField()
    # generos
    fecha_de_nacimiento = models.DateTimeField()
    lugar_de_nacimiento = models.CharField(max_length=900)
    numero_de_telefono = models.IntegerField()
    # preparacion academica
    preparacion_academica = models.CharField(max_length=900)
    direccion = models.CharField(max_length=900)
    pueblo = models.CharField(max_length=900)
    pais = models.CharField(max_length=900)
    zip_code = models.IntegerField()
    ocupacion = models.CharField(max_length=900)
    telefono_del_trabajo = models.IntegerField()
    lugar_del_trabajo = models.CharField(max_length=900)
    # Usuario 
    # Curso

    def __str__(self):
        return self.nombre
