from django.shortcuts import render
from django.views import generic, View
from .models import Curso, Categorias


class CursoListView(generic.ListView):
    context = ''
    def get_queryset(self, categoria):
        if categoria =="Todos":
            return Curso.objects.all()
        else:
            return Curso.objects.porCategorias(categoria)

class CategoriaListView(generic.ListView):
    def get_queryset(self):
        return Categorias.objects.masPopulares()


def curso(request, pk):
    return render(request, "curso/curso_detail.html")
