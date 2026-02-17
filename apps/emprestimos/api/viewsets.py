from rest_framework.viewsets import ModelViewSet
from apps.emprestimos.models import Emprestimo
from apps.emprestimos.api.serializers import EmprestimoSerializer

class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer