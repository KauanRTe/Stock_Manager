from django.db import models
from estoque.models import Produto
from fornecedores.models import Fornecedor

# Create your models here.
class Movimentacao(models.Model):
    TIPO_MOVIMENTACAO = [
        ('entrada', 'Entrada'),
        ('saida', 'Saida'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="movimentacoes")
    tipo = models.CharField(max_length=10, choices=TIPO_MOVIMENTACAO)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo.capitalize()} - {self.produto.nome} ({self.quantidade})"
