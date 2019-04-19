from django.contrib import admin
from .models import Curso, Categorias, Seccion, Temas, Subtemas, DiasDeLaSemana
from profesor.models import Profesor


class SeccionInline(admin.StackedInline):
    model = Seccion
    extra = 1
    show_change_link = True
    insert_after = 'tieneSeccion'
    classes = ("collapse",)


class TemasInline(admin.StackedInline):
    model = Temas
    extra = 2
    show_change_link = True
    search_fields = ('nombre',)
    classes = ("collapse",)


class SubtemaInline(admin.StackedInline):
    model = Subtemas
    extra = 2
    show_change_link = True
    search_fields = ('nombre',)
    classes = ("collapse",)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'profesor', 'categoria',)
    list_display_links = ('titulo', 'profesor', 'categoria')
    list_filter = ('profesor', 'categoria')
    search_fields = ('titulo', 'descripcion',
                     'profesor__nombre', 'categoria__nombre', 'temas__nombre', 'subtemas__nombre')
    autocomplete_fields = ['profesor', 'categoria']
    # For manyToMany fields
    filter_horizontal = ('dias',)
    fieldsets = (
        ('Información general ', {
            'fields': ('titulo', 'descripcion', 'dias', 'costo', 'cupos', 'duracion', 'tieneSeccion', 'profesor', 'categoria', 'imagen', 'video'),
        }), ('Prontuario', {'fields': ()}),
    )

    inlines = [
        TemasInline,
        SeccionInline,
        SubtemaInline
    ]

    # For rendering[modifying/hacking] the section inline after field tiene seccion
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


class TemasAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)


class SubtemasAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'tema')
    autocomplete_fields = ['tema']


admin.site.register(Curso, CursoAdmin)
admin.site.register(Temas, TemasAdmin)
admin.site.register(Subtemas, SubtemasAdmin)
admin.site.register(Seccion)
admin.site.register(Categorias, CategoriaAdmin)
admin.site.register(Profesor, ProfesorAdmin)
# admin.site.register(DiasDeLaSemana)
