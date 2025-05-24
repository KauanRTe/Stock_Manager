from django import forms
from .models import Movimentacao

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['produto', 'tipo', 'quantidade', 'fornecedor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fornecedor'].required = False

        for field_name, field in self.fields.items():
                if isinstance(field.widget, forms.Select):
                    field.widget.attrs.update({
                        "class": "block w-40 h-3 p-2 mb-6 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                    })