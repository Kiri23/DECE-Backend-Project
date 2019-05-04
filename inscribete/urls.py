from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.Inscribete.as_view(), name='inscribete')
]
