from django import forms

from .models import Professor

class PostForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ('nome', 'matricula','email',)