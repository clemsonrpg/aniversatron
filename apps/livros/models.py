from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    autor = models.CharField(max_length=100, blank=False, null=False)
    edicao = models.CharField(max_length=2)
    editora = models.CharField(max_length=50)
    ano_publicacao = models.DateField(blank=False, null=False)
    isbn = models.CharField(max_length=14)
    numero_paginas = models.IntegerField(blank=False, null=False)


    def __str__(self):
        return self.titulo


    class Meta:
        db_table = 'Livro'
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo']
