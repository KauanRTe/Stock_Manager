from django.shortcuts import render, redirect
from .forms import MovimentacaoForm

def nova_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relatorios:relatorio_estoque')
    else:
        form = MovimentacaoForm()

    return render(request, 'movimentacao/movimentacao_form.html', {'form': form})