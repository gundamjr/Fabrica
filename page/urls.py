from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$',views.consulta,name='Consulta'),
    url(r'^principal/$',views.principal,name='principal'),

    url(r'^cadastro/new/$', views.cadastro, name='cadastro'),
    url(r'^editar/edit/$',views.tabela_professor,name='Professores'),
    url(r'^post/(?P<pk>[0-9]+)/excluir/$', views.excluir, name='excluir'),
    url(r'^post/(?P<pk>[0-9]+)/editar/$', views.editar, name='editar'),

    url(r'^cadastro_prova/new/$', views.cadastro_Prova, name='cadastro_prova'),
    url(r'^post/(?P<pk>[0-9]+)/editar_Prova/$', views.editar_Prova, name='editar_Prova'),
    url(r'^post/(?P<pk>[0-9]+)/excluir_Prova/$', views.excluir_Prova, name='excluir_Prova'),
    url(r'^editar/editprovas/$',views.tabela_prova,name='Provas'),
    
    url(r'^cadastro_Disciplina/new/$', views.cadastro_Disciplina, name='cadastro_disciplina'),
    url(r'^post/(?P<pk>[0-9]+)/editar_Disciplina/$', views.editar_Disciplina, name='editar_disciplina'),
    url(r'^post/(?P<pk>[0-9]+)/excluir_Disciplina/$', views.excluir_Disciplina, name='excluir_disciplina'),
    url(r'^editar/editdisciplina/$',views.tabela_disciplina,name='Disciplinas'),

    url(r'^cadastro_curso/new/$', views.cadastro_curso, name='cadastro_curso'),
    url(r'^post/(?P<pk>[0-9]+)/editar_Curso/$', views.editar_Curso, name='editar_Curso'),
    url(r'^post/(?P<pk>[0-9]+)/excluir_Curso/$', views.excluir_Curso, name='excluir_Curso'),
    url(r'^editar/editcurso/$',views.tabela_curso,name='Cursos'),

    url(r'^Relatorio/$',views.some_view,name='relatorio'),
    url(r'^post/(?P<pk>[0-9]+)status/$',views.mudar_status,name='status'),





]