from django.shortcuts import render
from django.views import generic
from .models import Curso, Categorias, Temas, Subtemas

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache

# Retrieve the variable i  setting where I defined the time to live(ttl) the cache
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class CursoListView(generic.ListView):
    """
    .. note::
        Antes de ver estas clases deberías saber que los query que se hacen en la base de datos estan en la clase :py:class:`~curso.queryset` de esta aplicación.

        Tambien si deseas saber donde es que se crea el HTML esta en la carpeta de templates del proyecto. En la documentación no se encuentra esta carpeta

    Esta clase utiliza :term:`Class Based Views` de tipo ``ListView``. El proposito de esta clase es listar todos los cursos que se encuentren en la base de datos.
    """
    context_object_name = 'cursos'

    def get_queryset(self, tipo):
        """
        Como dice el nombre del metodo override el :term:`QuerySet` que se hace a la base de dato.
        """
        print(f'cursoListView: {tipo}')
        return self.getCursos(self, tipo)

    def getCursos(self, tipo):
        """
        Esta es la funcion general que hace los query a la base de datos. El metodo original :py:func:`get_queryset` llama a esta funcion. Esta funcion a su vez llama a otra funciones como los otros dos metodos que hay en esta clase :py:func:`getCursoByCategories`, :py:func:`searchCourseByTittle`
        """
        try:
            # In python does not exist a switch statement. This is my way of a switch
            if tipo['tipo'] == 'Categoria':
                return self.getCursoByCategories(tipo)
            elif tipo['tipo'] == 'Busqueda':
                return self.searchCourseByTittle(tipo)
            else:
                # Fallaback if none of the above works or are undefined
                return Curso.objects.all()
        except:
            #: ..todo:: Send sentry error. Use Loggin Module
            print('Ocurrio un error en el queryset del ListViewCurso')
            return Curso.objects.all()

    def getCursoByCategories(tipo):
        if tipo['Categoria']:
            categoria = tipo['Categoria']
            if categoria == 'Todos':
                print('mostrando todos los curso')
                return Curso.objects.all()
            else:
                return Curso.objects.porCategorias(categoria)
        else:
            #: ..todo:: Send Sentry error no se especifico categoria
            print('error: el dictionario no contiene categoria como key')

    def searchCourseByTittle(tipo):
        print(f'bsuqueda de curso:')
        if tipo['Titulo']:
            titulo = tipo['Titulo']
            return Curso.objects.porTitulo(titulo)
        else:
            #: ..todo:: Send Sentry error no se especifico titulo en el dictionario
            print('error: el dictionario no contiene titulo como key')


class CategoriaListView(generic.ListView):
    """
    Esta clase utiliza :term:`Class Based Views` de tipo ``ListView``. El proposito de esta clase es listar todos los categorias que se encuentren en la base de datos.
    """

    context_object_name = 'categorias'

    def get_queryset(self):
        """
        Attributes
        ----------
        mas_populares
           Hace el query a la base de datos para obtener los cursos mas populares
        categorias
            Hace el query a la base de datos para obtener todas las categorias
        """
        #: Hace el query a la base de datos para obtener los cursos mas populares
        mas_populares = Categorias.objects.masPopulares()
        #: Hace el query a la base de datos para obtener todos los cursos
        categorias = Categorias.objects.all().values()
        return mas_populares, categorias


# This cache the entire page the header and the html render content so it load fast
@method_decorator(cache_page(900), name='dispatch')
class CursoDetailView(generic.DetailView):
    """
    Esta clase detalla la información de cada curso por individual.
    """
    model = Curso
    context_object_name = 'curso'

    def get_object(self, queryset=None):
        """
        Este metodo obtiene el object, el modelo que se esta mostrando en esta vista de detalle. La utilizo para guardar el objecto en la memoria cache
        """
        if queryset is None:
            queryset = self.get_queryset()

        curso = super().get_object(queryset)
        cache.set('curso', curso)
        if 'curso' in cache:
            curso = cache.get('curso')
            print(curso.costo)
        return curso

    def obtenerProntuario(self):
        """
        Esta funcion va a tener la logica para crear el prontuario de cada curso.

        Atrributes
        ----------

        """
        # Si quiere coger la instancia del curso es en sel.objects
        curso_id = self.kwargs['pk']
        temas = Temas.objects.porCursoId(curso_id)
        #: Contiene todos los ID de cada tema.
        temas_id = [tema.id for tema in temas]
        subtemas = None
        #: :note: El argumento Tema_id tiene que ser una lista para que el query funcione
        if type(temas_id) is list:
            subtemas = Subtemas.objects.subtemas(temas_id, curso_id)
            return self.createDictionary(temas, subtemas)

        #: TODO: Callback error que pasa si no se puede coger los subtemas
        return {}

    def createDictionary(self, temas: list, subtemas: list):
        """
        En esta función es que creo el dictionario para mostrar el pronturaio. El prontuario consite de temas y cada tema puede tener un subtema.

        Explicación del algoritmo: \n
        Primero verifico si las listas no son vacias. Despues hago un loop anindado por tema y subtema.

        .. note::
            Por cada tema hago un loop por todos los subtemas. Esto significa que si hay cinco temas yo visitos todos los subtemas cinco veces. Esto obviamente es malo para el perfomance. Buscar una mejor opción

        En el loop de subtemas verificio si el id del tema es el mismo del subtema. Si un subtema pertenece a un tema en particular entonce creo el dictionario. Sigo añadiendo subtemas al mismo tema si hay mas de un subtema. Añado una lista vacia si un tema no tiene subtema.

        No hay necesidad de modificar el queryset porque yo accedos los metodos en el template. Siempre y cuando sea un generic view y el metodo no contenga argumentos
        """
        if (Subtemas is not None) and (temas is not None):
            temp = None
            dictionary = {}
            for tema in temas:
                print("---------")
                print(f"para el tema: {tema.nombre}")
                for subtema in subtemas:
                    #: Si un tema tiene subtema
                    if (tema.id == subtema.tema_id):
                        tema_actual = tema.nombre
                        if (tema_actual == temp):
                            dictionary[tema.nombre].append(subtema.nombre)
                        else:
                            dictionary[tema.nombre] = [subtema.nombre]
                    else:
                        print(
                            f"Subtema que no van al mismo tema: {subtema.nombre}")
                    temp = tema_actual

            #: Añadiendo Temas al dictionario que no tiene subtema
            for tema in temas:
                if tema.nombre in dictionary:
                    print(f"Existe {tema.nombre} en el dictionary")
                else:
                    print(
                        f"No existe {tema.nombre} en el dictioanry. Añadiendo ahora el tema")
                    #: Un tema no tiene subtema
                    dictionary[tema.nombre] = []
            return dictionary

    def getRelatedCourses(self):
        """
        Este metodo busca los cursos relacionados para cada detalle de un curso. Este metodo delega el query para la base de datos en la clase :py:class:`~curso.queryset.CursoQuerySet` en el metodo:  :py:meth:`~curso.queryset.CursoQuerySet.relacionados`
        """
        curso_id = self.kwargs['pk']
        return Curso.objects.relacionados(curso_id)
