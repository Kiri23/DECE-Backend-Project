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
        # When the page first load I want to show all courses then all course filtering is done through the ajax call. 
        categorias = "Todos"
        listaDeCurso = cargarListaDeCurso(categorias)
        categorias = cargarListaDeCategorias()
        self.debug(logger, listaDeCurso, categorias, request)
        return render(request, 'inicio/inicio.html', {"context": context, "cursos": listaDeCurso, "categorias": categorias})

    def debug(self, logger, listaDeCurso, categorias, request):
        logger.debug(
            (listaDeCurso, 'context de inicio para la lista de curso'))
        logger.debug(
            (categorias, 'context de inicio para categorias de curso'))
        lista = [curso for curso in listaDeCurso]
        # print(f'lista de curso en context: {lista}')

def cargarListaDeCurso(categoria):
    listaDeCurso = CursoListView.get_queryset(CursoListView, categoria).values()
    return listaDeCurso

def cargarListaDeCategorias():
    categorias = CategoriaListView.get_queryset(CategoriaListView).values()
    print(f'las primeras cinco categorias: {categorias} ')
    return categorias

'''
    Este metodo se llama cuando un estudiante cambio el estado de un Checkbox para mostrar los diferentes cursos
'''
def obtenerCategoriaFromAjax(request):
    # if request.is_ajax():
    if request.method == 'GET':
        if 'categoria[]' in request.GET:
            # El usuario marco uno/s checkbox. Filtrar por esa categoria/s
            #TODO Si lo pongo con el metodo no funciona. No se Porque 
            categoria = request.GET.getlist('categoria[]')
            queryDeCurso = cargarListaDeCurso(categoria)
            listaDeCurso = [curso for curso in queryDeCurso]
            data = {
                'cursos': listaDeCurso
            }
            return JsonResponse(data)
        elif 'categoria' in request.GET:
            # volver a mostrar todos los cursos cuando el usuario deseleciono todos los checkbox
            curso = cursoFromUrl('categoria', request)
            return JsonResponse(curso)

def cursoFromUrl(queryParam, request):
    categoria = request.GET[queryParam]
    queryDeCurso = cargarListaDeCurso(categoria)
    listaDeCurso = [curso for curso in queryDeCurso]
    data = {
        'cursos': listaDeCurso
    }
    return data
