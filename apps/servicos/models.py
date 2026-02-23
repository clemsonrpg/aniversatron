from django.db import models
from datetime import date
# Create your models here.
class Servico(models.Model):
    nome_servico = models.CharField(max_length=100, choices=[
        ("CEFIR", "Cefir"), ("Contrato de comodato", "Contrato de comodato"), ("Declaração de posse", "Declaração de posse"), ("CCIR", "CCIR"), ("ITR", "ITR"), ("Compra e venda", "Compra e venda"), ("Doação de imóvel", "Doação de imóvel")])
    descricao = models.TextField(blank=True, null=True)
    data_servico = models.DateField(default=date.today)
    data_criacao = models.DateTimeField(auto_now_add=True)
    pessoa = models.ForeignKey('pessoas.Pessoa', on_delete=models.CASCADE, related_name='servicos')