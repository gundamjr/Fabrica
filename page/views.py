from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .forms import PostCurso
from .forms import PostProva
from .forms import PostStatus
from .forms import PostDisciplina
from .forms import PostDisciplina_Professor
from .forms import PostDisciplina_Curso
from .models import Professor
from .models import status
from .models import Curso
from .models import Prova
from .models import Disciplina
from .models import Disciplina_Profesor
from .models import Disciplina_Curso
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
# Create your views here.


@login_required
def principal(request):
	professores=Professor.objects.all()
	cursos=Curso.objects.all()
	provas=Prova.objects.all()
	Disciplinas_professor=Disciplina_Profesor.objects.all()
	disciplinas=Disciplina.objects.all()
	disciplinas_cursos=Disciplina_Curso.objects.all()
	return render(request,'page/principal.html',{'disciplinas_cursos':disciplinas_cursos,'disciplinas':disciplinas,'Disciplinas_professor':Disciplinas_professor,'professores':professores,'provas':provas,'cursos':cursos})

@login_required
def cadastro(request):
	disciplinas=Disciplina.objects.all()	
	if request.method == "POST":
		form = PostForm(request.POST)
		form2 = PostDisciplina_Professor(request.POST)
		if form.is_valid():
			post = form.save()
			post2=form2.save(commit=False)
			post2.Professor_id = post
			post2.save()
			return redirect('page.views.principal')
	else:
		form = PostForm()
	return render(request, 'page/cadastro_professor.html', {'disciplinas':disciplinas})

@login_required
def editar(request, pk):
	post = get_object_or_404(Professor, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=True)
			return redirect('page.views.principal')
	else:
		form = PostForm(instance=post)
	return render(request, 'page/cadastro.html', {'form': form})

@login_required
def excluir(request, pk):
	post=get_object_or_404(Professor, pk=pk)
	post.delete()
	return redirect('page.views.principal')


@login_required
def cadastro_curso(request):
	if request.method=="POST":
		form = PostCurso(request.POST)
		if form.is_valid():
			post=form.save(commit=True)
			return redirect('page.views.principal')
	else:
		form=PostCurso()
	return render (request,'page/cadastro_curso.html',{'form':form})			

@login_required
def editar_Curso(request, pk):
	post = get_object_or_404(Curso, pk=pk)
	if request.method == "POST":
		form = PostCurso(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=True)
			return redirect('page.views.principal')
	else:
		form = PostCurso(instance=post)
	return render(request, 'page/cadastro.html', {'form': form})

@login_required
def excluir_Curso(request, pk):
	post=get_object_or_404(Curso, pk=pk)
	post.delete()
	return redirect('page.views.principal')	

@login_required
def cadastro_Prova(request):
	professores=Professor.objects.all()
	cursos=Curso.objects.all()
	provas=Prova.objects.all()
	disciplinas=Disciplina.objects.all()
	if request.method == "POST":
		form = PostDisciplina_Professor(request.POST)
		form2 = PostProva(request.POST)
		form3 = PostDisciplina_Curso(request.POST)
		if form.is_valid():
			post=form.save(commit=True)
			post2=form2.save(commit=True)
			post3=form3.save(commit=True)
			return redirect('page.views.principal')
	else:
		form = PostProva()
	return render(request, 'page/cadastro_Prova.html',{'professores':professores,'disciplinas':disciplinas,'form': form,'provas':provas,'cursos':cursos})


@login_required
def editar_Prova(request, pk):
	post = get_object_or_404(Prova, pk=pk)
	if request.method == "POST":
		form = PostProva(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=True)
			return redirect('page.views.principal')
	else:
		form = PostProva(instance=post)
	return render(request, 'page/cadastro.html', {'form': form})

@login_required
def excluir_Prova(request, pk):
	post=get_object_or_404(Prova, pk=pk)
	post.delete()
	return redirect('page.views.principal')	


@login_required
def cadastro_Disciplina(request):
	cursos=Curso.objects.all()
	if request.method == "POST":
		form = PostDisciplina(request.POST)
		form2= PostDisciplina_Curso(request.POST)
		if form.is_valid() and form2.is_valid():
			post = form.save(commit=True)
			post2=form2.save(commit=False)
			post2.Disciplina_id=post
			post2.save()
			return redirect('page.views.principal')
	else:
		form = PostDisciplina()
		form2= PostDisciplina_Curso()
	return render(request, 'page/cadastro_disciplina.html', {'form2':form2,'cursos':cursos,'form': form})


@login_required
def editar_Disciplina(request, pk):
	post = get_object_or_404(Disciplina, pk=pk)
	if request.method == "POST":
		form = PostProva(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=True)
			return redirect('page.views.principal')
	else:
		form = PostDisciplina(instance=post)
	return render(request, 'page/cadastro.html', {'form': form})

@login_required
def excluir_Disciplina(request, pk):
	post=get_object_or_404(Disciplina, pk=pk)
	post.delete()
	return redirect('page.views.principal')	
