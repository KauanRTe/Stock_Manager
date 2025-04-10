from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Produto, Estoque
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages

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
            estoque_id = request.session.get('estoque_id')
            try:
                estoque = Estoque.objects.get(id=estoque_id, usuario=request.user)
                categoria.estoque = estoque
                categoria.save()
                return redirect('home:home')
            except Estoque.DoesNotExist:
                messages.error(request, 'Não foi possível criar a categoria. Estoque não encontrado.')
                pass

    else:
        form = forms.CategoriaForm()
    return render(request, 'estoque/criar_categoria.html', {'form': form})

@login_required
def criar_produto(request):
    if request.method == 'POST':
        form = forms.ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            estoque_id = request.session.get('estoque_id')
            try:
                estoque = Estoque.objects.get(id = estoque_id, usuario=request.user)
                produto.estoque = estoque
                produto.save()
                return redirect('home:home')
            except Estoque.DoesNotExist:
                messages.error(request, 'Não foi possível criar a categoria. Estoque não encontrado.')
                pass
    else:
        form = forms.ProdutoForm()
    return render(request, 'estoque/criar_produto.html', {'form': form})

@login_required
def criar_estoque(request):
    if request.method == 'POST':
        form = forms.EstoqueForm(request.POST)
        if form.is_valid():
            estoque = form.save(commit=False)
            estoque.usuario = request.user
            estoque.save()
            request.session['estoque_id'] = estoque.id
            return redirect('home:home')
    else:
        form = forms.EstoqueForm()
        
    return render(request, 'estoque/criar_estoque.html', {'form': form})


def configurar_estoques(request):
    return render(request, 'estoque/configurar_estoques.html')

def renomear_estoque(request, estoque_id=None):
    estoque_id = request.session.get('estoque_id')
    if not estoque_id:
        messages.error(request, 'Nenhum estoque selecionado.')
        return redirect('estoque:configurar_estoques')
    
    estoque = get_object_or_404(Estoque, id=estoque_id, usuario=request.user)

    if request.method == 'POST':
        form = forms.EstoqueForm(request.POST, instance=estoque)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estoque renomeado com Sucesso')
            return redirect('home:home')
    else:
        form = forms.EstoqueForm(instance=estoque)
    
    return render(request, 'estoque/renomear_estoque.html', {'form': form})

def deletar_estoque(request):
    estoque_id = request.session.get('estoque_id')
    if not estoque_id:
        messages.error(request, 'Nenhum estoque selecionado')
        return redirect('home:home')
    
    estoque = get_object_or_404(Estoque, id=estoque_id, usuario=request.user)

    if request.method == 'POST':
        estoque.delete()
        request.session.pop('estoque_id', None)
        messages.success(request, 'Estoque deletado com sucesso.')
        return redirect('home:home')
    
    return render(request, 'estoque/deletar_estoque.html', {'estoque': estoque})
    


            

