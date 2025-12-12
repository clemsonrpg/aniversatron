from django import forms
from django.forms import ModelForm, DateInput

from . import models
from .models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        exclude = ['data_criacao', 'ultima_modificacao']
        fields = '__all__'
