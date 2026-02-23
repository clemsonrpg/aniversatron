from django.forms import ModelForm
from django import forms

from .models import Servico

class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'placeholder': 'Digite a descrição do serviço'}),
            'data_servico': forms.DateInput(attrs={'type': 'date'}),
        }