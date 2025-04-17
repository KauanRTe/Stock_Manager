from django import forms
from .models import Categoria, Produto, Estoque


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'categoria']
    
    def __init__(self, *args, **kwargs):
        estoque = kwargs.pop('estoque', None)
        super().__init__(*args, **kwargs)
        if estoque:
            self.fields['categoria'].queryset = estoque.categoria.all()

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['nome']

class SelecionarEstoqueForm(forms.Form):
    estoque = forms.ModelChoiceField(queryset=Estoque.objects.none(), label="Selecione o estoque antes de gerenciá-lo", empty_label=" ")

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)
        if usuario:
            self.fields['estoque'].queryset = Estoque.objects.filter(usuario=usuario)
