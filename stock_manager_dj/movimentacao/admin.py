from django.contrib import admin
from .models import Movimentacao
# Register your models here.

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'quantidade', 'data')
    list_filter = ('tipo', 'data')
    
