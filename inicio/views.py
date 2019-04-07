from django.shortcuts import render
import logging
import json
from django.views import View
from curso.views import CursoListView, CategoriaListView
from django.http import JsonResponse
from curso.models import Curso


class inicio(View):
    def get(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)
        # Aunque le este enviando el context al index.html. El context puede viajar anidamente los template. index.html -> base.html -> navbar.hmtl
        context = {"indexNavActiveClass": "active"}
        categoria = 'Todos'
        print(f'categoria es: {categoria}')
        listaDeCurso = CursoListView.get_queryset(CursoListView, categoria).values()
        categorias = CategoriaListView.get_queryset(CategoriaListView).values()
        self.debug(logger, listaDeCurso, categorias, request)
        return render(request, 'inicio/inicio.html', {"context": context, "cursos": listaDeCurso, "categorias": categorias})

    def debug(self, logger, listaDeCurso, categorias, request):
        logger.debug(
            (listaDeCurso, 'context de inicio para la lista de curso'))
        logger.debug(
            (categorias, 'context de inicio para categorias de curso'))
        lista = [curso for curso in listaDeCurso]
        # print(f'lista de curso en context: {lista}')

    # def categoriaFromUrl(self,request, CursoListView):
    #     categoria='Todos'
    #     print(f'request is ajax?:{request.is_ajax()}')
    #     # if request.is_ajax():
    #     if request.method == 'GET':
    #         if 'categoria' in request.GET:
    #             categoria = request.GET['categoria']
    #             return categoria
    #     return categoria


def obtenerCategoriaFromAjax(request):
    print('hello')
    # if request.is_ajax():
    if request.method == 'GET':
        print('hello 1')
        if 'categoria[]' in request.GET:
            print('hello 2')
            categoria = request.GET.getlist('categoria[]')
            print('categoria from inicio view', categoria )
            queryDeCurso = CursoListView.get_queryset(CursoListView, categoria).values()
            listaDeCurso = [curso for curso in queryDeCurso]
            # print(f'lista de curso ajax{listaDeCurso}')
            data = {
                'cursos': listaDeCurso
            }
            return JsonResponse(data)
        elif 'categoria' in request.GET:
            print('sola una categoria')
            categoria = request.GET['categoria']
            queryDeCurso = CursoListView.get_queryset(CursoListView, categoria).values()
            listaDeCurso = [curso for curso in queryDeCurso]
            # print(f'lista de curso ajax{listaDeCurso}')
            data = {
                'cursos': listaDeCurso
            }
            return JsonResponse(data)


