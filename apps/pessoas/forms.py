from django import forms
from django.forms import ModelForm, DateInput

from . import models
from .models import Pessoa


class PessoaForm(forms.ModelForm):
        
    class Meta:
        model = Pessoa
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
            'endereco': forms.TextInput(
                attrs={'placeholder': 'Digite o endereço completo'}
            )
        }