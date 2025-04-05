from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Produto
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.

@login_required
def produtos_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug, estoque=request.user.estoque)
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, 'estoque/produtos_por_categoria.html', {'categoria': categoria, 'produtos': produtos})

@login_required
def criar_categoria(request):
    if request.method == 'POST':
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.estoque = request.user.estoque
            categoria.save()
            return redirect('relatorios:relatorio_estoque')
    else:
        form = forms.CategoriaForm()
    return render(request, 'estoque/criar_categoria.html', {'form': form})

@login_required
def criar_produto(request):
    if request.method == 'POST':
        form = forms.ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.estoque = request.user.estoque
            produto.save()
            return redirect('relatorios:relatorio_estoque')
    else:
        form = forms.ProdutoForm()
    return render(request, 'estoque/criar_produto.html', {'form': form})

            

