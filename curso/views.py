from django.shortcuts import render

# Create your views here.


def curso(request):
    return render(request, "curso/curso_detail.html")
