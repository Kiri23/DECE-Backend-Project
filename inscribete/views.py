from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import InscribeteForm
from .models import Registracion
from django.core.cache import cache
from curso.models import Curso


class Inscribete(FormView):
    """
    Esta clase es la que se encarga de guardar la información de la registración 
    """
    form_class = InscribeteForm
    template_name = "inscribete/inscribete.html"

    # def post(self, request, *args, **kwargs):
    def form_valid(self, form):
        """
         Si el form tiene información valida. Guarda la informacion en la base de datos.
        """
        print('aqui')
        form = InscribeteForm(data=self.request.POST)
        # No guardes la información del formulario en la base de datos todavia
        registracion = form.save(commit=False)
        # Añade la información del curso a la tabla de registracion
        registracion.curso = self.get_curso()
        # Añade la información del usuario a la tabla de registracion
        registracion.estudiante = self.request.user
        # Añade a la url de succes el id del usuario para utilizarlo para cuando valla a comprar el curso
        self.success_url = reverse_lazy('matricula',kwargs={'pk':self.request.user.id})

        registracion.save()
        form.save_m2m()

        return super().form_valid(form)

    def get_initial(self):
        """
        Este metodo initializa el form con la data del usuario como el nombre y otra informacion.
        """
        self.get_curso()
        initial = super(Inscribete, self).get_initial()
        if self.request.user.is_authenticated:
            # .. Aqui es donde initializo el form con la data del usuario
            initial.update({
                'nombre': self.request.user.username,
                'appellido': self.request.user.last_name,
                'correo_electronico': self.request.user.email})
        return initial

    def get_curso(self):
        """
        Este metodo se utiliza para obtener el curso al cual la persona se quiere inscribir
        """
        if 'curso' in cache:
            curso = cache.get('curso')
            print(curso.costo)
        else:
            curso_id = self.kwargs['pk']
            curso = Curso.objects.get(pk=curso_id)
            cache.set('curso', curso)

        return curso
