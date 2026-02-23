from django.contrib import messages
from apps.servicos.models import Servico
from .forms import PessoaForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa

def inserir_pessoa(request):
    template_name = 'pessoas/form_pessoa.html'
    if request.method == 'POST':
        form = PessoaForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O cadastro da pessoa foi realizado com sucesso!')
        return redirect('core:index')
    form = PessoaForm()
    ultimo_servico = Servico.objects.order_by('data_servico').first()
    context = {'form': form, 'ultimo_servico': ultimo_servico}
    return render(request, template_name, context)

from django.db.models import Prefetch

def listar_pessoas(request):
    template_name = 'pessoas/listar_pessoas.html'

    pessoas = Pessoa.objects.prefetch_related(
        Prefetch(
            'servicos',
            queryset=Servico.objects.order_by('-data_servico'),
            to_attr='servicos_ordenados'
        )
    )

    context = {'pessoas': pessoas}
    return render(request, template_name, context)


def editar_pessoa(request, id):
    template_name = 'pessoas/form_pessoa.html'
    pessoa = get_object_or_404(Pessoa, id=id)
    form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)
    ultimo_servico = Servico.objects.filter(pessoa=pessoa).order_by('data_servico').first()
    context = {'form': form, 'ultimo_servico': ultimo_servico}
    if form.is_valid():
        form.save()
        messages.success(request, 'Os dados foram atualizados com sucesso.')
        return redirect('core:index')
    return render(request, template_name, context)

def excluir_pessoa(request, id):
    
    template_name = 'pessoas/excluir_pessoa.html'


    pessoa = Pessoa.objects.get(id=id)
    context = {'pessoa': pessoa}
    if request.method == "POST":
        pessoa.delete()
        messages.error(request, 'A pessoa foi excluída com sucesso.')
        return redirect('pessoas:listar_pessoas')
    return render(request, template_name, context)


def detalhe_pessoa(request, id):
    template_name = 'pessoas/detalhe_pessoa.html'
    pessoa = get_object_or_404(Pessoa, id=id)
    ultimo_servico = Servico.objects.filter(pessoa=pessoa).order_by('data_servico').first()
    context = {'pessoa': pessoa, 'ultimo_servico': ultimo_servico}
    return render(request, template_name, context)


