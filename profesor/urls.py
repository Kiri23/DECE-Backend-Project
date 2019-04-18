from django.urls import path, include
from . import views

app_name = 'profesor'
urlpatterns = [
    path('<int:pk>', views.ProfesorDetailView.as_view(), name='profesor')
]
