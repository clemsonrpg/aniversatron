from django.contrib import messages

from django.shortcuts import redirect, redirect, render
from .forms import ServicoForm
from apps.pessoas.models import Pessoa
from apps.servicos.models import Servico

# Create your views here.
def inserir_servico(request):
    template_name = 'servicos/form_servico.html'
    if request.method == 'POST':
        form = ServicoForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O cadastro do serviço foi realizado com sucesso!')
        return redirect('servicos:listar_servicos')
    form = ServicoForm()
    context = {'form': form}
    return render(request, template_name, context)

def listar_servicos(request):
    template_name = 'servicos/listar_servicos.html'
    servicos = Servico.objects.all().order_by('-data_servico', '-id')
    pessoas = Pessoa.objects.all()
    context = {'servicos': servicos, 'pessoas': pessoas}
    return render(request, template_name, context)

def editar_servico(request, id):
    template_name = 'servicos/form_servico.html'
    servico = Servico.objects.get(id=id)
    form = ServicoForm(request.POST or None, request.FILES or None, instance=servico)
    context = {'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, 'Os dados foram atualizados com sucesso.')
        return redirect('core:index')
    return render(request, template_name, context)

def excluir_servico(request, id):
    template_name = 'servicos/excluir_servico.html'
    servico = Servico.objects.get(id=id)
    context = {'servico': servico}
    if request.method == "POST":
        servico.delete()
        messages.warning(request, 'O serviço foi excluído com sucesso.')
        return redirect('servicos:listar_servicos')
    return render(request, template_name, context)

def detalhe_servico(request, id):
    template_name = 'servicos/detalhe_servico.html'
    servico = Servico.objects.get(id=id)
    context = {'servico': servico}
    return render(request, template_name, context)
