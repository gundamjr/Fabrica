from django import forms

from .models import Professor
from .models import Curso
from .models import Prova
from .models import status
from .models import Disciplina

class PostForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ('nome', 'matricula','email',)


class PostCurso(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ('nome', 'turma',)



class PostProva(forms.ModelForm):

    class Meta:
        model = Prova
        fields = ('data_prova', 'data_limite','estagio',)

class PostStatus(forms.ModelForm):

    class Meta:
        model = status
        fields = ('devolucao', 'data_devolucao',)

class PostDisciplina(forms.ModelForm):

    class Meta:
        model = Disciplina
        fields = ('nome', 'periodo',)


                