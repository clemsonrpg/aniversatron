from django.db import models
from datetime import date

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    data_nascimento = models.DateField(blank=True, null=True)

    LOCALIDADE_CHOICES = [
        ("GUAIBIM", "Guaibim"),
        ("GUEREM", "Guerém"),
        ("SERRA_GRANDE", "Serra Grande"),
        ("MARICOABO", "Maricoabo"),
        ("OROBO", "Orobó"),
        ("CAJAIBA", "Cajaíba"),
        ("JAGUARIPE", "Jaguaripe"),
        ("BONFIM", "Bonfim"),
        ("PEDRA_BRANCA", "Pedra Branca"),
        ("TABULEIRO_DA_VARZEA", "Tabuleiro da Várzea"),
        ("AGUA_MINERAL", "Água Mineral"),
        ("RIO_DO_MEIO", "Rio do Meio"),
        ("PIAU", "Piau"),
        ("SARAPUI", "Sarapuí"),
        ("CANTA_GALO", "Canta Galo"),
        ("RIACHAO_DA_SERRA", "Riachão da Serra"),
    ]

    localidade = models.CharField(
        max_length=50,
        choices=LOCALIDADE_CHOICES,
        blank=True,
        null=True
    )
    servico = models.ManyToManyField('servicos.Servico', blank=True, null=True, related_name='pessoas')
    endereco = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    def dias_para_aniversario(self):
        hoje = date.today()
        aniversario_este_ano = self.data_nascimento.replace(year=hoje.year)

        if aniversario_este_ano < hoje:
            aniversario_este_ano = aniversario_este_ano.replace(year=hoje.year + 1)

        return (aniversario_este_ano - hoje).days

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'Pessoa'
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['nome']