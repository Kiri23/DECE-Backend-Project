from django.contrib import admin
from .models import Curso, Categorias, Seccion, Temas, Subtemas, DiasDeLaSemana
from profesor.models import Profesor


class SeccionInline(admin.StackedInline):
    model = Seccion
    extra = 1
    insert_after = 'tieneSeccion'


class TemasInline(admin.StackedInline):
    model = Temas
    search_fields = ('nombre',)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'profesor', 'categoria',)
    list_display_links = ('titulo', 'profesor', 'categoria')
    list_filter = ('profesor', 'categoria')
    search_fields = ('titulo', 'descripcion',
                     'profesor__nombre', 'categoria__nombre', 'temas__nombre')
    autocomplete_fields = ['profesor', 'categoria']
    # For manyToMany fields
    filter_horizontal = ('dias',)
    fieldsets = (
        ('Información general ', {
            'fields': ('titulo', 'descripcion', 'dias', 'costo', 'cupos', 'duracion', 'tieneSeccion', 'profesor', 'categoria', 'imagen', 'video'),
        }),
    )

    inlines = [
        TemasInline,
        SeccionInline
    ]

    change_form_template = 'admin/custom/change_form.html'

    class Meta:
        model = Curso

    class Media:
        css = {
            'all': (
                'css/admin.css',
            )
        }


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
# admin.site.register(DiasDeLaSemana)
