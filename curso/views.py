from django.shortcuts import render
from django.views import generic
from .models import Curso, Categorias


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


class CursoDetailView(generic.DetailView):
    """
    Esta clase detalla la información de cada curso por individual.
    """
    model = Curso
    context_object_name = 'curso'

    def obtenerProntuario(self):
        """
        Esta funcion va a tener la logica para crear el prontuario de cada curso
        """
        return "Texto que viene del view"
