from django.db import models
from django.urls import reverse
from .validators import validacion_dias_de_la_semana


class Curso(models.Model):
    titulo = models.CharField(max_length=900)
    descripcion = models.TextField(verbose_name="descripción")
    dias = models.CharField(verbose_name='Días', max_length=50,
                            validators=[validacion_dias_de_la_semana], default='')
    costo = models.DecimalField(max_digits=6, decimal_places=2)
    cupos = models.PositiveSmallIntegerField(
        help_text="Los cupos disponibles para el curso")
    duracion = models.PositiveSmallIntegerField(
        verbose_name="duración", help_text="La duración del curso en horas")
    tieneSeccion = models.BooleanField(
        default=False, verbose_name="tiene sección", help_text='Marque el encasillado si este curso tiene una sección')
    seccion = models.SlugField(
        max_length=50, help_text="La sección del curso si este lleva una sección.", blank=True)
    profesor = models.ForeignKey(
        'Profesor', on_delete=models.CASCADE, help_text="El profesor del curso")
    categoria = models.ForeignKey(
        'Categorias', on_delete=models.CASCADE, help_text="La categoria que pertenece este curso.")

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("curso:curso", kwargs={"pk": self.pk})


class Profesor(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellidos')

    def __str__(self):
        return self.nombre


class Categorias(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')

    def __str__(self):
        return self.nombre


# TODO:
#   1) Hacer funcion para obtener el nombre
