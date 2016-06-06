from django import forms

from .models import Professor
from .models import Curso
from .models import Prova
from .models import status
from .models import Disciplina
from .models import Disciplina_Profesor
from .models import Disciplina_Curso

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
        fields = ()

class PostDisciplina(forms.ModelForm):

    class Meta:
        model = Disciplina
        fields = ('nome','periodo',)

class PostDisciplina_Professor(forms.ModelForm):

    class Meta:
        model = Disciplina_Profesor
        fields = ("Disciplina_id",)

class PostDisciplina_Curso(forms.ModelForm):

    class Meta:
        model = Disciplina_Curso
        fields=('Curso_id',)
                