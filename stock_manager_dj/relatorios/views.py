from django.shortcuts import render
from django.db.models import Sum, F, Case, When
from estoque.models import Produto
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def relatorio_estoque(request):
    estoque_usuario = request.user.estoque

    produtos = Produto.objects.filter(estoque=estoque_usuario).annotate(
        total_estoque = Sum(
            Case(
                When(movimentacoes__tipo = "entrada", then=F("movimentacoes__quantidade")),
                When(movimentacoes__tipo = "saida", then=-F("movimentacoes__quantidade")),
                default = 0
            )
        )
    )
    return render(request, 'estoque/relatorio_estoque.html', {"produtos": produtos})
