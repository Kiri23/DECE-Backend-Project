from django.db import models
from django.db.models import Q

'''
Esta clase va a tener los querys relacionados solamente con cursos
'''


class CursoQuerySet(models.QuerySet):
    def porCategorias(self, categorias):
        return self.filter(categoria__nombre__in=categorias)

    def porTitulo(self, titulo):
        print(f'queryset por titulo: {titulo}')
        # Utilizar el | para utilizar el or
        return self.filter(Q(titulo__icontains=titulo))


'''
Esta clase va a tener los querys relacionados solamente con categorias
'''


class CategoriasQuerySet(models.QuerySet):
    def masPopulares(self):
        return self.all().order_by('popularidad')[:5]
