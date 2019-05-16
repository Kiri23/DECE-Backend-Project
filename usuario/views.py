from django.urls import reverse_lazy
from django.views import generic, View
from django.core.mail import send_mail
import logging

from .forms import CustomUserCreationForm
from .models import CustomUser

# Refactor this later
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('usuario:signup')
    template_name = 'inscribete/inscribete.html'

    def form_valid(self, form):
        logger = logging.getLogger(__name__)
        email_Form = form.cleaned_data['email']
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        form.save()
        print('form valido email: ', email_Form)
        print('form valido email: ', username)
        print('form valido email: ', password)
        user = authenticate(username=username, password=password)
        print('usuario ', user)
        login(self.request, user)
        print('autenticado')

        logger.debug((str(user)), 'form valid function')
        logger.debug((str(email_Form)), 'email form')
        send_mail(
            'Cuenta creada en Educación Continua',
            'Bienvenido a tu cuenta',
            'from@example.com',
            [str(email_Form)],
            fail_silently=False,
        )
        logger.info('email sent')
        logger.debug(('----user', user))
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form invalido. valor del form abajo')
        print(form.errors)
        return super().form_invalid(form)


class Profile(generic.DetailView):
    template_name = 'usuario/profile.html'
    queryset = CustomUser.objects.all()


class ChangePassword(View):
    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')

    def get(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user)
        return render(request, 'registration/password_change_form.html', {
            'form': form})
