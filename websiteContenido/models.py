from django.db import models
from .queryset import WebsiteContenidoQuerySet


class contenidoDelWebsite(models.Model):
    texto = models.CharField(max_length=900, verbose_name='Contenido')
    pagina = models.CharField(max_length=30)

    # Specific properties to the model
    contenido = WebsiteContenidoQuerySet.as_manager()

    def __str__(self):
        return self.pagina

    class Meta:
        verbose_name_plural = "Encabezado"
