from django.contrib import admin
# I use this for nested inline formset inside temas inlines
from nested_admin import NestedModelAdmin, NestedStackedInline
from .models import Curso, Categorias, Seccion, Temas, Subtemas, DiasDeLaSemana
from profesor.models import Profesor
from django.utils.safestring import mark_safe


class SeccionInline(NestedStackedInline):
    model = Seccion
    extra = 1
    show_change_link = True
    # This work because I change the the form template in my model admin class
    insert_after = 'tieneSeccion'
    classes = ("collapse",)


class SubtemaInline(NestedStackedInline):
    model = Subtemas
    extra = 1
    show_change_link = True
    search_fields = ('nombre',)
    classes = ("collapse",)


class TemasInline(NestedStackedInline):
    model = Temas
    extra = 2
    show_change_link = True
    search_fields = ('nombre',)
    classes = ("collapse",)
    # This work because I have an extra package
    inlines = [SubtemaInline, ]


class CursoAdmin(NestedModelAdmin):
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
            'fields': ('titulo', 'descripcion', 'dias', 'costo', 'cupos', 'duracion', 'tieneSeccion', 'profesor', 'categoria', 'imagen', 'imagen_del_curso', 'video'),
        }), ('Prontuario', {'fields': ()}),
    )

    inlines = [
        TemasInline,
        SeccionInline
    ]
    # Preview de la imagen del curso
    readonly_fields = ["imagen_del_curso"]

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

    def imagen_del_curso(self, obj):
        """
        Esta funcion muestra la imagen como un preview en el admin. El parametro obj tiene acceso a todas las propiedades de este modelo que se esta modificando
        """
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.imagen.url,
            width=350,
            height=350,
        ))
    # TODO: Hacer lo mismo con el video. no me se el markuo html para el video


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
