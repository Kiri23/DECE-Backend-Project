from django.contrib import admin
from .models import Curso, Categorias, Temas, Subtemas
from profesor.models import Profesor


class TemasInline(admin.StackedInline):
    model = Temas


class CursoAdmin(admin.ModelAdmin):
    inlines = [
        TemasInline,
    ]

    class Meta:
        model = Curso


admin.site.register(Curso, CursoAdmin)
admin.site.register(Temas)
admin.site.register(Subtemas)
admin.site.register(Categorias)
admin.site.register(Profesor)
