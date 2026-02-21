from django.contrib import messages

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
    context = {'form': form}
    return render(request, template_name, context)

def listar_pessoas(request):
    template_name = 'pessoas/listar_pessoas.html'
    pessoas = Pessoa.objects.all()
    context = {'pessoas': pessoas}
    return render(request, template_name, context)

def editar_pessoa(request, id):
    template_name = 'pessoas/form_pessoa.html'
    pessoa = get_object_or_404(Pessoa, id=id)
    form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)
    context = {'form': form}
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