from django import forms
from .models import Categoria
from .models import Produto

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