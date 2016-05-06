from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Professor
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
@login_required
def principal(request):
	professores=Professor.objects.all()
	return render(request,'page/principal.html',{'professores':professores})

@login_required
def cadastro(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=True)
			return redirect('page.views.principal')
	else:
		form = PostForm()
	return render(request, 'page/cadastro.html', {'form': form})

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