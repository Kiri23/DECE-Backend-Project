from django.shortcuts import render
import logging
from django.views import View
from curso.views import CursoListView


class inicio(View):
    def get(self, request, *args, **kwargs):
        # Aunque le este enviando el context al index.html. El context puede viajar anidamente los template. index.html -> base.html -> navbar.hmtl
        context = {"indexNavActiveClass": "active"}
        listaDeCurso = CursoListView.get_queryset(CursoListView).values()
        print(listaDeCurso, 'context de inicio')
        return render(request, 'inicio/inicio.html', {"context": context, "query": listaDeCurso})
