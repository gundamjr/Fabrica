from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.principal),
    url(r'^cadastro/new/$', views.cadastro, name='cadastro'),

    url(r'^cadastro_prova/new/$', views.cadastro_Prova, name='cadastro_prova'),
    url(r'^post/(?P<pk>[0-9]+)/editar_Prova/$', views.editar_Prova, name='editar_Prova'),
    url(r'^post/(?P<pk>[0-9]+)/excluir_Prova/$', views.excluir_Prova, name='excluir_Prova'),
    url(r'^post/(?P<pk>[0-9]+)/editar/$', views.editar, name='editar'),

    url(r'^post/(?P<pk>[0-9]+)/excluir/$', views.excluir, name='excluir'),
    url(r'^cadastro_curso/new/$', views.cadastro_curso, name='cadastro_curso'),
    url(r'^post/(?P<pk>[0-9]+)/editar_Curso/$', views.editar_Curso, name='editar_Curso'),
    url(r'^post/(?P<pk>[0-9]+)/excluir_Curso/$', views.excluir_Curso, name='excluir_Curso'),


]