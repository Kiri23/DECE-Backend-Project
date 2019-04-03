from django.db import models


class Curso(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(verbose_name="descripción")
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
    categoria = models.ForeignKey('Categorias', on_delete=models.CASCADE, help_text="La categoria que pertenece este curso." )


class Profesor(models.Model):
    pass


class Categorias(models.Model):
    pass


# TODO:
#   1) Hacer funcion para obtener el nombre
