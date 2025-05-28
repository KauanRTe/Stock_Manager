from django import forms
from .models import Movimentacao

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['produto', 'tipo', 'quantidade', 'fornecedor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fornecedor'].required = False
        choices = [c for c in self.fields['tipo'].choices if c[0] != '']
        self.fields['tipo'].choices = [('', 'Selecione um tipo')] + choices
        self.fields['tipo'].widget.attrs['class'] = "w-full p-2 mb-6 text-sm focus:outline-none text-gray-900 shadow-lg rounded-lg focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

        choices = [c for c in self.fields['produto'].choices if c[0] != '']
        self.fields['produto'].choices = [('', 'Selecione um produto')] + choices
        self.fields['produto'].widget.attrs['class'] = "w-full p-2 mb-6 text-sm focus:outline-none text-gray-900 shadow-lg rounded-lg focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

        choices = [c for c in self.fields['fornecedor'].choices if c[0] != '']
        self.fields['fornecedor'].choices = [('', 'Selecione um fornecedor')] + choices
        self.fields['fornecedor'].widget.attrs['class'] = "w-full p-2 mb-6 text-sm focus:outline-none text-gray-900 shadow-lg rounded-lg focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

        self.fields['quantidade'].widget.attrs['class'] = "w-full p-2 mb-6 text-sm focus:outline-none text-gray-900 shadow-lg rounded-lg focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"