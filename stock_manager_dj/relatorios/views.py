from django.shortcuts import render, redirect
from django.db.models import Sum, F, Case, When, Max
from django.core.paginator import Paginator
from estoque.models  import Produto
from movimentacao.models import Movimentacao
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def relatorio_estoque(request):
    estoque_usuario = request.session['estoque_id']

    if estoque_usuario is None:
        messages.error(request, "Selecione um estoque antes de acessar o relatório.")
        return redirect('home')

    produtos = Produto.objects.filter(estoque=estoque_usuario).annotate(
        total_estoque = Sum(
            Case(
                When(movimentacoes__tipo = "entrada", then=F("movimentacoes__quantidade")),
                When(movimentacoes__tipo = "saida", then=-F("movimentacoes__quantidade")),
                default = 0
            )
        )
    )

    paginator = Paginator(produtos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ultimas_datas = (
        Movimentacao.objects.values("produto").annotate(ultima_data=Max('data'))
    )

    datas_dict = {item['produto']: item['ultima_data'] for item in ultimas_datas}

    return render(request, 'relatorios/relatorio_estoque.html', {"produtos": produtos, "datas_dict": datas_dict, "page_obj": page_obj})
