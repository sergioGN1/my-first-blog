from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listar_trabajadores, name="listado"),
    url(r'^trabajador/new/$', views.nuevo_trabajador, name='d'),
    url(r'^trabajador/(?P<pk>[0-9]+)/update/$', views.actualizar_trabajador, name='actualizar_trabajador'),
    url(r'^trabajador/(?P<pk>[0-9]+)/delete/$', views.borrar_trabajador, name='delete_trabajador'),
]
