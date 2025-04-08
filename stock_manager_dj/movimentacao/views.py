from django.shortcuts import render, redirect
from .forms import MovimentacaoForm
from django.contrib.auth.decorators import login_required
from .models import Estoque
from django.contrib import messages

@login_required
def nova_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            estoque_id = request.session.get('estoque_id')
            movimentacao = form.save(commit=False)
            try:
                estoque = Estoque.objects.get(id=estoque_id, usuario=request.user)
                movimentacao.estoque = estoque
                movimentacao.save()
                return redirect('relatorios:relatorio_estoque')
            except Estoque.DoesNotExist:
                messages.error(request, 'Não foi possível criar a categoria. Estoque não encontrado.')
                pass
    else:
        form = MovimentacaoForm()

    return render(request, 'movimentacao/movimentacao_form.html', {'form': form})