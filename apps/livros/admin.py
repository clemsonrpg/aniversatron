from django.contrib import admin
from .models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'edicao', 'numero_paginas')
    search_fields = ['titulo', 'autor']
