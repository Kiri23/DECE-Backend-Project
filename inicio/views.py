from django.shortcuts import render
import logging
from django.views import View
from curso.views import CursoListView, CategoriaListView


class inicio(View):
    def get(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)
        # Aunque le este enviando el context al index.html. El context puede viajar anidamente los template. index.html -> base.html -> navbar.hmtl
        context = {"indexNavActiveClass": "active"}
        listaDeCurso = CursoListView.get_queryset(CursoListView).values()
        categorias = CategoriaListView.get_queryset(CategoriaListView).values()
        self.debug(logger, listaDeCurso, categorias)
        return render(request, 'inicio/inicio.html', {"context": context, "cursos": listaDeCurso, "categorias": categorias})

    def debug(self, logger, listaDeCurso, categorias):
        logger.debug(
            (listaDeCurso, 'context de inicio para la lista de curso'))
        logger.debug(
            (categorias, 'context de inicio para categorias de curso'))
