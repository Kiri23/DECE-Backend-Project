from django.urls import path, include
from . import views

app_name = 'curso'
urlpatterns = [
    path('<int:pk>', views.curso, name='curso'),
    path('', views.CursoListView.as_view(), name='lista_de_curso'),
    path('categorias', views.CategoriaListView.as_view(), name='categorias')
]
