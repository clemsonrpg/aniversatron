from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Count
from apps.servicos.models import Servico
from apps.pessoas.models import Pessoa
from django.shortcuts import render
from django.db.models import Prefetch
import json
from django.db.models.functions import TruncMonth
from datetime import timedelta
from openpyxl import Workbook
from openpyxl.styles import Font

def index(request):
    hoje = timezone.localdate()

    aniversariantes = Pessoa.objects.filter(
        data_nascimento__month=hoje.month,
        data_nascimento__day=hoje.day
    )

    lista = []

    for p in aniversariantes:
        idade = hoje.year - p.data_nascimento.year - (
    (hoje.month, hoje.day) < (p.data_nascimento.month, p.data_nascimento.day)
    )   
        pessoa = Pessoa.objects.prefetch_related(
            Prefetch(
                'servicos',
                queryset=Servico.objects.order_by('-data_servico', '-id'),
                to_attr='servicos_ordenados'
            )
        ).get(id=p.id)

        lista.append({
            "nome": p.nome,
            "email": p.email,
            "telefone": p.telefone,
            "idade": idade,
            "servico": pessoa.servicos_ordenados[0].nome_servico if pessoa.servicos_ordenados else "Nenhum serviço cadastrado"
        })
    total_servicos = Servico.objects.count()
    context = {
        'total_pessoas': Pessoa.objects.count(),
        'total_servicos': total_servicos,
        'lista_aniversariantes': lista,
    }
    return render(request, 'index.html', context)




def relatorios(request):
    template_name = 'core/relatorios.html'
    hoje = timezone.localdate()


    servicos_mes = Servico.objects.filter(
        data_servico__month=hoje.month,
        data_servico__year=hoje.year
    )

    total_mes = servicos_mes.count()


    primeiro_dia_mes = hoje.replace(day=1)
    ultimo_mes = primeiro_dia_mes - timedelta(days=1)

    total_mes_anterior = Servico.objects.filter(
        data_servico__month=ultimo_mes.month,
        data_servico__year=ultimo_mes.year
    ).count()

    ultimos_6_meses = (
        Servico.objects
        .annotate(mes=TruncMonth('data_servico'))
        .values('mes')
        .annotate(total=Count('id'))
        .order_by('-mes')[:6]
    )

    dados_grafico = {
        "labels": [item['mes'].strftime("%m/%Y") for item in reversed(ultimos_6_meses)],
        "valores": [item['total'] for item in reversed(ultimos_6_meses)]
    }

    
    ranking_servicos = (
        Servico.objects
        .values('nome_servico')
        .annotate(total=Count('id'))
        .order_by('-total')[:5]
    )

    context = {
        "total_mes": total_mes,
        "total_mes_anterior": total_mes_anterior,
        "ranking_servicos": ranking_servicos,
        "grafico_dados": json.dumps(dados_grafico)
    }

    return render(request, template_name, context)







def relatorio_excel(request):
    hoje = timezone.localdate()

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="relatorio_servicos.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.title = "Relatório de Serviços"


    total_geral = Servico.objects.count()

    total_mes = Servico.objects.filter(
        data_servico__month=hoje.month,
        data_servico__year=hoje.year
    ).count()

    ranking = (
        Servico.objects
        .values("nome_servico")
        .annotate(total=Count("id"))
        .order_by("-total")[:5]
    )


    ws["A1"] = "SECRETARIA DE AGRICULTURA"
    ws["A1"].font = Font(size=14, bold=True)

    ws["A3"] = f"Relatório Estatístico - {hoje.strftime('%d/%m/%Y')}"
    ws["A3"].font = Font(bold=True)

    ws["A5"] = "Total Geral de Serviços:"
    ws["B5"] = total_geral

    ws["A6"] = "Total de Serviços no Mês Atual:"
    ws["B6"] = total_mes



    ws["A8"] = "Serviços Mais Realizados"
    ws["A8"].font = Font(size=12, bold=True)

    ws["A10"] = "Serviço"
    ws["B10"] = "Total"

    ws["A10"].font = Font(bold=True)
    ws["B10"].font = Font(bold=True)

    linha = 11
    for item in ranking:
        ws[f"A{linha}"] = item["nome_servico"]
        ws[f"B{linha}"] = item["total"]
        linha += 1

    ws.column_dimensions["A"].width = 40
    ws.column_dimensions["B"].width = 20

    wb.save(response)
    return response