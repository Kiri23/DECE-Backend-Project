from django.shortcuts import render
from django.views import generic
from .models import Curso, Categorias


class CursoListView(generic.ListView):
    context_object_name = 'cursos'

    def get_queryset(self, tipo):
        print(f'cursoListView: {tipo}')
        return self._getCursos(self, tipo)

    def _getCursos(self, tipo):
        try:
            # In python does not exist a switch statement. This is my way of a switch
            if tipo['tipo'] == 'Categoria':
                return self._getCursoByCategories(tipo)
            elif tipo['tipo'] == 'Busqueda':
                return self.searchCourseByTittle(tipo)
            else:
                # Fallabck if none of the above works or are undefined
                return Curso.objects.all()
        except:
            # TODO: Send sentry error. Use Loggin Module
            print('Ocurrio un error en el queryset del ListViewCurso')
            return Curso.objects.all()

    def _getCursoByCategories(tipo):
        if tipo['Categoria']:
            categoria = tipo['Categoria']
            if categoria == 'Todos':
                print('mostrando todos los curso')
                return Curso.objects.all()
            else:
                return Curso.objects.porCategorias(categoria)
        else:
            # TODO: Send Sentry error no se especifico categoria
            print('error: el dictionario no contiene categoria como key')

    def searchCourseByTittle(tipo):
        print(f'bsuqueda de curso:')
        if tipo['Titulo']:
            titulo = tipo['Titulo']
            return Curso.objects.porTitulo(titulo)
        else:
            # TODO: Send Sentry error no se especifico titulo en el dictionario
            print('error: el dictionario no contiene titulo como key')


class CategoriaListView(generic.ListView):
    context_object_name = 'categorias'

    def get_queryset(self):
        mas_populares = Categorias.objects.masPopulares()
        categorias = Categorias.objects.all().values()
        return mas_populares, categorias


class CursoDetailView(generic.DetailView):
    model = Curso
    context_object_name = 'curso'


def curso(request, pk):
    return render(request, "curso/curso_detail.html")
