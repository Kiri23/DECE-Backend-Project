from django.contrib import admin
from .models import Curso, Categorias
from profesor.models import Profesor


class CategoriasInline(admin.StackedInline):
    model = Categorias


class ProfesorInline(admin.StackedInline):
    model = Profesor


class CursoAdmin(admin.ModelAdmin):
    inlines = [
        CategoriasInline,
        ProfesorInline,
    ]


admin.site.register(Curso)
admin.site.register(Categorias)
admin.site.register(Profesor)
