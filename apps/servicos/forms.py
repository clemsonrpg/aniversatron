from django import forms
from .models import Servico
from apps.pessoas.models import Propriedade
from apps.pessoas.models import Pessoa




class ServicoForm(forms.ModelForm):
    pessoa = forms.ModelChoiceField(
        queryset=Pessoa.objects.all(),
        label="Pessoa",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_pessoa'}),
        required=True
    )

    class Meta:
        model = Servico
        fields = ['pessoa', 'propriedade', 'nome_servico', 'data_servico', 'status', 'descricao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Lógica para Edição (Carregar dados existentes)
        if self.instance and self.instance.pk and self.instance.propriedade:
            # Forçamos o valor inicial do campo 'pessoa'
            self.initial['pessoa'] = self.instance.propriedade.pessoa.pk
            # Filtramos as propriedades para mostrar apenas as do dono atual
            self.fields['propriedade'].queryset = Propriedade.objects.filter(
                pessoa=self.instance.propriedade.pessoa
            )
        else:
            # Para novos registros, começa vazio
            self.fields['propriedade'].queryset = Propriedade.objects.none()
            
            self.fields['pessoa'].widget.attrs.update({'id': 'id_pessoa'})

        # Lógica para manter os dados após um erro de validação (POST)
        if 'pessoa' in self.data:
            try:
                pessoa_id = int(self.data.get('pessoa'))
                self.fields['propriedade'].queryset = Propriedade.objects.filter(pessoa_id=pessoa_id)
            except (ValueError, TypeError):
                pass