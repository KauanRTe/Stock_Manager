from django.contrib import admin
from .models import Fornecedor

# Register your models here.
@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'cnpj', 'email', 'endereco')
    search_fields = ('nome',)
