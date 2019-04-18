from django.db import models
from django.urls import reverse
from profesor.models import Profesor


from .validators import validacion_dias_de_la_semana
from django.core.validators import MaxValueValidator, MinValueValidator
from .queryset import CursoQuerySet, CategoriasQuerySet


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
        'profesor.Profesor', on_delete=models.CASCADE, help_text="El profesor del curso")
    categoria = models.ForeignKey(
        'Categorias', on_delete=models.CASCADE, help_text="La categoria que pertenece este curso.")
    imagen = models.ImageField(
        upload_to='curso/imagen/', blank=True)
    video = models.FileField(
        upload_to='curso/video/', blank=True)

    # Specific properties to the model
    objects = CursoQuerySet.as_manager()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("curso:curso", kwargs={"pk": self.pk})


class Categorias(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    popularidad = models.PositiveSmallIntegerField(
        default=20000, validators=[MinValueValidator(1)], help_text="Elija un numero para ordenar los cursos mediante la popularidad.")

    # Specific properties to the model
    objects = CategoriasQuerySet.as_manager()

    def __str__(self):
        return self.nombre

    class Meta:
        # for admin listView
        ordering = ['popularidad']


# TODO:
#   1) Hacer funcion para obtener el nombre en el modelo no en el queryset
