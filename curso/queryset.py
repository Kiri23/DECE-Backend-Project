from django.db import models

'''
Esta clase va a tener los querys relacionados solamente con cursos
'''
class CursoQuerySet(models.QuerySet):
    def porCategorias(self,categorias):
        return self.filter(categoria__nombre__in=categorias)

'''
Esta clase va a tener los querys relacionados solamente con categorias
'''
class CategoriasQuerySet(models.QuerySet):
    def masPopulares(self):
        return self.all().order_by('popularidad')[:5]