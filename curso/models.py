from django.db import models
from django.urls import reverse
from profesor.models import Profesor


from .validators import validacion_dias_de_la_semana
from django.core.validators import MaxValueValidator, MinValueValidator
from .queryset import CursoQuerySet, CategoriasQuerySet, TemasQuerySet, SubtemasQuerySet


class Curso(models.Model):
    """
    Esta clase representa la tabla curso en la base de datos. Los campos son lo que estan abajos
    """
    titulo = models.CharField(max_length=900)
    descripcion = models.TextField(verbose_name="descripción")
    costo = models.DecimalField(max_digits=6, decimal_places=2)
    cupos = models.PositiveSmallIntegerField(
        help_text="Los cupos disponibles para el curso")
    duracion = models.PositiveSmallIntegerField(
        verbose_name="duración", help_text="La duración del curso en horas")
    tieneSeccion = models.BooleanField(
        default=False, verbose_name="tiene sección", help_text='Marque el encasillado si este curso tiene una sección')
    dias = models.ManyToManyField('DiasDeLaSemana', verbose_name='Días')
    profesor = models.ForeignKey(
        'profesor.Profesor', on_delete=models.CASCADE, help_text="El profesor del curso")
    categoria = models.ForeignKey(
        'Categorias', on_delete=models.CASCADE, help_text="La categoria que pertenece este curso.")
    imagen = models.ImageField(
        upload_to='curso/imagen/', blank=True)
    video = models.FileField(
        upload_to='curso/video/', blank=True)

    #: Specific properties to the model
    objects = CursoQuerySet.as_manager()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        "Coge la url de este curso para poder mostrarlo en pantalla. Se usa para redirecionar al detalle de cada curso en particular"
        return reverse("curso:curso", kwargs={"pk": self.pk})


class Categorias(models.Model):
    """
    Esta clase representa la tabla Categoria en la base de datos.Un curso puede tener muchas categorias pero una categoria pertenece a un solo cursos. Es una relación de muchos a unos. Los campos son lo que estan abajos
    """
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    popularidad = models.PositiveSmallIntegerField(
        default=20000, validators=[MinValueValidator(1)], help_text="Elija un numero para ordenar los cursos mediante la popularidad.")

    #: Specific properties to the model
    objects = CategoriasQuerySet.as_manager()

    def __str__(self):
        return self.nombre

    class Meta:
        # for admin listView
        ordering = ['popularidad']
        verbose_name_plural = "Categorias"


class Seccion(models.Model):
    """
    Esta clase representa la tabla seccion en la base de datos. Un curso puede tener muchas secciones pero una sección pertenece a un solo cursos. Es una relación de muchos a unos. Los campos son lo que estan abajos
    """
    #: El curso que pertenece esta sección
    curso = models.ForeignKey(
        'Curso', on_delete=models.CASCADE, null=True)
    seccion = models.SlugField(
        max_length=50, help_text="La sección del curso si este lleva una sección.", blank=True)

    def __str__(self):
        return self.seccion

    class Meta:
        verbose_name_plural = "Seciones"


class DiasDeLaSemana(models.Model):
    """
    Esta clase representa la tabla Dias de la semana en la base de datos. Esta clase se utiliza para tener una relación de muchos a muchos en la tabla de cursos. Los campos son lo que estan abajos
    """
    dias = models.CharField(verbose_name='Días', max_length=50,
                            validators=[validacion_dias_de_la_semana], default='', unique=True)

    def __str__(self):
        return self.dias


class Temas(models.Model):
    """
    Esta tabla se usa para representar el tema de un prontuario. 
    """
    curso = models.ForeignKey(
        'Curso', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=2000)
    # subtema = models.ForeignKey(
    #     'Subtemas', on_delete=models.CASCADE, null=True)

    #: Specific properties to the model
    objects = TemasQuerySet.as_manager()

    def __str__(self):
        return self.nombre

    # I made this little hack to have nested Inline form on the admin. So I can add temas y subtemas en el curso create view
    # def save(self, *args, **kwargs):
    #     self.subtema.tema = self
    #     super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Temas"


class Subtemas(models.Model):
    """
    Esta tabla se usa para representar el subtema de un tema. Los temas y subtemas se utilizan para hacer el prontuario
    """
    tema = models.ForeignKey(
        'Temas', on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=2000)

    #: Specific properties to the model
    objects = SubtemasQuerySet.as_manager()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Subtemas"


# Codigo
'''
  temas = Temas.objects.filter(curso__pk=11).only('nombre')
#   subtemas = Subtemas.objects.filter(tema__curso__pk=11)
  subtemas = Subtemas.objects.filter(tema__pk=3,tema__curso__pk=11).only('nombre')
  temas_nombre = [tema.nombre for tema in temas]
#   subtemas_tema = [subtema.tema_id for subtema in subtemas]
  subtemas_nombre = [subtema.nombre for subtema in subtemas]
# pero hay mejor forma de hacer esto con dict comprenhesion list
  prontuario = dict(zip(temas_nombre,subtemas_nombre))
#  prontuario = {k: v for k, v in zip(temas_nombre, subtemas_nombre)}
  prontuario['tema1']
#   Pero ahora el problema que estoy teniendo es que tema solamente puede tener un solo subtema         which is wrong. So temas debe de tener muchos subtemas
'''
