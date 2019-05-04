from django.urls import path, include
from . import views


urlpatterns = [
    path('<int:pk>', views.MatriculaListView.as_view(), name='matricula')
]
