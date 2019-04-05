from django.shortcuts import render
from django.views import generic, View
from .models import Curso, Categorias


class CursoListView(generic.ListView):
    def get_queryset(self):
        return Curso.objects.all()


class CategoriaListView(generic.ListView):
    def get_queryset(self):
        return Categorias.objects.all().order_by('popularidad')[:5]


def curso(request, pk):
    return render(request, "curso/curso_detail.html")
