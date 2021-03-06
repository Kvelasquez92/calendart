"""calendArt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', login, {'template_name':'miembros/index.html'}, name='login'),
    url(r'^logout/', logout, {'next_page':'home:index'}, name='logout'),
    url(r'^members/', include('apps.miembros.urls', namespace = 'member')),
    url(r'^members/requests', include('apps.miembros.urls', namespace = 'member1')), #se repiten entradas para el mismo archivo para que funcion
    url(r'^members/detail/', include('apps.miembros.urls', namespace = 'member2')), #la carga de imagenes
    url(r'^events/', include('apps.agenda.urls', namespace = 'event')),
    url(r'^notes/', include('apps.notas.urls', namespace = 'note')),
    url(r'^', include('apps.agenda.urls', namespace='home')),
]
