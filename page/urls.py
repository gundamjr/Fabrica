from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.principal),
    url(r'^cadastro/new/$', views.cadastro, name='cadastro'),
    url(r'^post/(?P<pk>[0-9]+)/editar/$', views.editar, name='editar'),
    url(r'^post/(?P<pk>[0-9]+)/excluir/$', views.excluir, name='excluir'),
]