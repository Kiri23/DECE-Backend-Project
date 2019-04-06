from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio.as_view(), name='inicio'),
    path('ajax/listaDeCurso', views.obtenerCategoriaFromAjax, name='ajax_cursos'),
]
