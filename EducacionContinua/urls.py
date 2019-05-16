"""EducacionContinua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('inicio.urls')),
    path('profesor/', include('profesor.urls')),
    path('curso/', include('curso.urls')),
    path('inscribete/', include('inscribete.urls')),
    # Como el user login esta dentro de la pagina de inscribete. La url del users/login tienen que matchear con lo que ya esta en inscribete
    path('inscribete/users/', include('usuario.urls')),
    path('inscribete/users/', include('django.contrib.auth.urls')),
    path('matricula/', include('matricula.urls')),
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('nested_admin/', include('nested_admin.urls')),

]
# Add to the url patterns this for search media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
