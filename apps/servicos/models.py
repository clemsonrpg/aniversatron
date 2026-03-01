from django.db import models
from datetime import date

from apps.pessoas.models import Pessoa, Propriedade
# Create your models here.
class Servico(models.Model):
    nome_servico = models.CharField(max_length=100, choices=[
        ("CEFIR", "Cefir"), ("Contrato de comodato", "Contrato de comodato"), ("Declaração de posse", "Declaração de posse"), ("CCIR", "CCIR"), ("ITR", "ITR"), ("Compra e venda", "Compra e venda"), ("Doação de imóvel", "Doação de imóvel")])
    descricao = models.TextField(blank=True, null=True)
    data_servico = models.DateField(default=date.today)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    propriedade = models.ForeignKey(
        Propriedade,
        on_delete=models.CASCADE,
        related_name='servicos',
        null=True,
        blank=True
    )
    
    
    pessoa = models.ForeignKey(
        Pessoa, 
        on_delete=models.CASCADE, 
        related_name='servicos', 
        null=True, 
        blank=True
    )

    status = models.CharField(max_length=20, choices=[("Pendente", "Pendente"), ("Concluído", "Concluído")], default="Pendente")