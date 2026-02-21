from django.db import models
from datetime import date

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    data_nascimento = models.DateField(blank=True, null=True)
    estado = models.CharField(choices=[('AC', 'Acre'),
                                      ('AL', 'Alagoas'),
                                      ('AP', 'Amapá'),
                                      ('AM', 'Amazonas'),
                                      ('BA', 'Bahia'),
                                      ('CE', 'Ceará'),
                                      ('DF', 'Distrito Federal'),
                                      ('ES', 'Espírito Santo'),
                                      ('GO', 'Goiás'),
                                      ('MA', 'Maranhão'),
                                      ('MT', 'Mato Grosso'),
                                      ('MS', 'Mato Grosso do Sul'),
                                      ('MG', 'Minas Gerais'),
                                      ('PA', 'Pará'),
                                      ('PB', 'Paraíba'),
                                      ('PR', 'Paraná'),
                                      ('PE', 'Pernambuco'),
                                      ('PI', 'Piauí'),
                                      ('RJ', 'Rio de Janeiro'),
                                      ('RN', 'Rio Grande do Norte'),
                                      ('RS', 'Rio Grande do Sul'),
                                      ('RO', 'Rondônia'),                                     
                                      ('RR', 'Roraima'),
                                      ('SC', 'Santa Catarina'),
                                      ('SP', 'São Paulo'),
                                      ('SE', 'Sergipe'),
                                      ('TO', 'Tocantins'),
                                      ], blank=False, null=False, default='BA')
    endereco = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=False, null=False)

    def dias_para_aniversario(self):
        hoje = date.today()
        aniversario_este_ano = self.data_nascimento.replace(year=hoje.year)

        if aniversario_este_ano < hoje:
            aniversario_este_ano = aniversario_este_ano.replace(year=hoje.year + 1)

        return (aniversario_este_ano - hoje).days

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'Aluno'
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome']