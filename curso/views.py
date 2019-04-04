from django.shortcuts import render
from django.views import generic, View
from .models import Curso


class CursoListView(generic.ListView):
    # template_name =
    # queryset = Curso.objects.all()

    def get_queryset(self):
        return Curso.objects.all()


def curso(request, pk):
    return render(request, "curso/curso_detail.html")
