from django.views import generic
from inscribete.models import Registracion


class MatriculaListView(generic.ListView):
    context_object_name = 'cursos_registrados'
    template_name = 'matricula/matricula_list.html'

    # Tengo que crear un metodo que me devuelva el total de costo para cada curso que el estudiante este registrado

    def get_queryset(self):
        """
        Devuelve las registraciones por estudiantes para que los estudiantes se puedan matricular
        """
        return Registracion.inscripciones.porEstudiante(estudianteId=self.kwargs['pk'])
