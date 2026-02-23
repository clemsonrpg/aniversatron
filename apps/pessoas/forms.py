from django import forms
from django.forms import ModelForm, DateInput

from . import models
from .models import Pessoa


class PessoaForm(forms.ModelForm):
        
    class Meta:
        model = Pessoa
        fields = 'data_nascimento', 'endereco', 'email', 'telefone', 'localidade', 'nome'
        widgets = {
            'data_nascimento': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
            'endereco': forms.TextInput(
                attrs={'placeholder': 'Digite o endereço completo'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Digite o email da pessoa (se houver)'}
            ),
            'telefone': forms.TextInput(
                attrs={'placeholder': 'Digite o telefone'}
            ),
            'localidade': forms.Select(
                attrs={'placeholder': 'Selecione a localidade'}
            ),
            'nome': forms.TextInput(
                attrs={'placeholder': 'Digite o nome completo da pessoa'}
            ),
        }