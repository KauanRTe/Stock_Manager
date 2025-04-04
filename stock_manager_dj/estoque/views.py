from django.shortcuts import render, get_object_or_404
from .models import Categoria, Produto
from django.http import HttpResponse

# Create your views here.

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/lista_produtos.html', {'produtos': produtos})

def home(request):
    return HttpResponse("<h1>Bem-vindo ao Stock Manager!</h1>")

def produtos_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, 'estoque/produtos_por_categoria.html', {'categoria': categoria, 'produtos': produtos})
