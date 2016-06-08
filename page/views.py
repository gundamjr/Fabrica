from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import datetime
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
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from datetime import date
from reportlab.lib.pagesizes import A4, cm
from django.shortcuts import redirect
from django.utils import timezone
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
def tabela_professor(request):
	professores=Professor.objects.filter().order_by("nome")
	return render(request, 'page/tabela_professor.html', {'professores':professores})

@login_required
def tabela_curso(request):
	cursos=Curso.objects.filter().order_by("nome")
	return render(request,'page/tabela_curso.html',{'cursos':cursos})	

@login_required
def tabela_disciplina(request):
	disciplinas=Disciplina.objects.filter().order_by("nome")
	return render(request,'page/tabela_disciplina.html',{'disciplinas':disciplinas})	

@login_required
def tabela_prova(request):
	provas=Disciplina_Profesor.objects.all()
	return render(request,'page/tabela_prova.html',{'provas':provas})

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
	return render(request, 'page/editar_professor.html', {'post': post})

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
	return render(request, 'page/editar_curso.html', {'post': post})

@login_required
def excluir_Curso(request, pk):
	post=get_object_or_404(Curso, pk=pk)
	post.delete()
	return redirect('page.views.principal')	

@login_required
def cadastro_Prova(request):
	professores = Disciplina_Profesor.objects.filter().order_by('Professor_id')
	disciplinas = Disciplina_Curso.objects.filter().order_by('id_Disciplina_Curso')
	cursos = Disciplina_Curso.objects.filter().order_by('Curso_id')
	if request.method == 'POST':
		form = PostProva(request.POST)
		form2 = PostStatus(request.POST)
		form3 = request.POST.get('Disciplina_id')
		disciplina = get_object_or_404(Disciplina, pk=form3)
		fieldDisc = {'nome': disciplina.nome,
					 'periodo': disciplina.periodo}
		form4 = PostDisciplina(fieldDisc, instance = disciplina)
		if form.is_valid() and form2.is_valid() and form4.is_valid():
			post2 = form2.save()
			post = form.save(commit=False)
			post.id_status = post2
			post.save()
			post3 = form4.save(commit=False)
			post3.id_prova = post
			post3.id_status = post2
			post3.save()
			return redirect('page.views.principal')
	return render(request, 'page/cadastro_Prova.html', {'professores': professores, 'cursos': cursos, 'disciplinas': disciplinas})


@login_required
def editar_Prova(request, pk):
	post = get_object_or_404(Disciplina_Profesor, pk=pk)
	print(post.Disciplina_id.id_prova.estagio)
	if request.method == "POST":
		form = PostProva(request.POST, instance=post.Disciplina_id.id_prova)
		if form.is_valid() :
			post = form.save() #salva Prova
			return redirect('page.views.principal')
	else:
		form = PostProva(instance=post)
	return render(request, 'page/editar_prova.html', {'post': post})

@login_required
def excluir_Prova(request, pk):
	post=get_object_or_404(Disciplina, pk=pk)
	post2 = get_object_or_404(Prova, pk=post.id_prova.id_prova)
	post3= get_object_or_404(status,pk=post2.id_status.id_status)
	post2.id_status=None
	post.id_prova = None
	post.save()
	post2.delete()
	post3.delete()
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
		form = PostDisciplina(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=True)
			return redirect('page.views.principal')
	else:
		form = PostDisciplina(instance=post)
	return render(request, 'page/editar_disciplina.html', {'post': post})

@login_required
def excluir_Disciplina(request, pk):
	post=get_object_or_404(Disciplina, pk=pk)
	post.delete()
	return redirect('page.views.principal')	


@login_required
def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

