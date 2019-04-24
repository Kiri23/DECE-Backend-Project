from django.shortcuts import render
import logging
import json
from django.views import View
from curso.views import CursoListView, CategoriaListView
from django.http import JsonResponse
from websiteContenido.models import contenidoDelWebsite


class inicio(View):
    """
    Aqui es donde esta la logica para la pagina de inicio. 
    """

    def get(self, request, *args, **kwargs):
        """
        Cuando se hace un ``Get`` request a la pagina de inicio

        Attributes
        ----------
        tipo_categoria
           Esta variable la utilizo para filtar los cursos por categoria
        listaDeCurso
            Delega la acción a la applicación ``curso``. Especificamente el metodo  :py:func:`~curso.views.CursoListView.get_queryset` para cargar toda la lista de curso
        mas_populares
            Delega la acción a la applicación ``curso``. Especificamente el metodo  :py:func:`~curso.views.CursoListView.get_queryset` para que busque las categorias mas populares
        categorias
            Delega la acción a la applicación ``curso``. Especificamente el metodo  :py:func:`~curso.views.CursoListView.get_queryset` para que busque todas las categorias de la base de datos.  
        textoHeader
            El texto del *header* que se obtiene automaticamente de la base de datos. El texto es dinamico y la organización puede cambiar el contenido.           
        """
        logger = logging.getLogger(__name__)
        # Aunque le este enviando el context al index.html. El context puede viajar anidamente los template. index.html -> base.html -> navbar.hmtl
        context = {"indexNavActiveClass": "active"}
        # When the page first load I want to show all courses then all course filtering is done through the ajax call.
        print('here we go')
        tipo_categoria = _dictCategoria('Todos')
        listaDeCurso = cargarListaDeCurso(tipo_categoria)
        masPopulares, categorias = cargarListaDeCategorias()
        textoHeader = cargarContenidoDelHeader()
        # This call internally __contains__ methods
        if "search" in request.GET:
            listaDeCurso = buscarCursosPorTitulos(request)
        self.debug(logger, listaDeCurso, categorias, request)
        return render(request, 'inicio/inicio.html', {"context": context, "cursos": listaDeCurso, "categorias": {"masPopulares": masPopulares, "todas": categorias}, "heading": textoHeader})

    def debug(self, logger, listaDeCurso, categorias, request):
        logger.debug(
            (listaDeCurso, 'context de inicio para la lista de curso'))
        logger.debug(
            (categorias, 'context de inicio para categorias de curso'))
        if listaDeCurso:
            lista = [curso for curso in listaDeCurso]
        # print(f'lista de curso en context: {lista}')


def cargarListaDeCurso(tipo):
    listaDeCurso = CursoListView.get_queryset(
        CursoListView, tipo).values()
    return listaDeCurso


def cargarListaDeCategorias():
    masPopulares, categorias = CategoriaListView.get_queryset(
        CategoriaListView)
    return masPopulares, categorias

# El _ significa que es un metodo privado
def _dictCategoria(categoria):
    data = {'tipo': 'Categoria', 'Categoria': categoria}
    return data


def cargarContenidoDelHeader():
    contenido = contenidoDelWebsite.contenido.pagina('Inicio')
    return contenido
    print(f'contenido: {contenido}')


def buscarCursosPorTitulos(request):
    titulo = request.GET['search']
    if titulo:
        print(f'query: {titulo}')
        tipo_busqueda = {'tipo': 'Busqueda', 'Titulo': titulo}
        return cargarListaDeCurso(tipo_busqueda)


def obtenerCategoriaFromAjax(request):
    """
    Este metodo se llama cuando un estudiante cambio el estado de un Checkbox para mostrar los diferentes cursos filtrado por la categoria selecionada
    """
    # if request.is_ajax():
    if request.method == 'GET':
        if 'categoria[]' in request.GET:
            # El usuario marco uno/s checkbox. Filtrar por esa categoria/s
            # TODO Si lo pongo con el metodo no funciona. No se Porque
            categoria = request.GET.getlist('categoria[]')
            tipo_categoria = _dictCategoria(categoria)
            queryDeCurso = cargarListaDeCurso(tipo_categoria)
            listaDeCurso = [curso for curso in queryDeCurso]
            data = {
                'cursos': listaDeCurso
            }
            return JsonResponse(data)
        elif 'categoria' in request.GET:
            # volver a mostrar todos los cursos cuando el usuario deseleciono todos los checkbox
            curso = muestraTodosLosCursos('categoria', request)
            return JsonResponse(curso)


def muestraTodosLosCursos(queryParam, request):
    """
    Hace lo que el nombre de la funcion dice. El proposito de este metodo es mostrar todos los cursos cuando un usuario deseleciono todos las categorias 
    """
    categoria = request.GET[queryParam]
    #: Pon la categoria como "Todos" para que muestre todos los curso 
    tipo_categoria = _dictCategoria(categoria)
    queryDeCurso = cargarListaDeCurso(tipo_categoria)
    listaDeCurso = [curso for curso in queryDeCurso]
    data = {
        'cursos': listaDeCurso
    }
    return data
