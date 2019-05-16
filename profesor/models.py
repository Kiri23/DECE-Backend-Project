from django.db import models
from django.urls import reverse


class Profesor(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellidos')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("profesor:profesor", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Profesores"

# TODO:
#   1) Hacer funcion para obtener el nombre en el modelo no en el queryset
