from pyexpat.errors import messages

from django.shortcuts import get_object_or_404, redirect, render
from apps.pessoas.forms import PessoaForm
from apps.pessoas.models import Pessoa


def index(request):

    total_pessoas = Pessoa.objects.count()
    pessoas = Pessoa.objects.all()
    template_name = 'index.html'
    context = {'total_pessoas': total_pessoas, 'pessoas': pessoas}
    return render(request, template_name, context)

