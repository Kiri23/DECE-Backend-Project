from django.shortcuts import render
from django.views import generic
from .models import Profesor


class ProfesorDetailView(generic.DetailView):
    model = Profesor
    context_object_name = 'profesor'