@login_required
def consulta(request):
	professores = Disciplina_Profesor.objects.filter().order_by('Professor_id')
	disciplinas = Disciplina_Curso.objects.filter().order_by('id_Disciplina_Curso')
	if request.method == 'POST':
			form = request.POST.get('estagio')
			form2= request.POST.get('status')
			if form2=="nulo" and form=="0":
				post=Disciplina_Profesor.objects.filter(Disciplina_id__id_prova__id_status__devolucao__icontains=True)
				vetor=set()
				for x in post:
					if x.Disciplina_id.id_prova.id_status.data_devolucao<= x.Disciplina_id.id_prova.data_limite:
						vetor.add(x)

				post2=Disciplina_Profesor.objects.filter(Disciplina_id__id_prova__id_status__devolucao__icontains=False)
				vetor2=set()
				for y in post2:
					if date.today()<= y.Disciplina_id.id_prova.data_limite:
						vetor2.add(x)

				post3=Disciplina_Profesor.objects.filter(Disciplina_id__id_prova__id_status__devolucao=True)
				vetor3=set()
				for x in post3:
					if x.Disciplina_id.id_prova.id_status.data_devolucao> x.Disciplina_id.id_prova.data_limite:
						vetor3.add(x)			
				
				post4=Disciplina_Profesor.objects.filter(Disciplina_id__id_prova__id_status__devolucao=False)
				vetor4=set()
				for x in post4:
					if date.today()> x.Disciplina_id.id_prova.data_limite:
						vetor4.add(x)

				aux=True
				return render (request,'page/resultado.html',{'aux':aux,'d_p':vetor,'d_p2':vetor2,'d_p3':vetor3,'d_p4':vetor4})
			
			if form2=="nulo" and form!="0":
				post=Disciplina_Profesor.objects.filter(Disciplina_id__id_prova__estagio__contains=form)
				return render (request,'page/resultado.html',{'Disciplinas_professor':post})			
			
			if form2=="True" and form=="0":
				post=Disciplina_Profesor.objects.filter(Disciplina_id__id_prova__id_status__devolucao__icontains=form2)
				stts="Dentro do prazo"
				vetor=set()
				for x in post:
					if x.Disciplina_id.id_prova.id_status.data_devolucao<= x.Disciplina_id.id_prova.data_limite:
						vetor.add(x)
				
				return render (request,'page/resultado.html',{'Disciplinas_professor':vetor,'eca':stts})	
			
			if form2=="True" and form!="0":
				post=Disciplina_Profesor.objects.filter(Disciplina_id__id_prova__estagio__contains=form).filter(Disciplina_id__id_prova__id_status__devolucao__icontains=form2)
				stts="Dentro do prazo"
				vetor=set()
				for x in post:
					if x.Disciplina_id.id_prova.id_status.data_devolucao<= x.Disciplina_id.id_prova.data_limite:
						vetor.add(x)
				
				return render (request,'page/resultado.html',{'Disciplinas_professor':vetor,'eca':stts})			
			
			if form2=="False" and form=="0":
				post=Disciplina_Profesor.objects.filter(Disciplina_id__id_prova__id_status__devolucao__icontains=form2)
				stts="Dentro do prazo"
				vetor=set()
				for x in post:
					if x.Disciplina_id.id_prova.id_status.data_devolucao<= x.Disciplina_id.id_prova.data_limite:
						print("destiny gundam")
						vetor.add(x)
				
				return render (request,'page/resultado.html',{'Disciplinas_professor':vetor,'aeca':stts})	
			
			if form2=="False" and form!="0":
				post=Disciplina_Profesor.objects.filter(Disciplina_id__id_prova__estagio__contains=form).filter(Disciplina_id__id_prova__id_status__devolucao__icontains=form2)
				stts="Dentro do prazo"
				vetor=set()
				for x in post:
					if x.Disciplina_id.id_prova.id_status.data_devolucao<= x.Disciplina_id.id_prova.data_limite:
						vetor.add(x)
				
				return render (request,'page/resultado.html',{'Disciplinas_professor':vetor,'aeca':stts})			

			if form2=="dca" and form=="0":	
				post=Disciplina_Profesor.objects.filter(Disciplina_id__id_prova__id_status__devolucao=True)
				stts="Atrasado"
				vetor=set()
				for x in post:
					if x.Disciplina_id.id_prova.id_status.data_devolucao> x.Disciplina_id.id_prova.data_limite:
						vetor.add(x)
				return render (request,'page/resultado.html',{'Disciplinas_professor':vetor,'eca':stts})
		
			
			if form2=="dca" and form!="0":
				post=Disciplina_Profesor.objects.filter(Disciplina_id__id_prova__id_status__devolucao=True).filter(Disciplina_id__id_prova__estagio__contains=form)
				stts="Atrasado"
				vetor=set()
				for x in post:
					if x.Disciplina_id.id_prova.id_status.data_devolucao> x.Disciplina_id.id_prova.data_limite:
						vetor.add(x)
				return render (request,'page/resultado.html',{'Disciplinas_professor':vetor,'eca':stts})

			if form2=="aeca" and form=="0":
				post=Disciplina_Profesor.objects.filter(Disciplina_id__id_prova__id_status__devolucao=False)
				vetor=set()
				for x in post:
					if date.today()> x.Disciplina_id.id_prova.data_limite:
						vetor.add(x)
				return render (request,'page/resultado.html',{'Disciplinas_professor':vetor})

			if form2=="aeca" and form!="0":
				post=Disciplina_Profesor.objects.filter(Disciplina_id__id_prova__id_status__devolucao=False).filter(Disciplina_id__id_prova__estagio__contains=form)
				vetor=set()
				for x in post:
					if date.today()> x.Disciplina_id.id_prova.data_limite:
						vetor.add(x)
				return render (request,'page/resultado.html',{'Disciplinas_professor':vetor})							



	return render (request,'page/Tela_consulta.html',{'professores':professores})

@login_required
def mudar_status(request,pk):
	post=get_object_or_404(Disciplina,pk=pk)
	post2=get_object_or_404(Prova,pk=post.id_prova.id_prova)
	post3=get_object_or_404(status,pk=post2.id_status.id_status)
	if post3.devolucao:
		post3.devolucao=False
		post3.data_devolucao=None
		post3.save()
		print(post3.data_devolucao)
		return redirect('page.views.principal')	
	post3.devolucao=True
	post3.data_devolucao=timezone.now()
	post3.save()
	print(post3.data_devolucao)
	return redirect('page.views.principal')	