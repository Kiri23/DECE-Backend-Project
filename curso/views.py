from django.shortcuts import render
from django.views import generic, View
from .models import Curso, Categorias


class CursoListView(generic.ListView):
    def get_queryset(self, categoria):
        if categoria =="Todos":
            print('Todos los cursos en listview')
            return Curso.objects.all()
        else:
            print('categoria from inicio in the curso app ', categoria)
            print(Curso.objects.filter(categoria__nombre__iexact=categoria))

            return Curso.objects.filter(categoria__nombre__iexact=categoria)
        # return Curso.objects.all()

class CategoriaListView(generic.ListView):
    def get_queryset(self):
        return Categorias.objects.all().order_by('popularidad')[:5]


def curso(request, pk):
    return render(request, "curso/curso_detail.html")
