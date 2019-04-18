from django.contrib import admin
from .models import Curso, Categorias, Seccion, Temas, Subtemas
from profesor.models import Profesor


class SeccionInline(admin.StackedInline):
    model = Seccion
    fields = ('tieneSeccion', 'seccion')


class TemasInline(admin.StackedInline):
    model = Temas
    search_fields = ('nombre',)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'profesor', 'categoria')
    list_display_links = ('titulo', 'profesor', 'categoria')
    list_filter = ('profesor', 'categoria')
    search_fields = ('titulo', 'descripcion')
    autocomplete_fields = ['profesor', 'categoria']
    fieldsets = (
        ('Información general ', {
            'fields': ('titulo', 'descripcion', 'dias', 'costo', 'cupos', 'duracion', 'profesor', 'categoria', 'imagen', 'video'),
        }),
    )

    inlines = [
        TemasInline,
        SeccionInline
    ]

    class Meta:
        model = Curso


class ProfesorAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'apellido')


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)


class SubtemaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)


admin.site.register(Curso, CursoAdmin)
admin.site.register(Temas)
admin.site.register(Subtemas, SubtemaAdmin)
admin.site.register(Seccion)
admin.site.register(Categorias, CategoriaAdmin)
admin.site.register(Profesor, ProfesorAdmin)
