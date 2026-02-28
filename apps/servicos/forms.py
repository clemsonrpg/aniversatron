from django import forms
from .models import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['propriedade', 'nome_servico', 'data_servico', 'status', 'descricao']
        widgets = {
            'propriedade': forms.Select(attrs={'class': 'form-control'}),
            'nome_servico': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a descrição do serviço',
                'rows': 3
            }),
            'data_servico': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'},
                format='%Y-%m-%d'
            ),
        }