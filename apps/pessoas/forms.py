from django import forms
from django.forms import ModelForm, DateInput
from django.forms import inlineformset_factory
from . import models
from .models import Pessoa, Propriedade


class PessoaForm(forms.ModelForm):
        
    class Meta:
        model = Pessoa
        fields = 'data_nascimento', 'endereco', 'email', 'telefone', 'nome'
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

            'nome': forms.TextInput(
                attrs={'placeholder': 'Digite o nome completo da pessoa'}
            ),
        }
    
class PropriedadeForm(forms.ModelForm):
    class Meta:
        model = Propriedade
        fields = ('nome_propriedade', 'localidade')
        widgets = {
            'nome_propriedade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome da propriedade'
            }),
            'localidade': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

PropriedadeFormSet = inlineformset_factory(
    Pessoa,
    Propriedade,
    form=PropriedadeForm,
    extra=1,
    can_delete=True
)