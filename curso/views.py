from django.shortcuts import render
from django.views import generic, View
from .models import Curso, Categorias


class CursoListView(generic.ListView):
    context_object_name = 'cursos'

    def get_queryset(self, categoria):
        if categoria == "Todos":
            return Curso.objects.all()
        else:
            return Curso.objects.porCategorias(categoria)


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
