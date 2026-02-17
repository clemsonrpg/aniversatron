from rest_framework.serializers import ModelSerializer
from apps.emprestimos.models import Emprestimo

class EmprestimoSerializer(ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ('id', 'aluno_id', 'livro_id', 'data_emprestimo', 'status')