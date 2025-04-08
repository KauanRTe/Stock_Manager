from django.shortcuts import render, redirect
from estoque.forms import SelecionarEstoqueForm
from estoque.models import Estoque

def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SelecionarEstoqueForm(request.POST, usuario=request.user)
            if form.is_valid():
                request.session['estoque_id'] = form.cleaned_data['estoque'].id
                return redirect('home:home')
        else:
            form = SelecionarEstoqueForm(usuario=request.user)

        estoque_selecionado = None
        if 'estoque_id' in request.session:
            try:
                    estoque_selecionado = Estoque.objects.get(id=request.session['estoque_id'], usuario=request.user)
            except Estoque.DoesNotExist:
                    estoque_selecionado = None

        estoques = Estoque.objects.filter(usuario=request.user)

        return render(request, 'home/home.html', {
            'form': form,
            'estoque_selecionado': estoque_selecionado,
            'estoques': estoques
        })
    
    else:
        return render(request, 'home/home.html')
