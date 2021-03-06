from django.db import models
from .queryset import InscribeteQueryset


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
    estudiante = models.ForeignKey(
        'usuario.CustomUser', on_delete=models.CASCADE, help_text="El estudiante que se esta registrando", default=None)
    # Curso
    curso = models.ForeignKey(
        'curso.Curso', on_delete=models.CASCADE, help_text="El curso que el estudiante se esta registrando", default=None)

    #: Specific properties to the model
    inscripciones = InscribeteQueryset.as_manager()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Inscripciones"
