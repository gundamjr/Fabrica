from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .forms import PostCurso
from .forms import PostProva
from .forms import PostStatus
from .forms import PostDisciplina
from .models import Professor
from .models import status
from .models import Curso
from .models import Prova
from .models import Disciplina
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
@login_required
def principal(request):
	professores=Professor.objects.all()
	cursos=Curso.objects.all()
	provas=Prova.objects.all()
	return render(request,'page/principal.html',{'professores':professores,'provas':provas,'cursos':cursos})

@login_required
def cadastro(request):
	cad=" Professor"
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=True)
			return redirect('page.views.principal')
	else:
		form = PostForm()
	return render(request, 'page/cadastro.html', {'form': form,'cad':cad})

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
	cad=" Curso"
	if request.method=="POST":
		form = PostCurso(request.POST)
		if form.is_valid():
			post=form.save(commit=True)
			return redirect('page.views.principal')
	else:
		form=PostCurso()
	return render (request,'page/cadastro.html',{'form':form,'cad':cad})			

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
	cad=" Prova"
	if request.method == "POST":
		form = PostProva(request.POST)
		form2= PostStatus(request.POST)
		if form.is_valid() and form2.is_valid():
			post2=form2.save(commit=True)
			post = form.save(commit=False)
			post.Prova_id_status=post2
			post.save()
			return redirect('page.views.principal')
	else:
		form = PostProva()
		form2= PostStatus()
	return render(request, 'page/cadastro.html', {'form': form,'form2':form2,'cad':cad})


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
	cad=" Disciplina"
	if request.method == "POST":
		form = PostDisciplina(request.POST)
		if form.is_valid() and form2.is_valid():
			post = form.save(commit=True)
			post.save()
			return redirect('page.views.principal')
	else:
		form = PostDisciplina()
	return render(request, 'page/cadastro.html', {'form': form,'cad':cad})


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
