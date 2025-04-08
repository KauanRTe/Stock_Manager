from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FornecedorForm
from .models import Estoque
from django.contrib import messages

# Create your views here.
@login_required
def criar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            fornecedor = form.save(commit=False)
            estoque_id = request.session.get('estoque_id')
            try:
                estoque = Estoque.objects.get(id=estoque_id, usuario=request.user)
                fornecedor.estoque = estoque
                fornecedor.save()
                return redirect('home:home')
            except Estoque.DoesNotExist:
                messages.error(request, 'Não foi possível criar a categoria. Estoque não encontrado.')
                pass
    else:
        form = FornecedorForm()
        return render(request, 'fornecedores/criar_fornecedor.html', {'form': form})
